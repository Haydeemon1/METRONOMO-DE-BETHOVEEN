#------------------Script para graficación del metrónomo de Beethoven---------------------
#Importación de las librerias del programa
from scipy.special import factorial2
from numpy import sin, deg2rad
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider,Button

#Función de la sumataria para el angulo theta
def fun_ang(theta):
    serie_sum=np.array([( factorial2(2*n-1)/factorial2(2*n)*(sin(deg2rad(theta)/2))**(2*n))**2 for n in range(1,151)])
    return 1+ np.sum(serie_sum)

#Función omega para las graficas
def omegas(g,theta,R,r,L,l,M,m,u):
    """Asiganción de cada variable
        g: Gravedad
        theta: Angulo de inclinación
        R:Distancia desde la mitad de la varilla hasta M
        r:Distancia desde la mitad de la varilla hasta m.
        L:Distancia desde el eje hasta el extremo inferior de la varilla
        l:Distancia desde el eje hasta el extremo superior de la varilla
        M:Masa mayor
        m:Masa menor(Es el trapecio que se desliza en el metronómo)
        u:Masa de la varilla
    """
    Mp=M/m #Variable M prima que corresponde a la formula M/m
    up=u/m #Variable u prima que corresponde a la formula u/m
    #Fórmula de la ecuación #5
    a_0=(g/(fun_ang(theta)**2))*((Mp*R)-((up/2)*(l-L)))/((Mp*(R**2))+((up/3)*((L**2)+(l**2)-(l*L))))
    #Fórmula de la ecuación #6
    b_2=-(1/((Mp*(R**2))+((up/3)*((L**2)+(l**2)-(l*L)))))
    #Fórmula de la ecuación #4
    omega=((a_0+(b_2*g)/fun_ang(theta)**2)/(1-(b_2*r**2)))#En función de la Ec[5], Ec[6] y la sumatoria
    return omega

r_grafica=np.linspace(40,218,25)#Intervalo de evaluación de Ω
g,theta,M,m,R,u,l,L,r=9,50,32,8,2,3.6,2,1,r_grafica#Parameteros iniciales de la gráfica

#Propiedades de la gráfica
fig = plt.figure()#Asignación de la variable fig, la creación de una nueva figura
ax = fig.subplots()#Creación de un subgráfico
plt.subplots_adjust(left = 0.08, bottom = 0.5, right=0.92)#Ajuste del subgráfico para una mejor apreciación
plt.grid()
plt.xlabel("r[mm]",size=15,color="teal")#Nombre para el eje x
plt.ylabel("Ω[]",size=15,color="teal")#Nombre para el eje y
plt.ylim(0,225)#Delimitamos el eje y, para que exista una mejor apreciación 
plt.title("Metrónomo de Beethoven",fontdict = {'family': 'serif', 
                    'color' : 'teal',
                    'weight': 'bold',
                    'size': 15})#Asignación del titulo de la gráfica
p, = ax.plot(r_grafica, omegas(g,theta,R,r,L,l,M,m,u),'-ok',color="indianred",label="Metrónomo de Beethoven")#Graficación
plt.legend()#Creación de la leyenda
#------Sliders de las variables---------
#Gravedad
slr_g=plt.axes([0.08,0.35,0.35,0.05])#Ubicación del slider de la gravedad
#Parametros del slider gravedad
tl_slr_g=Slider(ax=slr_g,
                label=("g[mm/s^2]"),#Nombre
                valmin=400,#Valor mínimo
                valmax=9800,#Valor máximo
                valinit=g,#Valor inicial del gráfico
                valstep=100.5,#Valor de variación
                color="cornflowerblue")
#Theta
slr_theta=plt.axes([0.08,0.27,0.35,0.05])#Ubicación del slider del angulo theta
#Parametros del slider gravedad
tl_slr_t=Slider(ax=slr_theta,
                label="θ[°]",#Nombre
                valmin=40,#Valor mínimo
                valmax=60,#Valor máximo
                valinit=theta,#Valor inicial del gráfico
                valstep=1,#Valor de variación
                color="royalblue")
#Masa mayor
slr_M=plt.axes([0.08,0.19,0.35,0.05])#Ubicación del slider de la masa mayor
#Parametros del slider gravedad
tl_slr_M=Slider(ax=slr_M,
                label=("M[g]"),#Nombre
                valmin=30,#Valor mínimo
                valmax=60,#Valor máximo
                valinit=M,#Valor inicial del gráfico
                valstep=0.1,#Valor de variación
                color="cornflowerblue")
#Masa menor
slr_m=plt.axes([0.08,0.11,0.35,0.05])#Ubicación del slider de la masa menor
#Parametros del slider gravedad
tl_slr_m=Slider(ax=slr_m,
                label=("m[g]"),#Nombre
                valmin=7,#Valor mínimo
                valmax=20,#Valor máximo
                valinit=m,#Valor inicial del gráfico
                valstep=0.1,#Valor de variación
                color="royalblue")
#Radio mayor
slr_R=plt.axes([0.57,0.35,0.35,0.05])#Ubicación del slider del radio mayor
#Parametros del slider gravedad
tl_slr_R=Slider(ax=slr_R,
                label="R[mm]",#Nombre
                valmin=3,#Valor mínimo
                valmax=7,#Valor máximo
                valinit=R,#Valor inicial del gráfico
                valstep=0.1,#Valor de variación
                color="cornflowerblue")
#Miu
slr_u=plt.axes([0.57,0.27,0.35,0.05])#Ubicación del slider del miu
#Parametros del slider gravedad
tl_slr_u=Slider(ax=slr_u,
                label="u",#Nombre
                valmin=3.5,#Valor mínimo
                valmax=10,#Valor máximo
                valinit=u,#Valor inicial del gráfico
                valstep=0.1,#Valor de variación
                color="royalblue")
#Longitud menor
slr_l=plt.axes([0.57,0.19,0.35,0.05])#Ubicación del slider de la longitud menor
#Parametros del slider gravedad
tl_slr_l=Slider(ax=slr_l,
                label="l[mm]",#Nombre
                valmin=13,#Valor mínimo
                valmax=20,#Valor máximo
                valinit=l,#Valor inicial del gráfico
                valstep=0.1,#Valor de variación
                color="cornflowerblue")
#Longitud mayor
slr_L=plt.axes([0.57,0.11,0.35,0.05])#Ubicación del slider de la longitud mayor
#Parametros del slider gravedad
tl_slr_L=Slider(ax=slr_L,
                label="L[mm]",#Nombre
                valmin=3,#Valor mínimo
                valmax=7,#Valor máximo
                valinit=L,#Valor inicial del gráfico
                valstep=0.1,#Valor de variación
                color="royalblue")

#Función para actualizar los datos 
def update(val):
    del ax.lines[0]#Eliminación gráfica anterior
    #Graficación de los valores de los sliders
    p, = ax.plot(r_grafica, omegas(tl_slr_g.val,tl_slr_t.val,tl_slr_R.val,r_grafica,tl_slr_L.val,tl_slr_l.val,tl_slr_M.val,tl_slr_m.val,tl_slr_u.val),'-ok',color="indianred")
#Actualización de datos
tl_slr_g.on_changed(update)
tl_slr_t.on_changed(update) 
tl_slr_M.on_changed(update)
tl_slr_m.on_changed(update)
tl_slr_R.on_changed(update)
tl_slr_u.on_changed(update)
tl_slr_l.on_changed(update)
tl_slr_L.on_changed(update)
#Boton de reseteo
ax_Graficar = plt.axes([0.85, 0.90, 0.1, 0.05])#Ubicación del boton
Reinicar_Grafico=Button(ax=ax_Graficar,
                        label='Reset',
                        color="lightgray")

#Función para regresar las variables a sus valores iniciales 
def reset(event):
    tl_slr_g.reset()
    tl_slr_t.reset()
    tl_slr_M.reset()
    tl_slr_m.reset()
    tl_slr_R.reset()
    tl_slr_u.reset()
    tl_slr_l.reset()
    tl_slr_L.reset()

#Evento para el boton de reseteo(Llama a la función reset)    
Reinicar_Grafico.on_clicked(reset)
plt.show()#Muestra la gráfica