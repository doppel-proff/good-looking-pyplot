import os
import numpy as np
from matplotlib import pyplot as plt

from utils import graph_utils as gu
from theme import nord_colors as nc

Path = os.getcwd()
#Figname = os.path.join(Path, "fig.png")
Figname = os.path.join(Path, "fig.svg")

V_x = np.linspace(0,1,100)
def f (V_x : np.ndarray, lam : int ) -> np.ndarray :
    V_Id = np.asarray([1 for i in range(len(V_x))])
    return V_Id - np.exp(-lam*V_x) 

fig, axs = plt.subplots(2,2, figsize= (12, 8), constrained_layout = True)

ax1=axs[0][0]
ax1.plot(V_x, f(V_x, 10), label=r"$f(\lambda, x)$", color= nc.blue)

ax1.set_title(r"$\lambda = 10$", fontsize = 14)
ax1.set_ylabel(r"$f(\lambda , x)$", fontsize = 12)
ax1.set_xlabel("x", fontsize= 12)
ax1=gu.pretty_ax(ax1, nc.fg2)


ax2 = axs[0][1]
ax2.plot(V_x, f(V_x, 5), label=r"$f(\lambda, x)$", color= nc.orange)
ax2.set_xlabel("x", fontsize= 12)
ax2.set_title(r"$\lambda = 5$", fontsize = 14)
ax2 = gu.pretty_ax(ax2, nc.fg2)

ax3 = axs[1][0]
ax3.plot(V_x, f(V_x, 10), label=r"$f(\lambda, x)$", color= nc.blue)
ax3.plot(V_x, f(V_x, 5), label=r"$f(\lambda, x)$", color= nc.orange)
ax3.set_title(r"$\lambda = 10$ vs $\lambda = 5$")
ax3.set_ylabel(r"$f(\lambda , x)$", fontsize = 12)
ax3.set_xlabel("x", fontsize= 12)
ax3=gu.pretty_ax(ax3, nc.fg2)

ax4 = axs[1][1]
ax4.plot(f(V_x,5),f(V_x, 10), label=r"$f(\lambda, x)$", color=nc.green)
ax4.set_title(r"$\forall x \in [0,1] $", fontsize = 14)
ax4.set_ylabel(r"$f(\lambda = 10, x)$", fontsize = 12)
ax4.set_xlabel(r"$f(\lambda = 5, x)$", fontsize = 12)
ax4=gu.pretty_ax(ax4, nc.fg2)

plt.savefig(Figname, dpi=300)
print(f"fig saved as : {Figname}")
plt.close
