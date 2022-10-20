from matplotlib import pyplot
import numpy

with open('settings.txt', 'r') as file:
    for line in file.readlines():
        if (line != '\n'):
            tmp = tuple([item for item in line.split()])
            s_freq = float(tmp[2])
            step = float(tmp[5])
data_array = numpy.loadtxt('data.txt', dtype=float)
t = []
u = []
count = 0
with open('data.txt', 'r') as data:
    for line in data.readlines():
        if line != '\n':
            count += 1
            x, y = tuple([float(item) for item in line.split()])
            t.append(x)
            u.append(y)
fig, ax = pyplot.subplots(figsize=(16, 10), dpi=400)
ax.axis(xmin = 0, xmax = max(t), ymin = 0, ymax=max(u))
ax.set_xlabel('время t')
ax.set_ylabel('напряжение u')
ax.set_title('Зависимость напряжения от времени')
ax.plot(t, u, 'o-', ms = 10, c = 'g', label = 'U(t)', markevery=1000)
ax.minorticks_on()
ax.grid(which='major')
ax.grid(which='minor', linestyle = ':')
ax.legend()
ax.text(80, 1.2, 'Время зарядки конденсатора 138 с')
ax.text(80, 1, 'Время разрядки конденсатора 122 с')
fig.savefig('graph.png')
pyplot.show()