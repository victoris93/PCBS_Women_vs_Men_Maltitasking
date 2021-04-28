import glob
from expyriment import design, control, stimuli, misc

#control.set_develop_mode(True)

SQUARE_RESPONSE_KEY = misc.constants.K_s # if the task is "shape"
DIAMOND_RESPONSE_KEY = misc.constants.K_l

TWO_CIRCLES_RESPONSE_KEY = misc.constants.K_s # if the task is "filling"
THREE_CIRCLES_RESPONSE_KEY = misc.constants.K_l

N_TRIALS = 40
INTER_TRIAL_INTERVAL = 800
MAX_RESPONSE_DELAY = 4000
INSTRUCTION_REMINDER_AFTER_INCORRECT_RESPONSE = 5000
PAUSE = 500

INSTRUCTIONS =  """Your task is to report the shape of the frame of the figure if it appears in the top part of the screen labeled "shape". If the frame is a square, press S on the keyboard. If it is a diamond, press L.
    If the figure appears in the bottom part of the screen labeled "filling", you task is to report the number of circles inside of the frame. If you see 2 circles, press S on the keyboard. If you see 3 circles, press L.

    Let's start with a bit of training.

    Press the space bar to start
    
    To exit the experiment, press escape."""
    
REMINDER_INSTRUCTIONS: """Your task is to report the shape of the frame of the figure if it appears in the top part of the screen labeled "shape". If the frame is a square, press S on the keyboard. If it is a diamond, press L.
    If the figure appears in the bottom part of the screen labeled "filling", you task is to report the number of circles inside of the frame. If you see 2 circles, press S on the keyboard. If you see 3 circles, press L.

    Press the space bar when you are ready.
    
    To exit the experiment, press escape."""

exp_1 = design.Experiment(name="Task Switching", text_size=40)
control.initialize(exp_1)
kb = expyriment.io.Keyboard()

# kb = expyriment.io.Keyboard()
stimuli_block = design.Block()

for pngfile in glob.glob('shape_square*.png'):
    trial = design.Trial()
    trial.add_stimulus(stimuli.Picture(pngfile))
    trial.set_factor('task_type', 'shape_square')
    stimuli_block.add_trial(trial)

for pngfile in glob.glob('shape_diamond*.png'):
 	trial = design.Trial()
 	trial.add_stimulus(stimuli.Picture(pngfile))
 	trial.set_factor('task_type', 'shape_diamond')
 	stimuli_block.add_trial(trial)

for pngfile in glob.glob('filling*2*.png'):
    trial = design.Trial()
    trial.add_stimulus(stimuli.Picture(pngfile))
    trial.set_factor('task_type', 'filling_2_circles')
    stimuli_block.add_trial(trial)
    
for pngfile in glob.glob('filling*3*.png'):
    trial = design.Trial()
    trial.add_stimulus(stimuli.Picture(pngfile))
    trial.set_factor('task_type', 'filling_3_circles')
    stimuli_block.add_trial(trial)

stimuli_block.shuffle_trials()

blankscreen = stimuli.BlankScreen()
instructions = stimuli.TextScreen("Instructions:", heading_size = 60, text = INSTRUCTIONS)
reminder_if_incorrect_response =  stimuli.TextScreen("Your response was incorrect. Instructions reminder:", heading_size = 60, text =  REMINDER_INSTRUCTIONS)    
#exp_1.add_data_variable_names(['trial', 'wait', 'respkey', 'RT'])

instructions.present()
kb.wait_char(' ')
control.start()

for i_trial in range(N_TRIALS):
    for trial in stimuli_block.trials:
        blankscreen.present()
        exp_1.clock.wait(INTER_TRIAL_INTERVAL)
        trial.stimuli[0].present(update=True, clear=True) 
        key, rt = exp_1.keyboard.wait(duration=MAX_RESPONSE_DELAY)
        if key == None:
        	is_correct = None
        if trial.get_factor('task_type') == "shape_square": 
        	is_correct = (key == SQUARE_RESPONSE_KEY)
        elif  trial.get_factor('task_type') == "shape_diamond": 
        	is_correct = (key == DIAMOND_RESPONSE_KEY)
        elif trial.get_factor('task_type') == "filling_2_circles":
        	is_correct = (key == TWO_CIRCLES_RESPONSE_KEY)
        elif trial.get_factor('task_type') == "filling_2_circles":
        	is_correct = (key == THREE_CIRCLES_RESPONSE_KEY)
        if  is_correct == False:
        	reminder_if_incorrect_response.present()
        	exp_1.clock.wait(INSTRUCTION_REMINDER_AFTER_INCORRECT_RESPONSE)
        	blankscreen.present()
        	exp_1.clock.wait(PAUSE)
        	

control.end()
    