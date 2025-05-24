from skyfield.api import load
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation


planets=load('de421.bsp')

ts=load.timescale()
times=ts.utc(2025,1,range(1,101))


earth=planets['earth']
moon=planets['moon']

x,y=[],[]


for t in times:
    posi=earth.at(t).observe(moon).apparent().position.km
    x.append(posi[0])
    y.append(posi[1])
   
    
fig,ax=plt.subplots()
ax.set_xlim(-450000,450000)
ax.set_ylim(-450000,450000)
ax.set_aspect('equal')

ax.set_title('Earth and Moon simulation')
ax.set_xlabel('X in Km')
ax.set_ylabel('Y in km')
ax.grid(True)
ax.scatter(0,0,color='blue',s=100,label='Earth')
moon,=ax.plot([],[],'ro',label='moon')
moon_trail,=ax.plot([],[],'r--',linewidth=1)
ax.legend()

def init():
    moon.set_data([],[])
    moon_trail.set_data([],[])
    return moon,moon_trail
def update(frame):
    moon.set_data([x[frame]],[y[frame]])
    moon_trail.set_data(x[:frame+1],y[:frame+1])
    return moon,moon_trail

ani=FuncAnimation(fig,update,frames=len(times),init_func=init,interval=100,blit=True)
plt.show()
