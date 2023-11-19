let currenttemperature = 0
basic.forever(function on_forever() {
    
    currenttemperature = input.temperature()
    led.plotBarGraph(currenttemperature, 50)
})
