import numpy as np
import matplotlib.pyplot as plt

U = np.random.rand(102, 102)
V = np.random.rand(102, 102)
dx = 0.02
dt = 0.001
T = 15
a = 6
Dv = 5 * 10**(-3)

k = np.linspace(-0.5, 0.15, 3)
Du = np.linspace(3e-5, 1.4e-4, 3)

fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(16, 9))
fig.suptitle('Horizontally stacked subplots')


def laplacian(Z):
    Ztop = Z[0:-2, 1:-1]
    Zleft = Z[1:-1, 0:-2]
    Zbottom = Z[2:, 1:-1]
    Zright = Z[1:-1, 2:]
    Zcenter = Z[1:-1, 1:-1]
    return (Ztop + Zleft + Zbottom + Zright -4 * Zcenter) / dx**2


steps = int(round(float(T)/dt))

def show_img_depends_on_k_and_Du(k, Du, i):
    for step in range(steps):
        deltaU = laplacian(U)
        deltaV = laplacian(V)

        Uc = U[1: -1, 1: -1]
        Vc = V[1: -1, 1: -1]

        U[1: -1, 1: -1] = Uc + dt * (Du * deltaU + Uc - Uc**3 - Vc + k)
        V[1: -1, 1: -1] = Vc + dt * (Dv * deltaV + Uc - Vc) * a

        for Z in (U, V):
            Z[0, :] = Z[1, :]
            Z[-1, :] = Z[-2, :]
            Z[:, 0] = Z[:, 1]
            Z[:, -1] = Z[:, -2]
    if i == 1:
        ax1.imshow(U)
        ax1.set_title('k = 0.15, Du = 1.4 * 10**(-4) - ax1')
    elif i == 2:
        ax2.imshow(U)
        ax2.set_title("k = 0, Du = 1*10**(-4) - ax2")
    elif i == 3:
        ax3.imshow(U)
        ax3.set_title("k = -0.5, Du = 3*10**(-5) - ax3")
    elif i == 4:
        ax4.imshow(U)
        ax4.set_title("k = -0.5, Du = 1.4*10**(-4) - ax4")


show_img_depends_on_k_and_Du(0.15, 1.4*10**(-4), 1)
show_img_depends_on_k_and_Du(0, 1*10**(-4), 2)
show_img_depends_on_k_and_Du(-0.5, 3*10**(-5), 3)
show_img_depends_on_k_and_Du(-0.5, 1.4*10**(-4), 4)

plt.show()



