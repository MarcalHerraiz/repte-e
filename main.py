currenttemperature = 0

def on_forever():
    global currenttemperature
    currenttemperature = input.temperature()
    led.plot_bar_graph(currenttemperature, 50)
basic.forever(on_forever)
