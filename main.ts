input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (die == 2) {
        die = 10
    } else {
        die = die - 1
    }
    
    if (die == 10) {
        basic.showNumber(0)
    } else {
        basic.showNumber(die)
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (die == 10) {
        die = 2
    } else {
        die = die + 1
    }
    
    if (die == 10) {
        basic.showNumber(0)
    } else {
        basic.showNumber(die)
    }
    
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    basic.pause(100)
    music.play(music.createSoundExpression(WaveShape.Noise, 2838, 2178, 203, 180, 500, SoundExpressionEffect.Warble, InterpolationCurve.Linear), music.PlaybackMode.UntilDone)
    if (die == 10) {
        basic.showNumber(randint(0, 9))
    } else {
        basic.showNumber(randint(1, die))
    }
    
    basic.pause(500)
    basic.clearScreen()
})
let die = 0
music.play(music.stringPlayable("C5 G B A F A C5 B ", 600), music.PlaybackMode.UntilDone)
die = 2
basic.showLeds(`
    . # # . .
    # . . . .
    # . # # .
    # . . # .
    . # # . .
    `)
basic.forever(function on_forever() {
    
})
