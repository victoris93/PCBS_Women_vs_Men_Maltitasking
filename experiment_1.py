import pandas as pd
import matplotlib.pyplot as plt
import glob
from expyriment import design, control, stimuli, misc, io

MALE_SEX_KEY = misc.constants.K_m
FEMALE_SEX_KEY =  misc.constants.K_f

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
    If the figure appears in the bottom part of the screen labeled "filling", you task is to report the number of circles inside of the frame. If you see 2 circles, press S on the keyboard. If you see 3 circles, press L. Let's start with a bit of training!
    
    Press the space bar to start.
    To exit the experiment, press escape."""
    
EXPERIMENT_INSTRUCTIONS = """Report the shape of the frame of the figure if it appears in the top part of the screen labeled "shape". If the frame is a square, press S on the keyboard. If it is a diamond, press L. Report the number of circles inside of the frame, if the figure appears in the bottom part of the screen labeled "filling". If you see 2 circles, press S. If you see 3 circles, press L. Every time give an incorrect response, you will get a reminder of the instructions.

    Press the space bar to start.
    To exit the experiment, press escape."""
    
REMINDER_INSTRUCTIONS = """Your task is to report the shape of the frame of the figure if it appears in the top part of the screen labeled "shape". If the frame is a square, press S on the keyboard. If it is a diamond, press L.
    If the figure appears in the bottom part of the screen labeled "filling", you task is to report the number of circles inside of the frame. If you see 2 circles, press S on the keyboard. If you see 3 circles, press L.
    
    To exit the experiment, press escape."""
    
exp_1 = design.Experiment(name="Task Switching", text_size= 40)
control.initialize(exp_1)

def training(N_TRIALS):
	training_instructions.present()
	kb.wait_char(' ')
	for i_trial in range(N_TRIALS):
		trial = stimuli_block.get_random_trial()
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
	experiment_instructions.present()
	kb.wait_char(' ')
	sex=get_subject_sex()
	for i_trial in range(N_TRIALS):
		trial = stimuli_block.get_random_trial()
		blankscreen.present()
		exp_1.clock.wait(INTER_TRIAL_INTERVAL)
		trial.stimuli[0].present(update=True, clear=True)
		key, rt = exp_1.keyboard.wait(duration=MAX_RESPONSE_DELAY)
		if key == None:
			is_correct = None
		elif trial.get_factor('task_type') == "shape_square":
			correct_key = 'S'
			is_correct = (key == SQUARE_RESPONSE_KEY)
		elif  trial.get_factor('task_type') == "shape_diamond":
			correct_key = 'L'
			is_correct = (key == DIAMOND_RESPONSE_KEY)
		elif trial.get_factor('task_type') == "filling_2_circles":
			correct_key = 'S'
			is_correct = (key == TWO_CIRCLES_RESPONSE_KEY)
		elif trial.get_factor('task_type') == "filling_3_circles":
			correct_key = 'L'
			is_correct = (key == THREE_CIRCLES_RESPONSE_KEY)
		if  is_correct == False:
			reminder_if_incorrect_response.present()
			exp_1.clock.wait(INSTRUCTION_REMINDER_AFTER_INCORRECT_RESPONSE)
			blankscreen.present()
			exp_1.clock.wait(PAUSE)
		exp_1.data.add([sex, i_trial, trial.get_factor('task_type'), correct_key, rt, is_correct])
	
def get_subject_sex():
	sex_question.present()
	key, rt = exp_1.keyboard.wait(keys = [MALE_SEX_KEY, FEMALE_SEX_KEY])
	if key == MALE_SEX_KEY:
		sex = 'Male'
	elif key == FEMALE_SEX_KEY:
		sex = 'Female'
	return(sex)

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


blankscreen = stimuli.BlankScreen()
sex_question = stimuli.TextScreen("One last question...", heading_size = 40, text = "What is your biological sex? Press M for male and F for female.")
training_instructions = stimuli.TextScreen("Instructions:", heading_size = 40, text = TRAINING_INSTRUCTIONS)
reminder_if_incorrect_response =  stimuli.TextScreen("Your response was incorrect. Instructions reminder:", heading_size = 40, text =  REMINDER_INSTRUCTIONS)   
experiment_instructions =  stimuli.TextScreen("So, you're all set for the experiment! Instructions:", heading_size = 40, text =  EXPERIMENT_INSTRUCTIONS) 
exp_1.data_variable_names = ["Sex", "Trial Number", "Task Type", "Correct Key", "RT", "Correct Response"]

kb = io.Keyboard()

control.start()

training(1)

experiment(5)

control.end()

misc.data_preprocessing.write_concatenated_data('/Users/VictoriaShevchenko/Documents/PCBS/PCBS_Project/PCBS_Women_vs_Men_Multitasking/data', file_name = 'experiment_1', output_file = 'experiment_1_data.csv' , delimiter=',', to_R_data_frame=False, names_comprise_glob_pattern=False)

