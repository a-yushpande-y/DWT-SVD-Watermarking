def get_x_array(x0, u, h):
    x = []
    a=100
    b=100
    c=x0
    while len(x)<(h*h):
        c = u * c * (1.0 - c)
        x.append(c)
    for i in range(0,h*h):
        if(round(b*x[i])<(b*x[i])):
            x[i]=int((round(a*(b*x[i]-round(b*x[i]))))%256)
        if(round(b*x[i])>(b*x[i])):
            x[i]=int((round(a*(1-b*x[i]-round(b*x[i]))))%256)
    return x

