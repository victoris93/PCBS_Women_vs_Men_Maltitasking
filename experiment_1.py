# Author: Victoria Shevchenko

""" Here, distinct functions are defined for the training and experimental trials. The training function does not collect data and takes the number of trials as imput. The experiment function attributes additional factors to trials (correct_key, is_congruent, is_correct) and collects data. It takes as input a list of stimulus blocks and the number of trials for each block. Subject's sex is retrieved with a separate function and is recorded for every trial. The factors related to stimuli (task, shape of the frame, number of circles) are attributed at the stage of trial block creation. Three blocks are created: pure shape, pure filling and mixed. At the end of the experiment, the script concatenates the generated data in a csv file and saves it to the current directory."""

import os
from expyriment import design, control, stimuli, misc, io

MALE_SEX_KEY = misc.constants.K_m
FEMALE_SEX_KEY =  misc.constants.K_f

SQUARE_RESPONSE_KEY = misc.constants.K_l
DIAMOND_RESPONSE_KEY = misc.constants.K_s

TWO_CIRCLES_RESPONSE_KEY = misc.constants.K_s
THREE_CIRCLES_RESPONSE_KEY = misc.constants.K_l

TRAINING_TRIALS = 40
EXPERIMENT_TRIALS_PER_BLOCK = 64
INTER_TRIAL_INTERVAL = 800
MAX_RESPONSE_DELAY = 4000
INSTRUCTION_REMINDER_AFTER_INCORRECT_RESPONSE = 5000
PAUSE = 500

TRAINING_INSTRUCTIONS =  """Your task is to report the shape of the frame of the figure if it appears in the top part of the screen labeled "shape". If the frame is a square, press L on the keyboard. If it is a diamond, press S.
    If the figure appears in the bottom part of the screen labeled "filling", you task is to report the number of circles inside of the frame. If you see 2 circles, press S on the keyboard. If you see 3 circles, press L. Let's start with a bit of training!
    
    Press the space bar to start.
    To exit the experiment, press escape."""
    
EXPERIMENT_INSTRUCTIONS = """Report the shape of the frame of the figure if it appears in the top part of the screen labeled "shape". If the frame is a square, press L on the keyboard. If it is a diamond, press S. Report the number of circles inside of the frame, if the figure appears in the bottom part of the screen labeled "filling". If you see 2 circles, press S. If you see 3 circles, press L. Every time give an incorrect response, you will get a reminder of the instructions.

    Press the space bar to start.
    To exit the experiment, press escape."""
    
REMINDER_INSTRUCTIONS = """Your task is to report the shape of the frame of the figure if it appears in the top part of the screen labeled "shape". If the frame is a square, press L on the keyboard. If it is a diamond, press S.
    If the figure appears in the bottom part of the screen labeled "filling", you task is to report the number of circles inside of the frame. If you see 2 circles, press S on the keyboard. If you see 3 circles, press L.
    
    To exit the experiment, press escape."""

exp_1 = design.Experiment(name="Task Switching", text_size= 40)
control.initialize(exp_1)

def training(N_TRIALS):
	training_instructions.present()
	kb.wait_char(' ')
	for i_trial in range(N_TRIALS):
		trial = mixed_block.get_random_trial()
		blankscreen.present()
		exp_1.clock.wait(INTER_TRIAL_INTERVAL)
		trial.stimuli[0].present(update=True, clear=True)
		key, rt = exp_1.keyboard.wait(duration=MAX_RESPONSE_DELAY)
		if key == None:
			is_correct = None
		elif trial.get_factor('task') == "shape": #determine the task
			if  trial.get_factor('shape') == "square": #determine correct condition
				is_correct = (key == SQUARE_RESPONSE_KEY) #determine correct key
			elif trial.get_factor('shape') == "diamond":
				is_correct = (key == DIAMOND_RESPONSE_KEY)
		elif trial.get_factor('task') == "filling":
			if  trial.get_factor('number_of_circles') == 2:
				is_correct = (key == TWO_CIRCLES_RESPONSE_KEY)
			elif trial.get_factor('number_of_circles') == 3:
				is_correct = (key == THREE_CIRCLES_RESPONSE_KEY)
		if  is_correct == False:
			reminder_if_incorrect_response.present()
			exp_1.clock.wait(INSTRUCTION_REMINDER_AFTER_INCORRECT_RESPONSE)
			blankscreen.present()
			exp_1.clock.wait(PAUSE)

def experiment(BLOCK_LIST, N_TRIALS):
	experiment_instructions.present()
	kb.wait_char(' ')
	sex=get_subject_sex()
	for BLOCK in BLOCK_LIST:
		for i_trial in range(N_TRIALS):
			trial = BLOCK.get_random_trial() # PURE SHAPE
			blankscreen.present()
			exp_1.clock.wait(INTER_TRIAL_INTERVAL)
			trial.stimuli[0].present(update=True, clear=True)
			key, rt = exp_1.keyboard.wait(duration=MAX_RESPONSE_DELAY)
			if key == None:
				is_correct = None
			elif trial.get_factor('task') == "shape": #determine the task
				if  trial.get_factor('shape') == "square": #determine correct condition
					is_correct = (key == SQUARE_RESPONSE_KEY) #determine correct key
					correct_key = 'L'
					if trial.get_factor('number_of_circles') == 3: # determine corgruence condition
						is_congruent = 'C' #determine congruency
					elif trial.get_factor('number_of_circles') == 2: #alternative congruency condition
						is_congruent = 'I' #alternative congruency
				elif trial.get_factor('shape') == "diamond":
					is_correct = (key == DIAMOND_RESPONSE_KEY)
					correct_key = 'S'
					if trial.get_factor('number_of_circles') == 2:
						is_congruent = 'C'
					elif trial.get_factor('number_of_circles') == 3:
						is_congruent = 'I' 
			elif trial.get_factor('task') == "filling":
				if  trial.get_factor('number_of_circles') == 2:
					is_correct = (key == TWO_CIRCLES_RESPONSE_KEY)
					correct_key = 'S'
					if  trial.get_factor('shape') == "diamond":
						is_congruent = 'C'
					elif trial.get_factor('shape') == "square":
						is_congruent = 'I' 
				elif trial.get_factor('number_of_circles') == 3:
					is_correct = (key == THREE_CIRCLES_RESPONSE_KEY)
					correct_key = 'L'
					if  trial.get_factor('shape') == "square":
						is_congruent = 'C'
					elif trial.get_factor('shape') == "diamond":
						is_congruent = 'I' 
			if  is_correct == False:
				reminder_if_incorrect_response.present()
				exp_1.clock.wait(INSTRUCTION_REMINDER_AFTER_INCORRECT_RESPONSE)
				blankscreen.present()
				exp_1.clock.wait(PAUSE)
			exp_1.data.add([sex, i_trial,trial.get_factor('block') ,trial.get_factor('task'), trial.get_factor('shape'), trial.get_factor('number_of_circles'), is_congruent, correct_key, rt, is_correct])

def get_subject_sex():
	sex_question.present()
	key, rt = exp_1.keyboard.wait(keys = [MALE_SEX_KEY, FEMALE_SEX_KEY])
	if key == MALE_SEX_KEY:
		sex = 'Male'
	elif key == FEMALE_SEX_KEY:
		sex = 'Female'
	return(sex)

STIM_DIR = 'Stimuli/'

#I decided not to implement a loop for these three blocks, since I would need to use a dictionary to create variable names from strings. The popular opinion is that it is not advisable

pure_shape_block = design.Block()
for shape in ['diamond', 'square']:
	for number in [2, 3]:
		trial = design.Trial()
		trial.set_factor('block', 'pure_shape')
		trial.set_factor('task', 'shape')
		trial.set_factor('shape', shape)
		trial.set_factor('number_of_circles', number)
		pngname = os.path.join(STIM_DIR, 'shape_{}_{}_circles.png'.format(shape, number))
		trial.add_stimulus(stimuli.Picture(pngname))
		pure_shape_block.add_trial(trial)
pure_shape_block.shuffle_trials()

pure_filling_block = design.Block()
for shape in ['diamond', 'square']:
	for number in [2, 3]:
		trial = design.Trial()
		trial.set_factor('block', 'pure_filling')
		trial.set_factor('task', 'filling')
		trial.set_factor('shape', shape)
		trial.set_factor('number_of_circles', number)
		pngname = os.path.join(STIM_DIR, 'filling_{}_{}_circles.png'.format(shape, number))
		trial.add_stimulus(stimuli.Picture(pngname))
		pure_filling_block.add_trial(trial)
pure_filling_block.shuffle_trials()

mixed_block = design.Block()
for task in ['filling', 'shape']:
    for shape in ['diamond', 'square']:
        for number in [2, 3]:
            trial = design.Trial()
            trial.set_factor('block', 'mixed')
            trial.set_factor('task', task)
            trial.set_factor('shape', shape)
            trial.set_factor('number_of_circles', number)
            pngname = os.path.join(STIM_DIR, '{}_{}_{}_circles.png'.format(task, shape, number))
            trial.add_stimulus(stimuli.Picture(pngname))
            mixed_block.add_trial(trial)
mixed_block.shuffle_trials()

BLOCKS = [pure_shape_block, pure_filling_block, mixed_block]

blankscreen = stimuli.BlankScreen()
sex_question = stimuli.TextScreen("One last question...", heading_size = 40, text = "What is your biological sex? Press M for male and F for female.")
training_instructions = stimuli.TextScreen("Instructions:", heading_size = 40, text = TRAINING_INSTRUCTIONS)
reminder_if_incorrect_response =  stimuli.TextScreen("Your response was incorrect. Instructions reminder:", heading_size = 40, text =  REMINDER_INSTRUCTIONS)   
experiment_instructions =  stimuli.TextScreen("So, you're all set for the experiment! Instructions:", heading_size = 40, text =  EXPERIMENT_INSTRUCTIONS) 
exp_1.data_variable_names = ["Sex", "Trial Number", "Block", "Task Type", "Frame Shape", "Number of Circles","Congruent Trial", "Correct Key", "RT", "Correct Response"]

kb = io.Keyboard()

control.start(skip_ready_screen=True)

training(TRAINING_TRIALS)
experiment(BLOCKS, EXPERIMENT_TRIALS_PER_BLOCK)

current_dir = os.getcwd() + '/'
data_dir = "data"
misc.data_preprocessing.write_concatenated_data(os.path.join(current_dir, data_dir), file_name = 'experiment_1', output_file = 'experiment_1_data.csv' , delimiter=',', to_R_data_frame=False, names_comprise_glob_pattern=False)
