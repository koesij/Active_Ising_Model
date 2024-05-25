import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

###########################define constant and variables###########################
Lx = 400
Ly = 100
beta = 1.8
rho = 3.0
e = 0.9000 #epsilon
tf = 1500
D = 1 #diffusion coefficient

dt = 1 / (4.0 * D + np.exp(beta))
prob_move = 2.0 * dt
prob_move2 = 2.0 * prob_move
L2 = Lx * Ly
N = int(L2 * rho)
t = 0

total_timesteps = int(tf / dt)

class Ptcl:
    def __init__(self, pos, spin):
        self.pos = pos
        self.spin = spin

nn = np.zeros((L2, 4), dtype=int)
for i in range(L2):
    #right
    if (i%Lx==Lx-1):
        nn[i, 0] = i + 1 - Lx
    else: 
        nn[i, 0] = i + 1
    #left
    if (i%Lx==0):
        nn[i, 1] = i - 1 + Lx
    else:
        nn[i, 1] = i - 1
    #up
    if (i//Lx==0):
        nn[i, 2] = i - Lx + L2
    else:
        nn[i, 2] = i - Lx
    #down
    if (i//Lx==Ly-1):
        nn[i, 3] = i + Lx - L2
    else:
        nn[i, 3] = i + Lx
        
ptcl = [Ptcl(random.randint(0, L2 - 1), random.choice([-1, 1])) for _ in range(N)]
next_ptcl = [Ptcl(0, 0) for _ in range(N)]

density = np.zeros(L2, dtype=int)
magnetization = np.zeros(L2, dtype=int)

for n in range(N): 
    density[ptcl[n].pos] += 1
    magnetization[ptcl[n].pos] += ptcl[n].spin
    

# positions_over_time = np.zeros((total_timesteps, N, 2))
density_over_time = np.zeros((total_timesteps, L2))
magnetization_over_time = np.zeros((total_timesteps, L2))

###########################Simulation###########################
for current_step in range(total_timesteps):
    
    next_density = np.zeros(L2, dtype=int)
    next_magnetization = np.zeros(L2, dtype=int)
    next_ptcl = []
    current_positions = np.zeros((N, 2))  

    for n in range(N):
        pos, spin = ptcl[n].pos, ptcl[n].spin
        prob_r = 0.5 * (1.0 + spin * e)
        
        if density[pos] == 0:
            prob_flip = 1
        else:
            exponent = -beta * spin * magnetization[pos] / max(1, density[pos])
            prob_flip = np.exp(exponent) * dt
        prob = random.random()

        next_pos = pos
        next_spin = spin

        # Horizontal hopping
        if prob < prob_move:
            if random.random() < prob_r:
                next_pos = nn[pos][0]
            else:
                next_pos = nn[pos][1]
                
        # Vertical hopping
        elif prob < prob_move2:
            if random.random() < 0.5:
                next_pos = nn[pos][2]
            else:
                next_pos = nn[pos][3]
                
        # Spin change
        elif prob < prob_move2 + prob_flip:
            next_spin = -spin

        # y, x = divmod(next_pos, Lx)  # Correctly mapping linear index to 2D coordinates
        # current_positions[n] = [x, y]  # Adjusted to match the typical (row, column) ordering
        next_density[next_pos] += 1
        next_magnetization[next_pos] += next_spin
        next_ptcl.append(Ptcl(next_pos, next_spin))

    # positions_over_time[current_step] = current_positions
    density = next_density
    magnetization = next_magnetization
    
    density_over_time[current_step] = density
    magnetization_over_time[current_step] = magnetization
    ptcl = next_ptcl.copy()

    t += dt

###########################Reshape###########################    
time_steps = density_over_time.shape[0]
coordinated_density = np.zeros((time_steps, Lx, Ly), dtype=int)

# Reshape each time step
for t in range(density_over_time.shape[0]):
    for i in range(density_over_time.shape[1]):
        y, x = divmod(i, Lx)
        coordinated_density[t, x, y] = density_over_time[t, i]
        
time_steps = magnetization_over_time.shape[0]
coordinated_magnetization = np.zeros((time_steps, Lx, Ly), dtype=int)

# Reshape each time step
for t in range(magnetization_over_time.shape[0]):
    for i in range(magnetization_over_time.shape[1]):
        y, x = divmod(i, Lx)
        coordinated_magnetization[t, x, y] = magnetization_over_time[t, i]
        

###########################Animation###########################    
time_steps, Lx, Ly = coordinated_density.shape

# Create a figure and axis for the animation
fig, ax = plt.subplots(figsize=(8, 8))

# Initial frame setup
c = ax.imshow(coordinated_density[0].T, animated=True, cmap='viridis', 
              extent=[0, Lx, 0, Ly], vmin=coordinated_density.min(), vmax=coordinated_density.max())
ax.set_title('Gas Spinodal Decomposition (Density), Time = 0')
fig.colorbar(c)

def animate(i):
    """Updates the plot for each frame."""
    # Update the image data and title for each frame
    c.set_data(coordinated_density[i].T)
    ax.set_title(f'Gas Spinodal Decompostion (Density), Time = {i*dt:.2f}')
    return c,

# Create the animation using FuncAnimation
ani = FuncAnimation(fig, animate, frames=time_steps, blit=True)

# Save the animation
ani.save(f'gas_spin_den_{tf}.gif', writer='imagemagick')

# Close the figure to avoid memory issues
plt.close(fig)


time_steps, Lx, Ly = coordinated_magnetization.shape
abs_max = np.abs(coordinated_magnetization).max()

# Create a figure and axis for the animation
fig, ax = plt.subplots(figsize=(8, 8))


# Initial frame setup
c = ax.imshow(coordinated_magnetization[0].T, animated=True, cmap='coolwarm',
              extent=[0, Lx, 0, Ly], vmin=-abs_max, vmax=abs_max)

ax.set_title('Gas Spinodal Decomposition (Magnetization), Time = 0')
fig.colorbar(c)

def animate(i):
    """Updates the plot for each frame."""
    # Update the image data and title for each frame
    c.set_data(coordinated_magnetization[i].T)
    ax.set_title(f'Gas Spinodal Decomposition (Magnetization), Time = {i*dt:.2f}')
    return c,

# Create the animation using FuncAnimation
ani = FuncAnimation(fig, animate, frames=time_steps, blit=True)

# Save the animation
ani.save(f'gas_spin_mag_{tf}.gif', writer='imagemagick')

# Close the figure to avoid memory issues
plt.close(fig)