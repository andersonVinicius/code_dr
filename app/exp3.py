

m = 90 #kg
distance = 5000 # m
vg = 15# m/s
vw = 12# m/s
vp = vg + vw# m/s
g = 9.8 #m/s


t = distance/vg

print('Equation1a:',((0.5*m*(vp**2)*t) + (m * g * t) )/1000)

print('Equation1b:',( ( (m*(vp**2)*distance) + (m*distance*g))/ (2 * vg) ) /1000)

Cd = 0.54  # drag coefficient
A = 1.2  # m - front surface of UAV
D = 1.2754  # kgm3 - air density
b = 8.7  # m - UAV width
payload = m #UAV weight + payload

p = (0.5 * Cd * A * D * ((vp) ** 3)) + ((  ((payload) ** 2)) / (D * (b ** 2) * vp))
t = distance / vg
#t = np.ceil(t)

print('Equation2:',(p*t)/1000  )
p = (0.5 * Cd * A * D * ((vp) ** 3))
print('Equation2 p_1:',(p*t)/1000  )
p = ((  ((payload) ** 2)) / (D * (b ** 2) * vp))
print('Equation2 p_2:',(p*t)/1000  )