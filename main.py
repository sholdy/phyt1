import math

if __name__ == '__main__':
    x, y, z = 45, -38, 44
    f = ((math.sin(math.pow(z, 2)-10*y-30)+math.fabs(y))/((math.tan(math.exp(x)-math.log1p(x))+math.tan(x))) - (21*math.pow(y, 3)+95 * math.pow(x, 5)-77)/(54*math.pow(z, 7)-math.tan(x)+5)+50*x-math.pow(y,2))
    print '%e' %f