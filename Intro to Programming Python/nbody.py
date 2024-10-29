import math

earth = [1.4960e+11, 0.0000e+00, 0.0000e+00, 2.9800e+04, 5.9740e+24]
mars = [2.2790e+11, 0.0000e+00, 0.0000e+00, 2.4100e+04, 6.4190e+23]
mercury = [5.7900e+10, 0.0000e+00, 0.0000e+00, 4.7900e+04, 3.3020e+23]
sun = [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 1.9890e+30]
venus = [1.0820e+11, 0.0000e+00, 0.0000e+00, 3.5000e+04, 4.8690e+24]
planets = [earth, mars, mercury, sun, venus]

N = 5
G = 6.67E-11
px = [planet[0] for planet in planets]
py = [planet[1] for planet in planets]
vx = [planet[2] for planet in planets]
vy = [planet[3] for planet in planets]
m = [planet[4] for planet in planets]

SUN = 3

t_total = 0.0
dt = 25000.0 # delta t
t = 157788000 # total simulation time

while t_total < t:
    for i in range(N):
        # skip the sun
        if i == SUN:
            continue

        #calculate delta_x and delta_y for current timestep
        delta_x = (px[SUN] - px[i]) 
        delta_y = (py[SUN] - py[i]) 

        # calculate the radius between i'th planet and the sun
        r = math.sqrt(delta_x**2 + delta_y**2)

        # calculate the pair-wise force between i'th planet and the sun
        F = (G * (m[i]) * (m[SUN])) / (r**2)

        # calculate the x and y components of the force
        fx = F * ((delta_x/r))
        fy = F * ((delta_y/r))

        # calculate the x and y components of the acceleration
        # for the current timestep
        ax = fx / m[i]
        ay = fy / m[i]

        # calculate the x and y components of the velocity
        # for the next time step
        vx[i] += ax * dt
        vy[i] += ay * dt

        # calculate the x and y components of the resulting position
        px[i] += vx[i] * dt
        py[i] += vy[i] * dt

    # update the time by delta_t
    t_total += dt
# output the formatted values for the x and y components of position/velocity and mass
for i in range(N):
    # print formatted output for each planet
    print(f"{px[i]:.4e} {py[i]:.4e} {vx[i]:.4e} {vy[i]:.4e} {m[i]:.4e}")