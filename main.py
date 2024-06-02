def on_button_pressed_a():
    global die
    if die == 2:
        die = 10
    else:
        die = die - 1
    if die == 10:
        basic.show_number(0)
    else:
        basic.show_number(die)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global die
    if die == 10:
        die = 2
    else:
        die = die + 1
    if die == 10:
        basic.show_number(0)
    else:
        basic.show_number(die)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    basic.pause(100)
    music.play(music.create_sound_expression(WaveShape.NOISE,
            2838,
            2178,
            203,
            180,
            500,
            SoundExpressionEffect.WARBLE,
            InterpolationCurve.LINEAR),
        music.PlaybackMode.UNTIL_DONE)
    if die == 10:
        basic.show_number(randint(0, 9))
    else:
        basic.show_number(randint(1, die))
    basic.pause(500)
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

die = 0
music.play(music.string_playable("C5 G B A F A C5 B ", 600),
    music.PlaybackMode.UNTIL_DONE)
die = 2
basic.show_leds("""
    . # # . .
    # . . . .
    # . # # .
    # . . # .
    . # # . .
    """)

def on_forever():
    pass
basic.forever(on_forever)
