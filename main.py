def on_button_pressed_a():
    global entry
    entry = "" + entry + "A"
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global entry
    if passward == entry:
        pins.digital_write_pin(DigitalPin.P1, 1)
        basic.show_icon(IconNames.YES)
        basic.pause(10000)
        pins.servo_write_pin(AnalogPin.P0, 90)
        pins.digital_write_pin(DigitalPin.P1, 0)
    else:
        pins.digital_write_pin(DigitalPin.P2, 1)
        basic.show_icon(IconNames.NO)
        basic.pause(2000)
        pins.digital_write_pin(DigitalPin.P2, 0)
    basic.pause(500)
    basic.clear_screen()
    entry = ""
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global entry
    entry = "" + entry + "B"
input.on_button_pressed(Button.B, on_button_pressed_b)

entry = ""
passward = ""
passward = "AABAA"
entry = ""
pins.servo_write_pin(AnalogPin.P0, 0)