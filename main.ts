input.onButtonPressed(Button.A, function () {
    entry = "" + entry + "A"
})
input.onButtonPressed(Button.AB, function () {
    if (passward == entry) {
        pins.digitalWritePin(DigitalPin.P1, 1)
        basic.showIcon(IconNames.Yes)
        basic.pause(10000)
        pins.servoWritePin(AnalogPin.P0, 90)
        pins.digitalWritePin(DigitalPin.P1, 0)
    } else {
        pins.digitalWritePin(DigitalPin.P2, 1)
        basic.showIcon(IconNames.No)
        basic.pause(2000)
        pins.digitalWritePin(DigitalPin.P2, 0)
    }
    basic.pause(500)
    basic.clearScreen()
    entry = ""
})
input.onButtonPressed(Button.B, function () {
    entry = "" + entry + "B"
})
let entry = ""
let passward = ""
passward = "AABAA"
entry = ""
pins.servoWritePin(AnalogPin.P0, 0)
