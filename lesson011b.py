# The distance (m) and time (s) travelled by three projectiles were recorded in
# an experiment.  Write a Python code to build a table that adequately displays
# the data on the three projectiles: distance, time and velocity (that you must
# obtain by the distance and the time travelled)
# 202 m; 7.5s; v m/s
# 14 m; 2.5s; v m/s
# 312 m; 8.5s; v m/s

def velocity(d, t):
    return d/t

values = (
    (202, 7.5),
    (14, 2.5),
    (312, 8.5)
)

print('-'*30)
print(f"\tD(m)\tT(s)\tv(m/s")
print('-'*30)
for value in values:
    print(f"\t{value[0]}\t\t{value[1]}\t\t{velocity(value[0],value[1]):.2f}")
print('-'*30)
