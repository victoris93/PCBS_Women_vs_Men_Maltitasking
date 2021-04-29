import glob
from expyriment import design, control, stimuli, misc, io

#control.set_develop_mode(True)

SQUARE_RESPONSE_KEY = misc.constants.K_s # if the task is "shape"
DIAMOND_RESPONSE_KEY = misc.constants.K_l

TWO_CIRCLES_RESPONSE_KEY = misc.constants.K_s # if the task is "filling"
THREE_CIRCLES_RESPONSE_KEY = misc.constants.K_l

TRAINING_TRIALS = 40
EXPERIMENT_TRIALS = 192
INTER_TRIAL_INTERVAL = 800
MAX_RESPONSE_DELAY = 4000
INSTRUCTION_REMINDER_AFTER_INCORRECT_RESPONSE = 5000
PAUSE = 500

TRAINING_INSTRUCTIONS =  """Your task is to report the shape of the frame of the figure if it appears in the top part of the screen labeled "shape". If the frame is a square, press S on the keyboard. If it is a diamond, press L.
    If the figure appears in the bottom part of the screen labeled "filling", you task is to report the number of circles inside of the frame. If you see 2 circles, press S on the keyboard. If you see 3 circles, press L.

    Let's start with a bit of training.

    Press the space bar to start
    
    To exit the experiment, press escape."""
    
EXPERIMENT_INSTRUCTIONS = """Every time give an incorrect response, you will get a reminder of the instructions.

    Press the space bar to start
    
    To exit the experiment, press escape."""
    
REMINDER_INSTRUCTIONS = """Your task is to report the shape of the frame of the figure if it appears in the top part of the screen labeled "shape". If the frame is a square, press S on the keyboard. If it is a diamond, press L.
    If the figure appears in the bottom part of the screen labeled "filling", you task is to report the number of circles inside of the frame. If you see 2 circles, press S on the keyboard. If you see 3 circles, press L.

    Press the space bar when you are ready.
    
    To exit the experiment, press escape."""

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
training_instructions = stimuli.TextScreen("Instructions:", heading_size = 60, text = TRAINING_INSTRUCTIONS)
reminder_if_incorrect_response =  stimuli.TextScreen("Your response was incorrect. Instructions reminder:", heading_size = 60, text =  REMINDER_INSTRUCTIONS)   
experiment_instructions =  stimuli.TextScreen("So, you are all set to do the actual experiment! ", heading_size = 60, text =  EXPERIMENT_INSTRUCTIONS) 

def training(N_TRIALS):
	for i_trial in range(N_TRIALS):
		for trial in stimuli_block.trials:
			blankscreen.present()
			exp_1.clock.wait(INTER_TRIAL_INTERVAL)
			trial.stimuli[0].present(update=True, clear=True) 
			key, rt = exp_1.keyboard.wait(duration=MAX_RESPONSE_DELAY)
			if key == None:
				is_correct = None
			elif trial.get_factor('task_type') == "shape_square":
				is_correct = (key == SQUARE_RESPONSE_KEY)
			elif  trial.get_factor('task_type') == "shape_diamond":
				is_correct = (key == DIAMOND_RESPONSE_KEY)
			elif trial.get_factor('task_type') == "filling_2_circles":
				is_correct = (key == TWO_CIRCLES_RESPONSE_KEY)
			elif trial.get_factor('task_type') == "filling_3_circles":
				is_correct = (key == THREE_CIRCLES_RESPONSE_KEY)
			if  is_correct == False:
				reminder_if_incorrect_response.present()
				exp_1.clock.wait(INSTRUCTION_REMINDER_AFTER_INCORRECT_RESPONSE)
				blankscreen.present()
				exp_1.clock.wait(PAUSE)
	
def experiment(N_TRIALS):
	for i_trial in range(N_TRIALS):
		for trial in stimuli_block.trials:
			blankscreen.present()
			exp_1.clock.wait(INTER_TRIAL_INTERVAL)
			trial.stimuli[0].present(update=True, clear=True)
			key, rt = exp_1.keyboard.wait(duration=MAX_RESPONSE_DELAY)
			if key == None:
				is_correct = None
			elif trial.get_factor('task_type') == "shape_square":
				is_correct = (key == SQUARE_RESPONSE_KEY)
			elif  trial.get_factor('task_type') == "shape_diamond":
				is_correct = (key == DIAMOND_RESPONSE_KEY)
			elif trial.get_factor('task_type') == "filling_2_circles":
				is_correct = (key == TWO_CIRCLES_RESPONSE_KEY)
			elif trial.get_factor('task_type') == "filling_3_circles":
				is_correct = (key == THREE_CIRCLES_RESPONSE_KEY)
			if  is_correct == False:
				reminder_if_incorrect_response.present()
				exp_1.clock.wait(INSTRUCTION_REMINDER_AFTER_INCORRECT_RESPONSE)
				blankscreen.present()
				exp_1.clock.wait(PAUSE)
	exp_1.data.add([i_trial, trial.get_factor('task_type'), key, rt, is_correct])

control.initialize(exp_1)
kb = io.Keyboard()
training_instructions.present()
kb.wait_char(' ')
control.start()

training(TRAINING_TRIALS)

experiment_instructions.present()
kb.wait_char(' ')

experiment (EXPERIMENT_TRIALS)

control.end()
    