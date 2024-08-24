#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2023.2.2),
    on April 22, 2024, at 12:17
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# --- Setup global variables (available in all functions) ---
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# Store info about the experiment session
psychopyVersion = '2023.2.2'
expName = 'final_final_task'  # from the Builder filename that created this script
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date': data.getDateStr(),  # add a simple timestamp
    'expName': expName,
    'psychopyVersion': psychopyVersion,
}


def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # temporarily remove keys which the dialog doesn't need to show
    poppedKeys = {
        'date': expInfo.pop('date', data.getDateStr()),
        'expName': expInfo.pop('expName', expName),
        'psychopyVersion': expInfo.pop('psychopyVersion', psychopyVersion),
    }
    # show participant info dialog
    dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # restore hidden keys
    expInfo.update(poppedKeys)
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\fatma\\OneDrive\\Desktop\\IITK BOOKS\\Decision Making\\DM Project\\Task_psychoPy\\task_design4_\\final_final_task_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(logging.EXP)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=logging.EXP)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=(1024, 768), fullscr=True, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height'
        )
        if expInfo is not None:
            # store frame rate of monitor if we can measure it
            expInfo['frameRate'] = win.getActualFrameRate()
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    win.mouseVisible = False
    win.hideMessage()
    return win


def setupInputs(expInfo, thisExp, win):
    """
    Setup whatever inputs are available (mouse, keyboard, eyetracker, etc.)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    dict
        Dictionary of input devices by name.
    """
    # --- Setup input devices ---
    inputs = {}
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    eyetracker = None
    
    # create a default keyboard (e.g. to check for escape)
    defaultKeyboard = keyboard.Keyboard(backend='iohub')
    # return inputs dict
    return {
        'ioServer': ioServer,
        'defaultKeyboard': defaultKeyboard,
        'eyetracker': eyetracker,
    }

def pauseExperiment(thisExp, inputs=None, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # make sure we have a keyboard
        if inputs is None:
            inputs = {
                'defaultKeyboard': keyboard.Keyboard(backend='ioHub')
            }
        # check for quit (typically the Esc key)
        if inputs['defaultKeyboard'].getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win, inputs=inputs)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, inputs=inputs, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, inputs, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    inputs : dict
        Dictionary of input devices by name.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = inputs['ioServer']
    defaultKeyboard = inputs['defaultKeyboard']
    eyetracker = inputs['eyetracker']
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "instructions" ---
    text = visual.TextStim(win=win, name='text',
        text="Welcome to auditory task!!\n\nPress 'Y' to read the task instructions.\n\n",
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_2 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "trial_text" ---
    text_14 = visual.TextStim(win=win, name='text_14',
        text="HOW TO REPORT:\n\nThis is a continuous reporting task. Your job is to press a key whenever you see a 'GREEN BOX' appear on the screen. The box will last for 2 seconds. Pay attention to which ear you feel like you heard the sound coming from.\n\nRemember to press:\n\n'Left arrow key' for 'Left ear'\n'Right arrow key' for 'Right ear'\n'Spacebar' for 'Cannot predict'\n\nPress 'Y' to continue.",
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_18 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "start" ---
    text_15 = visual.TextStim(win=win, name='text_15',
        text="REMENBER:\n\nAlso after each trial you have to report how confident you were for you responses during the trials by clicking on the white line over the slider.\n\nPress 'Y' when you are ready to play the game.\n",
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_19 = keyboard.Keyboard()
    
    # --- Initialize components for Routine "catch1" ---
    sound_14 = sound.Sound('C:/Users/fatma/OneDrive/Desktop/IITK BOOKS/Decision Making/DM Project/Stimulus/task_sound_stimulus/catch_trail.ogg.opus', secs=-1, stereo=True, hamming=True,
        name='sound_14')
    sound_14.setVolume(1.0)
    key_resp_20 = keyboard.Keyboard()
    ct1_2 = visual.Rect(
        win=win, name='ct1_2',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-2.0, interpolate=True)
    ct2_2 = visual.Rect(
        win=win, name='ct2_2',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-3.0, interpolate=True)
    ct3_2 = visual.Rect(
        win=win, name='ct3_2',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-4.0, interpolate=True)
    ct4_2 = visual.Rect(
        win=win, name='ct4_2',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-5.0, interpolate=True)
    ct5_2 = visual.Rect(
        win=win, name='ct5_2',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-6.0, interpolate=True)
    
    # --- Initialize components for Routine "c1" ---
    slider_1 = visual.Slider(win=win, name='slider_1',
        startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=win.units,
        labels=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=1.0,
        style='slider', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=0, readOnly=False)
    text_4 = visual.TextStim(win=win, name='text_4',
        text="Report how confident you were about your responses throughtout the trial by clicking on the white line on the slider.\n\nWhere '1' is for 'least confident' and '10' is for 'most confident'.\n\n",
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "catch1" ---
    sound_14 = sound.Sound('C:/Users/fatma/OneDrive/Desktop/IITK BOOKS/Decision Making/DM Project/Stimulus/task_sound_stimulus/catch_trail.ogg.opus', secs=-1, stereo=True, hamming=True,
        name='sound_14')
    sound_14.setVolume(1.0)
    key_resp_20 = keyboard.Keyboard()
    ct1_2 = visual.Rect(
        win=win, name='ct1_2',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-2.0, interpolate=True)
    ct2_2 = visual.Rect(
        win=win, name='ct2_2',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-3.0, interpolate=True)
    ct3_2 = visual.Rect(
        win=win, name='ct3_2',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-4.0, interpolate=True)
    ct4_2 = visual.Rect(
        win=win, name='ct4_2',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-5.0, interpolate=True)
    ct5_2 = visual.Rect(
        win=win, name='ct5_2',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-6.0, interpolate=True)
    
    # --- Initialize components for Routine "c1" ---
    slider_1 = visual.Slider(win=win, name='slider_1',
        startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=win.units,
        labels=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=1.0,
        style='slider', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=0, readOnly=False)
    text_4 = visual.TextStim(win=win, name='text_4',
        text="Report how confident you were about your responses throughtout the trial by clicking on the white line on the slider.\n\nWhere '1' is for 'least confident' and '10' is for 'most confident'.\n\n",
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "trial1" ---
    sound_18 = sound.Sound('C:/Users/fatma/OneDrive/Desktop/IITK BOOKS/Decision Making/DM Project/Stimulus/task_sound_stimulus/t1.ogg.opus', secs=-1, stereo=True, hamming=True,
        name='sound_18')
    sound_18.setVolume(1.0)
    key_resp_43 = keyboard.Keyboard()
    target_11 = visual.Rect(
        win=win, name='target_11',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-2.0, interpolate=True)
    target2_11 = visual.Rect(
        win=win, name='target2_11',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-3.0, interpolate=True)
    target3_11 = visual.Rect(
        win=win, name='target3_11',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-4.0, interpolate=True)
    target4_11 = visual.Rect(
        win=win, name='target4_11',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-5.0, interpolate=True)
    target5_11 = visual.Rect(
        win=win, name='target5_11',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-6.0, interpolate=True)
    target6_11 = visual.Rect(
        win=win, name='target6_11',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-7.0, interpolate=True)
    target7_11 = visual.Rect(
        win=win, name='target7_11',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-8.0, interpolate=True)
    target8_11 = visual.Rect(
        win=win, name='target8_11',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-9.0, interpolate=True)
    target9_11 = visual.Rect(
        win=win, name='target9_11',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-10.0, interpolate=True)
    target10_11 = visual.Rect(
        win=win, name='target10_11',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-11.0, interpolate=True)
    target11_11 = visual.Rect(
        win=win, name='target11_11',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-12.0, interpolate=True)
    target12_11 = visual.Rect(
        win=win, name='target12_11',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-13.0, interpolate=True)
    target13_11 = visual.Rect(
        win=win, name='target13_11',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-14.0, interpolate=True)
    target14_11 = visual.Rect(
        win=win, name='target14_11',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-15.0, interpolate=True)
    target15_11 = visual.Rect(
        win=win, name='target15_11',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-16.0, interpolate=True)
    target16_11 = visual.Rect(
        win=win, name='target16_11',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-17.0, interpolate=True)
    target17_11 = visual.Rect(
        win=win, name='target17_11',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-18.0, interpolate=True)
    target18_11 = visual.Rect(
        win=win, name='target18_11',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-19.0, interpolate=True)
    target19_11 = visual.Rect(
        win=win, name='target19_11',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-20.0, interpolate=True)
    target20_11 = visual.Rect(
        win=win, name='target20_11',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-21.0, interpolate=True)
    
    # --- Initialize components for Routine "c1" ---
    slider_1 = visual.Slider(win=win, name='slider_1',
        startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=win.units,
        labels=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=1.0,
        style='slider', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=0, readOnly=False)
    text_4 = visual.TextStim(win=win, name='text_4',
        text="Report how confident you were about your responses throughtout the trial by clicking on the white line on the slider.\n\nWhere '1' is for 'least confident' and '10' is for 'most confident'.\n\n",
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "trial2" ---
    sound_19 = sound.Sound('C:/Users/fatma/OneDrive/Desktop/IITK BOOKS/Decision Making/DM Project/Stimulus/task_sound_stimulus/t2.ogg.opus', secs=-1, stereo=True, hamming=True,
        name='sound_19')
    sound_19.setVolume(1.0)
    key_resp = keyboard.Keyboard()
    target = visual.Rect(
        win=win, name='target',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-2.0, interpolate=True)
    target2 = visual.Rect(
        win=win, name='target2',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-3.0, interpolate=True)
    target3 = visual.Rect(
        win=win, name='target3',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-4.0, interpolate=True)
    target4 = visual.Rect(
        win=win, name='target4',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-5.0, interpolate=True)
    target5 = visual.Rect(
        win=win, name='target5',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-6.0, interpolate=True)
    target6 = visual.Rect(
        win=win, name='target6',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-7.0, interpolate=True)
    target7 = visual.Rect(
        win=win, name='target7',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-8.0, interpolate=True)
    target8 = visual.Rect(
        win=win, name='target8',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-9.0, interpolate=True)
    target9 = visual.Rect(
        win=win, name='target9',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-10.0, interpolate=True)
    target10 = visual.Rect(
        win=win, name='target10',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-11.0, interpolate=True)
    target11 = visual.Rect(
        win=win, name='target11',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-12.0, interpolate=True)
    target12 = visual.Rect(
        win=win, name='target12',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-13.0, interpolate=True)
    target13 = visual.Rect(
        win=win, name='target13',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-14.0, interpolate=True)
    target14 = visual.Rect(
        win=win, name='target14',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-15.0, interpolate=True)
    target15 = visual.Rect(
        win=win, name='target15',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-16.0, interpolate=True)
    target16 = visual.Rect(
        win=win, name='target16',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-17.0, interpolate=True)
    target17 = visual.Rect(
        win=win, name='target17',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-18.0, interpolate=True)
    target18 = visual.Rect(
        win=win, name='target18',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-19.0, interpolate=True)
    target19 = visual.Rect(
        win=win, name='target19',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-20.0, interpolate=True)
    target20 = visual.Rect(
        win=win, name='target20',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-21.0, interpolate=True)
    
    # --- Initialize components for Routine "c1" ---
    slider_1 = visual.Slider(win=win, name='slider_1',
        startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=win.units,
        labels=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=1.0,
        style='slider', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=0, readOnly=False)
    text_4 = visual.TextStim(win=win, name='text_4',
        text="Report how confident you were about your responses throughtout the trial by clicking on the white line on the slider.\n\nWhere '1' is for 'least confident' and '10' is for 'most confident'.\n\n",
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "trial3" ---
    sound_20 = sound.Sound('C:/Users/fatma/OneDrive/Desktop/IITK BOOKS/Decision Making/DM Project/Stimulus/task_sound_stimulus/t3.ogg.opus', secs=-1, stereo=True, hamming=True,
        name='sound_20')
    sound_20.setVolume(1.0)
    key_resp_44 = keyboard.Keyboard()
    target_12 = visual.Rect(
        win=win, name='target_12',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-2.0, interpolate=True)
    target2_12 = visual.Rect(
        win=win, name='target2_12',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-3.0, interpolate=True)
    target3_12 = visual.Rect(
        win=win, name='target3_12',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-4.0, interpolate=True)
    target4_12 = visual.Rect(
        win=win, name='target4_12',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-5.0, interpolate=True)
    target5_12 = visual.Rect(
        win=win, name='target5_12',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-6.0, interpolate=True)
    target6_12 = visual.Rect(
        win=win, name='target6_12',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-7.0, interpolate=True)
    target7_12 = visual.Rect(
        win=win, name='target7_12',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-8.0, interpolate=True)
    target8_12 = visual.Rect(
        win=win, name='target8_12',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-9.0, interpolate=True)
    target9_12 = visual.Rect(
        win=win, name='target9_12',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-10.0, interpolate=True)
    target10_12 = visual.Rect(
        win=win, name='target10_12',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-11.0, interpolate=True)
    target11_12 = visual.Rect(
        win=win, name='target11_12',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-12.0, interpolate=True)
    target12_12 = visual.Rect(
        win=win, name='target12_12',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-13.0, interpolate=True)
    target13_12 = visual.Rect(
        win=win, name='target13_12',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-14.0, interpolate=True)
    target14_12 = visual.Rect(
        win=win, name='target14_12',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-15.0, interpolate=True)
    target15_12 = visual.Rect(
        win=win, name='target15_12',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-16.0, interpolate=True)
    target16_12 = visual.Rect(
        win=win, name='target16_12',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-17.0, interpolate=True)
    target17_12 = visual.Rect(
        win=win, name='target17_12',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-18.0, interpolate=True)
    target18_12 = visual.Rect(
        win=win, name='target18_12',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-19.0, interpolate=True)
    target19_12 = visual.Rect(
        win=win, name='target19_12',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-20.0, interpolate=True)
    target20_12 = visual.Rect(
        win=win, name='target20_12',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-21.0, interpolate=True)
    
    # --- Initialize components for Routine "c1" ---
    slider_1 = visual.Slider(win=win, name='slider_1',
        startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=win.units,
        labels=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=1.0,
        style='slider', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=0, readOnly=False)
    text_4 = visual.TextStim(win=win, name='text_4',
        text="Report how confident you were about your responses throughtout the trial by clicking on the white line on the slider.\n\nWhere '1' is for 'least confident' and '10' is for 'most confident'.\n\n",
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "trial4" ---
    sound_21 = sound.Sound('C:/Users/fatma/OneDrive/Desktop/IITK BOOKS/Decision Making/DM Project/Stimulus/task_sound_stimulus/t4.ogg.opus', secs=-1, stereo=True, hamming=True,
        name='sound_21')
    sound_21.setVolume(1.0)
    key_resp_45 = keyboard.Keyboard()
    target_13 = visual.Rect(
        win=win, name='target_13',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-2.0, interpolate=True)
    target2_13 = visual.Rect(
        win=win, name='target2_13',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-3.0, interpolate=True)
    target3_13 = visual.Rect(
        win=win, name='target3_13',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-4.0, interpolate=True)
    target4_13 = visual.Rect(
        win=win, name='target4_13',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-5.0, interpolate=True)
    target5_13 = visual.Rect(
        win=win, name='target5_13',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-6.0, interpolate=True)
    target6_13 = visual.Rect(
        win=win, name='target6_13',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-7.0, interpolate=True)
    target7_13 = visual.Rect(
        win=win, name='target7_13',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-8.0, interpolate=True)
    target8_13 = visual.Rect(
        win=win, name='target8_13',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-9.0, interpolate=True)
    target9_13 = visual.Rect(
        win=win, name='target9_13',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-10.0, interpolate=True)
    target10_13 = visual.Rect(
        win=win, name='target10_13',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-11.0, interpolate=True)
    target11_13 = visual.Rect(
        win=win, name='target11_13',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-12.0, interpolate=True)
    target12_13 = visual.Rect(
        win=win, name='target12_13',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-13.0, interpolate=True)
    target13_13 = visual.Rect(
        win=win, name='target13_13',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-14.0, interpolate=True)
    target14_13 = visual.Rect(
        win=win, name='target14_13',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-15.0, interpolate=True)
    target15_13 = visual.Rect(
        win=win, name='target15_13',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-16.0, interpolate=True)
    target16_13 = visual.Rect(
        win=win, name='target16_13',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-17.0, interpolate=True)
    target17_13 = visual.Rect(
        win=win, name='target17_13',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-18.0, interpolate=True)
    target18_13 = visual.Rect(
        win=win, name='target18_13',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-19.0, interpolate=True)
    target19_13 = visual.Rect(
        win=win, name='target19_13',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-20.0, interpolate=True)
    target20_13 = visual.Rect(
        win=win, name='target20_13',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-21.0, interpolate=True)
    
    # --- Initialize components for Routine "c1" ---
    slider_1 = visual.Slider(win=win, name='slider_1',
        startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=win.units,
        labels=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=1.0,
        style='slider', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=0, readOnly=False)
    text_4 = visual.TextStim(win=win, name='text_4',
        text="Report how confident you were about your responses throughtout the trial by clicking on the white line on the slider.\n\nWhere '1' is for 'least confident' and '10' is for 'most confident'.\n\n",
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "trial5" ---
    sound_23 = sound.Sound('C:/Users/fatma/OneDrive/Desktop/IITK BOOKS/Decision Making/DM Project/Stimulus/task_sound_stimulus/t5.ogg.opus', secs=-1, stereo=True, hamming=True,
        name='sound_23')
    sound_23.setVolume(1.0)
    key_resp_47 = keyboard.Keyboard()
    target_15 = visual.Rect(
        win=win, name='target_15',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-2.0, interpolate=True)
    target2_15 = visual.Rect(
        win=win, name='target2_15',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-3.0, interpolate=True)
    target3_15 = visual.Rect(
        win=win, name='target3_15',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-4.0, interpolate=True)
    target4_15 = visual.Rect(
        win=win, name='target4_15',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-5.0, interpolate=True)
    target5_15 = visual.Rect(
        win=win, name='target5_15',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-6.0, interpolate=True)
    target6_15 = visual.Rect(
        win=win, name='target6_15',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-7.0, interpolate=True)
    target7_15 = visual.Rect(
        win=win, name='target7_15',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-8.0, interpolate=True)
    target8_15 = visual.Rect(
        win=win, name='target8_15',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-9.0, interpolate=True)
    target9_15 = visual.Rect(
        win=win, name='target9_15',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-10.0, interpolate=True)
    target10_15 = visual.Rect(
        win=win, name='target10_15',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-11.0, interpolate=True)
    target11_15 = visual.Rect(
        win=win, name='target11_15',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-12.0, interpolate=True)
    target12_15 = visual.Rect(
        win=win, name='target12_15',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-13.0, interpolate=True)
    target13_15 = visual.Rect(
        win=win, name='target13_15',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-14.0, interpolate=True)
    target14_15 = visual.Rect(
        win=win, name='target14_15',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-15.0, interpolate=True)
    target15_15 = visual.Rect(
        win=win, name='target15_15',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-16.0, interpolate=True)
    target16_15 = visual.Rect(
        win=win, name='target16_15',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-17.0, interpolate=True)
    target17_15 = visual.Rect(
        win=win, name='target17_15',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-18.0, interpolate=True)
    target18_15 = visual.Rect(
        win=win, name='target18_15',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-19.0, interpolate=True)
    target19_15 = visual.Rect(
        win=win, name='target19_15',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-20.0, interpolate=True)
    target20_15 = visual.Rect(
        win=win, name='target20_15',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-21.0, interpolate=True)
    
    # --- Initialize components for Routine "c1" ---
    slider_1 = visual.Slider(win=win, name='slider_1',
        startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=win.units,
        labels=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=1.0,
        style='slider', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=0, readOnly=False)
    text_4 = visual.TextStim(win=win, name='text_4',
        text="Report how confident you were about your responses throughtout the trial by clicking on the white line on the slider.\n\nWhere '1' is for 'least confident' and '10' is for 'most confident'.\n\n",
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "catch1" ---
    sound_14 = sound.Sound('C:/Users/fatma/OneDrive/Desktop/IITK BOOKS/Decision Making/DM Project/Stimulus/task_sound_stimulus/catch_trail.ogg.opus', secs=-1, stereo=True, hamming=True,
        name='sound_14')
    sound_14.setVolume(1.0)
    key_resp_20 = keyboard.Keyboard()
    ct1_2 = visual.Rect(
        win=win, name='ct1_2',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-2.0, interpolate=True)
    ct2_2 = visual.Rect(
        win=win, name='ct2_2',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-3.0, interpolate=True)
    ct3_2 = visual.Rect(
        win=win, name='ct3_2',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-4.0, interpolate=True)
    ct4_2 = visual.Rect(
        win=win, name='ct4_2',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-5.0, interpolate=True)
    ct5_2 = visual.Rect(
        win=win, name='ct5_2',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-6.0, interpolate=True)
    
    # --- Initialize components for Routine "c1" ---
    slider_1 = visual.Slider(win=win, name='slider_1',
        startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=win.units,
        labels=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=1.0,
        style='slider', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=0, readOnly=False)
    text_4 = visual.TextStim(win=win, name='text_4',
        text="Report how confident you were about your responses throughtout the trial by clicking on the white line on the slider.\n\nWhere '1' is for 'least confident' and '10' is for 'most confident'.\n\n",
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "trial6" ---
    sound_22 = sound.Sound('C:/Users/fatma/OneDrive/Desktop/IITK BOOKS/Decision Making/DM Project/Stimulus/task_sound_stimulus/t6.ogg.opus', secs=-1, stereo=True, hamming=True,
        name='sound_22')
    sound_22.setVolume(1.0)
    key_resp_46 = keyboard.Keyboard()
    target_14 = visual.Rect(
        win=win, name='target_14',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-2.0, interpolate=True)
    target2_14 = visual.Rect(
        win=win, name='target2_14',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-3.0, interpolate=True)
    target3_14 = visual.Rect(
        win=win, name='target3_14',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-4.0, interpolate=True)
    target4_14 = visual.Rect(
        win=win, name='target4_14',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-5.0, interpolate=True)
    target5_14 = visual.Rect(
        win=win, name='target5_14',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-6.0, interpolate=True)
    target6_14 = visual.Rect(
        win=win, name='target6_14',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-7.0, interpolate=True)
    target7_14 = visual.Rect(
        win=win, name='target7_14',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-8.0, interpolate=True)
    target8_14 = visual.Rect(
        win=win, name='target8_14',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-9.0, interpolate=True)
    target9_14 = visual.Rect(
        win=win, name='target9_14',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-10.0, interpolate=True)
    target10_14 = visual.Rect(
        win=win, name='target10_14',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-11.0, interpolate=True)
    target11_14 = visual.Rect(
        win=win, name='target11_14',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-12.0, interpolate=True)
    target12_14 = visual.Rect(
        win=win, name='target12_14',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-13.0, interpolate=True)
    target13_14 = visual.Rect(
        win=win, name='target13_14',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-14.0, interpolate=True)
    target14_14 = visual.Rect(
        win=win, name='target14_14',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-15.0, interpolate=True)
    target15_14 = visual.Rect(
        win=win, name='target15_14',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-16.0, interpolate=True)
    target16_14 = visual.Rect(
        win=win, name='target16_14',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-17.0, interpolate=True)
    target17_14 = visual.Rect(
        win=win, name='target17_14',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-18.0, interpolate=True)
    target18_14 = visual.Rect(
        win=win, name='target18_14',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-19.0, interpolate=True)
    target19_14 = visual.Rect(
        win=win, name='target19_14',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-20.0, interpolate=True)
    target20_14 = visual.Rect(
        win=win, name='target20_14',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-21.0, interpolate=True)
    
    # --- Initialize components for Routine "c1" ---
    slider_1 = visual.Slider(win=win, name='slider_1',
        startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=win.units,
        labels=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=1.0,
        style='slider', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=0, readOnly=False)
    text_4 = visual.TextStim(win=win, name='text_4',
        text="Report how confident you were about your responses throughtout the trial by clicking on the white line on the slider.\n\nWhere '1' is for 'least confident' and '10' is for 'most confident'.\n\n",
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "trial7" ---
    sound_24 = sound.Sound('C:/Users/fatma/OneDrive/Desktop/IITK BOOKS/Decision Making/DM Project/Stimulus/task_sound_stimulus/t7.ogg.opus', secs=-1, stereo=True, hamming=True,
        name='sound_24')
    sound_24.setVolume(1.0)
    key_resp_48 = keyboard.Keyboard()
    target_16 = visual.Rect(
        win=win, name='target_16',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-2.0, interpolate=True)
    target2_16 = visual.Rect(
        win=win, name='target2_16',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-3.0, interpolate=True)
    target3_16 = visual.Rect(
        win=win, name='target3_16',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-4.0, interpolate=True)
    target4_16 = visual.Rect(
        win=win, name='target4_16',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-5.0, interpolate=True)
    target5_16 = visual.Rect(
        win=win, name='target5_16',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-6.0, interpolate=True)
    target6_16 = visual.Rect(
        win=win, name='target6_16',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-7.0, interpolate=True)
    target7_16 = visual.Rect(
        win=win, name='target7_16',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-8.0, interpolate=True)
    target8_16 = visual.Rect(
        win=win, name='target8_16',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-9.0, interpolate=True)
    target9_16 = visual.Rect(
        win=win, name='target9_16',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-10.0, interpolate=True)
    target10_16 = visual.Rect(
        win=win, name='target10_16',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-11.0, interpolate=True)
    target11_16 = visual.Rect(
        win=win, name='target11_16',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-12.0, interpolate=True)
    target12_16 = visual.Rect(
        win=win, name='target12_16',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-13.0, interpolate=True)
    target13_16 = visual.Rect(
        win=win, name='target13_16',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-14.0, interpolate=True)
    target14_16 = visual.Rect(
        win=win, name='target14_16',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-15.0, interpolate=True)
    target15_16 = visual.Rect(
        win=win, name='target15_16',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-16.0, interpolate=True)
    target16_16 = visual.Rect(
        win=win, name='target16_16',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-17.0, interpolate=True)
    target17_16 = visual.Rect(
        win=win, name='target17_16',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-18.0, interpolate=True)
    target18_16 = visual.Rect(
        win=win, name='target18_16',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-19.0, interpolate=True)
    target19_16 = visual.Rect(
        win=win, name='target19_16',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-20.0, interpolate=True)
    target20_16 = visual.Rect(
        win=win, name='target20_16',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-21.0, interpolate=True)
    
    # --- Initialize components for Routine "c1" ---
    slider_1 = visual.Slider(win=win, name='slider_1',
        startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=win.units,
        labels=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=1.0,
        style='slider', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=0, readOnly=False)
    text_4 = visual.TextStim(win=win, name='text_4',
        text="Report how confident you were about your responses throughtout the trial by clicking on the white line on the slider.\n\nWhere '1' is for 'least confident' and '10' is for 'most confident'.\n\n",
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "trial8" ---
    sound_25 = sound.Sound('C:/Users/fatma/OneDrive/Desktop/IITK BOOKS/Decision Making/DM Project/Stimulus/task_sound_stimulus/t8.ogg.opus', secs=-1, stereo=True, hamming=True,
        name='sound_25')
    sound_25.setVolume(1.0)
    key_resp_49 = keyboard.Keyboard()
    target_17 = visual.Rect(
        win=win, name='target_17',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-2.0, interpolate=True)
    target2_17 = visual.Rect(
        win=win, name='target2_17',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-3.0, interpolate=True)
    target3_17 = visual.Rect(
        win=win, name='target3_17',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-4.0, interpolate=True)
    target4_17 = visual.Rect(
        win=win, name='target4_17',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-5.0, interpolate=True)
    target5_17 = visual.Rect(
        win=win, name='target5_17',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-6.0, interpolate=True)
    target6_17 = visual.Rect(
        win=win, name='target6_17',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-7.0, interpolate=True)
    target7_17 = visual.Rect(
        win=win, name='target7_17',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-8.0, interpolate=True)
    target8_17 = visual.Rect(
        win=win, name='target8_17',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-9.0, interpolate=True)
    target9_17 = visual.Rect(
        win=win, name='target9_17',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-10.0, interpolate=True)
    target10_17 = visual.Rect(
        win=win, name='target10_17',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-11.0, interpolate=True)
    target11_17 = visual.Rect(
        win=win, name='target11_17',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-12.0, interpolate=True)
    target12_17 = visual.Rect(
        win=win, name='target12_17',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-13.0, interpolate=True)
    target13_17 = visual.Rect(
        win=win, name='target13_17',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-14.0, interpolate=True)
    target14_17 = visual.Rect(
        win=win, name='target14_17',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-15.0, interpolate=True)
    target15_17 = visual.Rect(
        win=win, name='target15_17',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-16.0, interpolate=True)
    target16_17 = visual.Rect(
        win=win, name='target16_17',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-17.0, interpolate=True)
    target17_17 = visual.Rect(
        win=win, name='target17_17',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-18.0, interpolate=True)
    target18_17 = visual.Rect(
        win=win, name='target18_17',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-19.0, interpolate=True)
    target19_17 = visual.Rect(
        win=win, name='target19_17',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-20.0, interpolate=True)
    target20_17 = visual.Rect(
        win=win, name='target20_17',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-21.0, interpolate=True)
    
    # --- Initialize components for Routine "c1" ---
    slider_1 = visual.Slider(win=win, name='slider_1',
        startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=win.units,
        labels=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=1.0,
        style='slider', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=0, readOnly=False)
    text_4 = visual.TextStim(win=win, name='text_4',
        text="Report how confident you were about your responses throughtout the trial by clicking on the white line on the slider.\n\nWhere '1' is for 'least confident' and '10' is for 'most confident'.\n\n",
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "trial9" ---
    sound_26 = sound.Sound('C:/Users/fatma/OneDrive/Desktop/IITK BOOKS/Decision Making/DM Project/Stimulus/task_sound_stimulus/t9.ogg.opus', secs=-1, stereo=True, hamming=True,
        name='sound_26')
    sound_26.setVolume(1.0)
    key_resp_50 = keyboard.Keyboard()
    target_18 = visual.Rect(
        win=win, name='target_18',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-2.0, interpolate=True)
    target2_18 = visual.Rect(
        win=win, name='target2_18',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-3.0, interpolate=True)
    target3_18 = visual.Rect(
        win=win, name='target3_18',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-4.0, interpolate=True)
    target4_18 = visual.Rect(
        win=win, name='target4_18',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-5.0, interpolate=True)
    target5_18 = visual.Rect(
        win=win, name='target5_18',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-6.0, interpolate=True)
    target6_18 = visual.Rect(
        win=win, name='target6_18',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-7.0, interpolate=True)
    target7_18 = visual.Rect(
        win=win, name='target7_18',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-8.0, interpolate=True)
    target8_18 = visual.Rect(
        win=win, name='target8_18',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-9.0, interpolate=True)
    target9_18 = visual.Rect(
        win=win, name='target9_18',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-10.0, interpolate=True)
    target10_18 = visual.Rect(
        win=win, name='target10_18',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-11.0, interpolate=True)
    target11_18 = visual.Rect(
        win=win, name='target11_18',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-12.0, interpolate=True)
    target12_18 = visual.Rect(
        win=win, name='target12_18',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-13.0, interpolate=True)
    target13_18 = visual.Rect(
        win=win, name='target13_18',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-14.0, interpolate=True)
    target14_18 = visual.Rect(
        win=win, name='target14_18',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-15.0, interpolate=True)
    target15_18 = visual.Rect(
        win=win, name='target15_18',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-16.0, interpolate=True)
    target16_18 = visual.Rect(
        win=win, name='target16_18',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-17.0, interpolate=True)
    target17_18 = visual.Rect(
        win=win, name='target17_18',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-18.0, interpolate=True)
    target18_18 = visual.Rect(
        win=win, name='target18_18',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-19.0, interpolate=True)
    target19_18 = visual.Rect(
        win=win, name='target19_18',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-20.0, interpolate=True)
    target20_18 = visual.Rect(
        win=win, name='target20_18',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-21.0, interpolate=True)
    
    # --- Initialize components for Routine "c1" ---
    slider_1 = visual.Slider(win=win, name='slider_1',
        startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=win.units,
        labels=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=1.0,
        style='slider', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=0, readOnly=False)
    text_4 = visual.TextStim(win=win, name='text_4',
        text="Report how confident you were about your responses throughtout the trial by clicking on the white line on the slider.\n\nWhere '1' is for 'least confident' and '10' is for 'most confident'.\n\n",
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "trial10" ---
    sound_27 = sound.Sound('C:/Users/fatma/OneDrive/Desktop/IITK BOOKS/Decision Making/DM Project/Stimulus/task_sound_stimulus/t10.ogg.opus', secs=-1, stereo=True, hamming=True,
        name='sound_27')
    sound_27.setVolume(1.0)
    key_resp_51 = keyboard.Keyboard()
    target_19 = visual.Rect(
        win=win, name='target_19',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-2.0, interpolate=True)
    target2_19 = visual.Rect(
        win=win, name='target2_19',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-3.0, interpolate=True)
    target3_19 = visual.Rect(
        win=win, name='target3_19',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-4.0, interpolate=True)
    target4_19 = visual.Rect(
        win=win, name='target4_19',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-5.0, interpolate=True)
    target5_19 = visual.Rect(
        win=win, name='target5_19',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-6.0, interpolate=True)
    target6_19 = visual.Rect(
        win=win, name='target6_19',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-7.0, interpolate=True)
    target7_19 = visual.Rect(
        win=win, name='target7_19',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-8.0, interpolate=True)
    target8_19 = visual.Rect(
        win=win, name='target8_19',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-9.0, interpolate=True)
    target9_19 = visual.Rect(
        win=win, name='target9_19',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-10.0, interpolate=True)
    target10_19 = visual.Rect(
        win=win, name='target10_19',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-11.0, interpolate=True)
    target11_19 = visual.Rect(
        win=win, name='target11_19',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-12.0, interpolate=True)
    target12_19 = visual.Rect(
        win=win, name='target12_19',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-13.0, interpolate=True)
    target13_19 = visual.Rect(
        win=win, name='target13_19',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-14.0, interpolate=True)
    target14_19 = visual.Rect(
        win=win, name='target14_19',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-15.0, interpolate=True)
    target15_19 = visual.Rect(
        win=win, name='target15_19',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-16.0, interpolate=True)
    target16_19 = visual.Rect(
        win=win, name='target16_19',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-17.0, interpolate=True)
    target17_19 = visual.Rect(
        win=win, name='target17_19',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-18.0, interpolate=True)
    target18_19 = visual.Rect(
        win=win, name='target18_19',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-19.0, interpolate=True)
    target19_19 = visual.Rect(
        win=win, name='target19_19',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-20.0, interpolate=True)
    target20_19 = visual.Rect(
        win=win, name='target20_19',units='pix', 
        width=(100, 100)[0], height=(100, 100)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0.2706, 1.0000, -0.5451],
        opacity=None, depth=-21.0, interpolate=True)
    
    # --- Initialize components for Routine "c1" ---
    slider_1 = visual.Slider(win=win, name='slider_1',
        startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=win.units,
        labels=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=1.0,
        style='slider', styleTweaks=(), opacity=None,
        labelColor='LightGray', markerColor='Red', lineColor='White', colorSpace='rgb',
        font='Open Sans', labelHeight=0.05,
        flip=False, ori=0.0, depth=0, readOnly=False)
    text_4 = visual.TextStim(win=win, name='text_4',
        text="Report how confident you were about your responses throughtout the trial by clicking on the white line on the slider.\n\nWhere '1' is for 'least confident' and '10' is for 'most confident'.\n\n",
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "end" ---
    text_3 = visual.TextStim(win=win, name='text_3',
        text='Thank you\nGame end!',
        font='Open Sans',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_23 = keyboard.Keyboard()
    
    # create some handy timers
    if globalClock is None:
        globalClock = core.Clock()  # to track the time since experiment started
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6)
    
    # --- Prepare to start Routine "instructions" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instructions.started', globalClock.getTime())
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    instructionsComponents = [text, key_resp_2]
    for thisComponent in instructionsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "instructions" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 60.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text* updates
        
        # if text is starting this frame...
        if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text.frameNStart = frameN  # exact frame index
            text.tStart = t  # local t and not account for scr refresh
            text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text.started')
            # update status
            text.status = STARTED
            text.setAutoDraw(True)
        
        # if text is active this frame...
        if text.status == STARTED:
            # update params
            pass
        
        # if text is stopping this frame...
        if text.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 60-frameTolerance:
                # keep track of stop time/frame for later
                text.tStop = t  # not accounting for scr refresh
                text.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.stopped')
                # update status
                text.status = FINISHED
                text.setAutoDraw(False)
        
        # *key_resp_2* updates
        waitOnFlip = False
        
        # if key_resp_2 is starting this frame...
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        
        # if key_resp_2 is stopping this frame...
        if key_resp_2.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 60-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_2.tStop = t  # not accounting for scr refresh
                key_resp_2.frameNStop = frameN  # exact frame index
                # update status
                key_resp_2.status = FINISHED
                key_resp_2.status = FINISHED
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['y'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = [key.name for key in _key_resp_2_allKeys]  # storing all keys
                key_resp_2.rt = [key.rt for key in _key_resp_2_allKeys]
                key_resp_2.duration = [key.duration for key in _key_resp_2_allKeys]
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions" ---
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instructions.stopped', globalClock.getTime())
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys = None
    thisExp.addData('key_resp_2.keys',key_resp_2.keys)
    if key_resp_2.keys != None:  # we had a response
        thisExp.addData('key_resp_2.rt', key_resp_2.rt)
        thisExp.addData('key_resp_2.duration', key_resp_2.duration)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-60.000000)
    
    # --- Prepare to start Routine "trial_text" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('trial_text.started', globalClock.getTime())
    key_resp_18.keys = []
    key_resp_18.rt = []
    _key_resp_18_allKeys = []
    # keep track of which components have finished
    trial_textComponents = [text_14, key_resp_18]
    for thisComponent in trial_textComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial_text" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 60.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_14* updates
        
        # if text_14 is starting this frame...
        if text_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_14.frameNStart = frameN  # exact frame index
            text_14.tStart = t  # local t and not account for scr refresh
            text_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_14.status = STARTED
            text_14.setAutoDraw(True)
        
        # if text_14 is active this frame...
        if text_14.status == STARTED:
            # update params
            pass
        
        # if text_14 is stopping this frame...
        if text_14.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 60-frameTolerance:
                # keep track of stop time/frame for later
                text_14.tStop = t  # not accounting for scr refresh
                text_14.frameNStop = frameN  # exact frame index
                # update status
                text_14.status = FINISHED
                text_14.setAutoDraw(False)
        
        # *key_resp_18* updates
        waitOnFlip = False
        
        # if key_resp_18 is starting this frame...
        if key_resp_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_18.frameNStart = frameN  # exact frame index
            key_resp_18.tStart = t  # local t and not account for scr refresh
            key_resp_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_18, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_18.started')
            # update status
            key_resp_18.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_18.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_18.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if key_resp_18 is stopping this frame...
        if key_resp_18.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 60-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_18.tStop = t  # not accounting for scr refresh
                key_resp_18.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_18.stopped')
                # update status
                key_resp_18.status = FINISHED
                key_resp_18.status = FINISHED
        if key_resp_18.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_18.getKeys(keyList=['y'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_18_allKeys.extend(theseKeys)
            if len(_key_resp_18_allKeys):
                key_resp_18.keys = _key_resp_18_allKeys[-1].name  # just the last key pressed
                key_resp_18.rt = _key_resp_18_allKeys[-1].rt
                key_resp_18.duration = _key_resp_18_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial_textComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial_text" ---
    for thisComponent in trial_textComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('trial_text.stopped', globalClock.getTime())
    # check responses
    if key_resp_18.keys in ['', [], None]:  # No response was made
        key_resp_18.keys = None
    thisExp.addData('key_resp_18.keys',key_resp_18.keys)
    if key_resp_18.keys != None:  # we had a response
        thisExp.addData('key_resp_18.rt', key_resp_18.rt)
        thisExp.addData('key_resp_18.duration', key_resp_18.duration)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-60.000000)
    
    # --- Prepare to start Routine "start" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('start.started', globalClock.getTime())
    key_resp_19.keys = []
    key_resp_19.rt = []
    _key_resp_19_allKeys = []
    # keep track of which components have finished
    startComponents = [text_15, key_resp_19]
    for thisComponent in startComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "start" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 60.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_15* updates
        
        # if text_15 is starting this frame...
        if text_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_15.frameNStart = frameN  # exact frame index
            text_15.tStart = t  # local t and not account for scr refresh
            text_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_15.status = STARTED
            text_15.setAutoDraw(True)
        
        # if text_15 is active this frame...
        if text_15.status == STARTED:
            # update params
            pass
        
        # if text_15 is stopping this frame...
        if text_15.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 60-frameTolerance:
                # keep track of stop time/frame for later
                text_15.tStop = t  # not accounting for scr refresh
                text_15.frameNStop = frameN  # exact frame index
                # update status
                text_15.status = FINISHED
                text_15.setAutoDraw(False)
        
        # *key_resp_19* updates
        waitOnFlip = False
        
        # if key_resp_19 is starting this frame...
        if key_resp_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_19.frameNStart = frameN  # exact frame index
            key_resp_19.tStart = t  # local t and not account for scr refresh
            key_resp_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_19, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_19.started')
            # update status
            key_resp_19.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_19.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_19.clearEvents, eventType='keyboard')  # clear events on next screen flip
        
        # if key_resp_19 is stopping this frame...
        if key_resp_19.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 60-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_19.tStop = t  # not accounting for scr refresh
                key_resp_19.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_19.stopped')
                # update status
                key_resp_19.status = FINISHED
                key_resp_19.status = FINISHED
        if key_resp_19.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_19.getKeys(keyList=['y'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_19_allKeys.extend(theseKeys)
            if len(_key_resp_19_allKeys):
                key_resp_19.keys = _key_resp_19_allKeys[-1].name  # just the last key pressed
                key_resp_19.rt = _key_resp_19_allKeys[-1].rt
                key_resp_19.duration = _key_resp_19_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in startComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "start" ---
    for thisComponent in startComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('start.stopped', globalClock.getTime())
    # check responses
    if key_resp_19.keys in ['', [], None]:  # No response was made
        key_resp_19.keys = None
    thisExp.addData('key_resp_19.keys',key_resp_19.keys)
    if key_resp_19.keys != None:  # we had a response
        thisExp.addData('key_resp_19.rt', key_resp_19.rt)
        thisExp.addData('key_resp_19.duration', key_resp_19.duration)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-60.000000)
    
    # --- Prepare to start Routine "catch1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('catch1.started', globalClock.getTime())
    sound_14.setSound('C:/Users/fatma/OneDrive/Desktop/IITK BOOKS/Decision Making/DM Project/Stimulus/task_sound_stimulus/catch_trail.ogg.opus', secs=30, hamming=True)
    sound_14.setVolume(1.0, log=False)
    sound_14.seek(0)
    key_resp_20.keys = []
    key_resp_20.rt = []
    _key_resp_20_allKeys = []
    # keep track of which components have finished
    catch1Components = [sound_14, key_resp_20, ct1_2, ct2_2, ct3_2, ct4_2, ct5_2]
    for thisComponent in catch1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "catch1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 30.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 30-frameTolerance:
            continueRoutine = False
        
        # if sound_14 is starting this frame...
        if sound_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_14.frameNStart = frameN  # exact frame index
            sound_14.tStart = t  # local t and not account for scr refresh
            sound_14.tStartRefresh = tThisFlipGlobal  # on global time
            # update status
            sound_14.status = STARTED
            sound_14.play(when=win)  # sync with win flip
        
        # if sound_14 is stopping this frame...
        if sound_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_14.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                sound_14.tStop = t  # not accounting for scr refresh
                sound_14.frameNStop = frameN  # exact frame index
                # update status
                sound_14.status = FINISHED
                sound_14.stop()
        # update sound_14 status according to whether it's playing
        if sound_14.isPlaying:
            sound_14.status = STARTED
        elif sound_14.isFinished:
            sound_14.status = FINISHED
        
        # *key_resp_20* updates
        waitOnFlip = False
        
        # if key_resp_20 is starting this frame...
        if key_resp_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_20.frameNStart = frameN  # exact frame index
            key_resp_20.tStart = t  # local t and not account for scr refresh
            key_resp_20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_20, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_20.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_20.clock.reset)  # t=0 on next screen flip
        
        # if key_resp_20 is stopping this frame...
        if key_resp_20.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 30-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_20.tStop = t  # not accounting for scr refresh
                key_resp_20.frameNStop = frameN  # exact frame index
                # update status
                key_resp_20.status = FINISHED
                key_resp_20.status = FINISHED
        if key_resp_20.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_20.getKeys(keyList=['left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_20_allKeys.extend(theseKeys)
            if len(_key_resp_20_allKeys):
                key_resp_20.keys = [key.name for key in _key_resp_20_allKeys]  # storing all keys
                key_resp_20.rt = [key.rt for key in _key_resp_20_allKeys]
                key_resp_20.duration = [key.duration for key in _key_resp_20_allKeys]
        
        # *ct1_2* updates
        
        # if ct1_2 is starting this frame...
        if ct1_2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            ct1_2.frameNStart = frameN  # exact frame index
            ct1_2.tStart = t  # local t and not account for scr refresh
            ct1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ct1_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ct1_2.started')
            # update status
            ct1_2.status = STARTED
            ct1_2.setAutoDraw(True)
        
        # if ct1_2 is active this frame...
        if ct1_2.status == STARTED:
            # update params
            pass
        
        # if ct1_2 is stopping this frame...
        if ct1_2.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4-frameTolerance:
                # keep track of stop time/frame for later
                ct1_2.tStop = t  # not accounting for scr refresh
                ct1_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ct1_2.stopped')
                # update status
                ct1_2.status = FINISHED
                ct1_2.setAutoDraw(False)
        
        # *ct2_2* updates
        
        # if ct2_2 is starting this frame...
        if ct2_2.status == NOT_STARTED and tThisFlip >= 8-frameTolerance:
            # keep track of start time/frame for later
            ct2_2.frameNStart = frameN  # exact frame index
            ct2_2.tStart = t  # local t and not account for scr refresh
            ct2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ct2_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ct2_2.started')
            # update status
            ct2_2.status = STARTED
            ct2_2.setAutoDraw(True)
        
        # if ct2_2 is active this frame...
        if ct2_2.status == STARTED:
            # update params
            pass
        
        # if ct2_2 is stopping this frame...
        if ct2_2.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 10-frameTolerance:
                # keep track of stop time/frame for later
                ct2_2.tStop = t  # not accounting for scr refresh
                ct2_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ct2_2.stopped')
                # update status
                ct2_2.status = FINISHED
                ct2_2.setAutoDraw(False)
        
        # *ct3_2* updates
        
        # if ct3_2 is starting this frame...
        if ct3_2.status == NOT_STARTED and tThisFlip >= 14-frameTolerance:
            # keep track of start time/frame for later
            ct3_2.frameNStart = frameN  # exact frame index
            ct3_2.tStart = t  # local t and not account for scr refresh
            ct3_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ct3_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ct3_2.started')
            # update status
            ct3_2.status = STARTED
            ct3_2.setAutoDraw(True)
        
        # if ct3_2 is active this frame...
        if ct3_2.status == STARTED:
            # update params
            pass
        
        # if ct3_2 is stopping this frame...
        if ct3_2.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 16-frameTolerance:
                # keep track of stop time/frame for later
                ct3_2.tStop = t  # not accounting for scr refresh
                ct3_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ct3_2.stopped')
                # update status
                ct3_2.status = FINISHED
                ct3_2.setAutoDraw(False)
        
        # *ct4_2* updates
        
        # if ct4_2 is starting this frame...
        if ct4_2.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
            # keep track of start time/frame for later
            ct4_2.frameNStart = frameN  # exact frame index
            ct4_2.tStart = t  # local t and not account for scr refresh
            ct4_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ct4_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ct4_2.started')
            # update status
            ct4_2.status = STARTED
            ct4_2.setAutoDraw(True)
        
        # if ct4_2 is active this frame...
        if ct4_2.status == STARTED:
            # update params
            pass
        
        # if ct4_2 is stopping this frame...
        if ct4_2.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 22-frameTolerance:
                # keep track of stop time/frame for later
                ct4_2.tStop = t  # not accounting for scr refresh
                ct4_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ct4_2.stopped')
                # update status
                ct4_2.status = FINISHED
                ct4_2.setAutoDraw(False)
        
        # *ct5_2* updates
        
        # if ct5_2 is starting this frame...
        if ct5_2.status == NOT_STARTED and tThisFlip >= 26-frameTolerance:
            # keep track of start time/frame for later
            ct5_2.frameNStart = frameN  # exact frame index
            ct5_2.tStart = t  # local t and not account for scr refresh
            ct5_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ct5_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ct5_2.started')
            # update status
            ct5_2.status = STARTED
            ct5_2.setAutoDraw(True)
        
        # if ct5_2 is active this frame...
        if ct5_2.status == STARTED:
            # update params
            pass
        
        # if ct5_2 is stopping this frame...
        if ct5_2.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 28-frameTolerance:
                # keep track of stop time/frame for later
                ct5_2.tStop = t  # not accounting for scr refresh
                ct5_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ct5_2.stopped')
                # update status
                ct5_2.status = FINISHED
                ct5_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in catch1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "catch1" ---
    for thisComponent in catch1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('catch1.stopped', globalClock.getTime())
    sound_14.pause()  # ensure sound has stopped at end of Routine
    # check responses
    if key_resp_20.keys in ['', [], None]:  # No response was made
        key_resp_20.keys = None
    thisExp.addData('key_resp_20.keys',key_resp_20.keys)
    if key_resp_20.keys != None:  # we had a response
        thisExp.addData('key_resp_20.rt', key_resp_20.rt)
        thisExp.addData('key_resp_20.duration', key_resp_20.duration)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-30.000000)
    
    # --- Prepare to start Routine "c1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('c1.started', globalClock.getTime())
    slider_1.reset()
    # keep track of which components have finished
    c1Components = [slider_1, text_4]
    for thisComponent in c1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "c1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 15.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 15-frameTolerance:
            continueRoutine = False
        
        # *slider_1* updates
        
        # if slider_1 is starting this frame...
        if slider_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_1.frameNStart = frameN  # exact frame index
            slider_1.tStart = t  # local t and not account for scr refresh
            slider_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider_1.started')
            # update status
            slider_1.status = STARTED
            slider_1.setAutoDraw(True)
        
        # if slider_1 is active this frame...
        if slider_1.status == STARTED:
            # update params
            pass
        
        # if slider_1 is stopping this frame...
        if slider_1.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 15-frameTolerance:
                # keep track of stop time/frame for later
                slider_1.tStop = t  # not accounting for scr refresh
                slider_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_1.stopped')
                # update status
                slider_1.status = FINISHED
                slider_1.setAutoDraw(False)
        
        # *text_4* updates
        
        # if text_4 is starting this frame...
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_4.status = STARTED
            text_4.setAutoDraw(True)
        
        # if text_4 is active this frame...
        if text_4.status == STARTED:
            # update params
            pass
        
        # if text_4 is stopping this frame...
        if text_4.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 15-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                # update status
                text_4.status = FINISHED
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in c1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "c1" ---
    for thisComponent in c1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('c1.stopped', globalClock.getTime())
    thisExp.addData('slider_1.response', slider_1.getRating())
    thisExp.addData('slider_1.rt', slider_1.getRT())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-15.000000)
    
    # --- Prepare to start Routine "catch1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('catch1.started', globalClock.getTime())
    sound_14.setSound('C:/Users/fatma/OneDrive/Desktop/IITK BOOKS/Decision Making/DM Project/Stimulus/task_sound_stimulus/catch_trail.ogg.opus', secs=30, hamming=True)
    sound_14.setVolume(1.0, log=False)
    sound_14.seek(0)
    key_resp_20.keys = []
    key_resp_20.rt = []
    _key_resp_20_allKeys = []
    # keep track of which components have finished
    catch1Components = [sound_14, key_resp_20, ct1_2, ct2_2, ct3_2, ct4_2, ct5_2]
    for thisComponent in catch1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "catch1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 30.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 30-frameTolerance:
            continueRoutine = False
        
        # if sound_14 is starting this frame...
        if sound_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_14.frameNStart = frameN  # exact frame index
            sound_14.tStart = t  # local t and not account for scr refresh
            sound_14.tStartRefresh = tThisFlipGlobal  # on global time
            # update status
            sound_14.status = STARTED
            sound_14.play(when=win)  # sync with win flip
        
        # if sound_14 is stopping this frame...
        if sound_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_14.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                sound_14.tStop = t  # not accounting for scr refresh
                sound_14.frameNStop = frameN  # exact frame index
                # update status
                sound_14.status = FINISHED
                sound_14.stop()
        # update sound_14 status according to whether it's playing
        if sound_14.isPlaying:
            sound_14.status = STARTED
        elif sound_14.isFinished:
            sound_14.status = FINISHED
        
        # *key_resp_20* updates
        waitOnFlip = False
        
        # if key_resp_20 is starting this frame...
        if key_resp_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_20.frameNStart = frameN  # exact frame index
            key_resp_20.tStart = t  # local t and not account for scr refresh
            key_resp_20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_20, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_20.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_20.clock.reset)  # t=0 on next screen flip
        
        # if key_resp_20 is stopping this frame...
        if key_resp_20.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 30-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_20.tStop = t  # not accounting for scr refresh
                key_resp_20.frameNStop = frameN  # exact frame index
                # update status
                key_resp_20.status = FINISHED
                key_resp_20.status = FINISHED
        if key_resp_20.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_20.getKeys(keyList=['left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_20_allKeys.extend(theseKeys)
            if len(_key_resp_20_allKeys):
                key_resp_20.keys = [key.name for key in _key_resp_20_allKeys]  # storing all keys
                key_resp_20.rt = [key.rt for key in _key_resp_20_allKeys]
                key_resp_20.duration = [key.duration for key in _key_resp_20_allKeys]
        
        # *ct1_2* updates
        
        # if ct1_2 is starting this frame...
        if ct1_2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            ct1_2.frameNStart = frameN  # exact frame index
            ct1_2.tStart = t  # local t and not account for scr refresh
            ct1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ct1_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ct1_2.started')
            # update status
            ct1_2.status = STARTED
            ct1_2.setAutoDraw(True)
        
        # if ct1_2 is active this frame...
        if ct1_2.status == STARTED:
            # update params
            pass
        
        # if ct1_2 is stopping this frame...
        if ct1_2.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4-frameTolerance:
                # keep track of stop time/frame for later
                ct1_2.tStop = t  # not accounting for scr refresh
                ct1_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ct1_2.stopped')
                # update status
                ct1_2.status = FINISHED
                ct1_2.setAutoDraw(False)
        
        # *ct2_2* updates
        
        # if ct2_2 is starting this frame...
        if ct2_2.status == NOT_STARTED and tThisFlip >= 8-frameTolerance:
            # keep track of start time/frame for later
            ct2_2.frameNStart = frameN  # exact frame index
            ct2_2.tStart = t  # local t and not account for scr refresh
            ct2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ct2_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ct2_2.started')
            # update status
            ct2_2.status = STARTED
            ct2_2.setAutoDraw(True)
        
        # if ct2_2 is active this frame...
        if ct2_2.status == STARTED:
            # update params
            pass
        
        # if ct2_2 is stopping this frame...
        if ct2_2.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 10-frameTolerance:
                # keep track of stop time/frame for later
                ct2_2.tStop = t  # not accounting for scr refresh
                ct2_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ct2_2.stopped')
                # update status
                ct2_2.status = FINISHED
                ct2_2.setAutoDraw(False)
        
        # *ct3_2* updates
        
        # if ct3_2 is starting this frame...
        if ct3_2.status == NOT_STARTED and tThisFlip >= 14-frameTolerance:
            # keep track of start time/frame for later
            ct3_2.frameNStart = frameN  # exact frame index
            ct3_2.tStart = t  # local t and not account for scr refresh
            ct3_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ct3_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ct3_2.started')
            # update status
            ct3_2.status = STARTED
            ct3_2.setAutoDraw(True)
        
        # if ct3_2 is active this frame...
        if ct3_2.status == STARTED:
            # update params
            pass
        
        # if ct3_2 is stopping this frame...
        if ct3_2.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 16-frameTolerance:
                # keep track of stop time/frame for later
                ct3_2.tStop = t  # not accounting for scr refresh
                ct3_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ct3_2.stopped')
                # update status
                ct3_2.status = FINISHED
                ct3_2.setAutoDraw(False)
        
        # *ct4_2* updates
        
        # if ct4_2 is starting this frame...
        if ct4_2.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
            # keep track of start time/frame for later
            ct4_2.frameNStart = frameN  # exact frame index
            ct4_2.tStart = t  # local t and not account for scr refresh
            ct4_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ct4_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ct4_2.started')
            # update status
            ct4_2.status = STARTED
            ct4_2.setAutoDraw(True)
        
        # if ct4_2 is active this frame...
        if ct4_2.status == STARTED:
            # update params
            pass
        
        # if ct4_2 is stopping this frame...
        if ct4_2.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 22-frameTolerance:
                # keep track of stop time/frame for later
                ct4_2.tStop = t  # not accounting for scr refresh
                ct4_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ct4_2.stopped')
                # update status
                ct4_2.status = FINISHED
                ct4_2.setAutoDraw(False)
        
        # *ct5_2* updates
        
        # if ct5_2 is starting this frame...
        if ct5_2.status == NOT_STARTED and tThisFlip >= 26-frameTolerance:
            # keep track of start time/frame for later
            ct5_2.frameNStart = frameN  # exact frame index
            ct5_2.tStart = t  # local t and not account for scr refresh
            ct5_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ct5_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ct5_2.started')
            # update status
            ct5_2.status = STARTED
            ct5_2.setAutoDraw(True)
        
        # if ct5_2 is active this frame...
        if ct5_2.status == STARTED:
            # update params
            pass
        
        # if ct5_2 is stopping this frame...
        if ct5_2.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 28-frameTolerance:
                # keep track of stop time/frame for later
                ct5_2.tStop = t  # not accounting for scr refresh
                ct5_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ct5_2.stopped')
                # update status
                ct5_2.status = FINISHED
                ct5_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in catch1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "catch1" ---
    for thisComponent in catch1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('catch1.stopped', globalClock.getTime())
    sound_14.pause()  # ensure sound has stopped at end of Routine
    # check responses
    if key_resp_20.keys in ['', [], None]:  # No response was made
        key_resp_20.keys = None
    thisExp.addData('key_resp_20.keys',key_resp_20.keys)
    if key_resp_20.keys != None:  # we had a response
        thisExp.addData('key_resp_20.rt', key_resp_20.rt)
        thisExp.addData('key_resp_20.duration', key_resp_20.duration)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-30.000000)
    
    # --- Prepare to start Routine "c1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('c1.started', globalClock.getTime())
    slider_1.reset()
    # keep track of which components have finished
    c1Components = [slider_1, text_4]
    for thisComponent in c1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "c1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 15.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 15-frameTolerance:
            continueRoutine = False
        
        # *slider_1* updates
        
        # if slider_1 is starting this frame...
        if slider_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_1.frameNStart = frameN  # exact frame index
            slider_1.tStart = t  # local t and not account for scr refresh
            slider_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider_1.started')
            # update status
            slider_1.status = STARTED
            slider_1.setAutoDraw(True)
        
        # if slider_1 is active this frame...
        if slider_1.status == STARTED:
            # update params
            pass
        
        # if slider_1 is stopping this frame...
        if slider_1.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 15-frameTolerance:
                # keep track of stop time/frame for later
                slider_1.tStop = t  # not accounting for scr refresh
                slider_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_1.stopped')
                # update status
                slider_1.status = FINISHED
                slider_1.setAutoDraw(False)
        
        # *text_4* updates
        
        # if text_4 is starting this frame...
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_4.status = STARTED
            text_4.setAutoDraw(True)
        
        # if text_4 is active this frame...
        if text_4.status == STARTED:
            # update params
            pass
        
        # if text_4 is stopping this frame...
        if text_4.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 15-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                # update status
                text_4.status = FINISHED
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in c1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "c1" ---
    for thisComponent in c1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('c1.stopped', globalClock.getTime())
    thisExp.addData('slider_1.response', slider_1.getRating())
    thisExp.addData('slider_1.rt', slider_1.getRT())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-15.000000)
    
    # --- Prepare to start Routine "trial1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('trial1.started', globalClock.getTime())
    sound_18.setSound('C:/Users/fatma/OneDrive/Desktop/IITK BOOKS/Decision Making/DM Project/Stimulus/task_sound_stimulus/t1.ogg.opus', hamming=True)
    sound_18.setVolume(1.0, log=False)
    sound_18.seek(0)
    key_resp_43.keys = []
    key_resp_43.rt = []
    _key_resp_43_allKeys = []
    # keep track of which components have finished
    trial1Components = [sound_18, key_resp_43, target_11, target2_11, target3_11, target4_11, target5_11, target6_11, target7_11, target8_11, target9_11, target10_11, target11_11, target12_11, target13_11, target14_11, target15_11, target16_11, target17_11, target18_11, target19_11, target20_11]
    for thisComponent in trial1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 120-frameTolerance:
            continueRoutine = False
        
        # if sound_18 is starting this frame...
        if sound_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_18.frameNStart = frameN  # exact frame index
            sound_18.tStart = t  # local t and not account for scr refresh
            sound_18.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_18.started', tThisFlipGlobal)
            # update status
            sound_18.status = STARTED
            sound_18.play(when=win)  # sync with win flip
        # update sound_18 status according to whether it's playing
        if sound_18.isPlaying:
            sound_18.status = STARTED
        elif sound_18.isFinished:
            sound_18.status = FINISHED
        
        # *key_resp_43* updates
        waitOnFlip = False
        
        # if key_resp_43 is starting this frame...
        if key_resp_43.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_43.frameNStart = frameN  # exact frame index
            key_resp_43.tStart = t  # local t and not account for scr refresh
            key_resp_43.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_43, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_43.started')
            # update status
            key_resp_43.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_43.clock.reset)  # t=0 on next screen flip
        
        # if key_resp_43 is stopping this frame...
        if key_resp_43.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 120-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_43.tStop = t  # not accounting for scr refresh
                key_resp_43.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_43.stopped')
                # update status
                key_resp_43.status = FINISHED
                key_resp_43.status = FINISHED
        if key_resp_43.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_43.getKeys(keyList=['left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_43_allKeys.extend(theseKeys)
            if len(_key_resp_43_allKeys):
                key_resp_43.keys = [key.name for key in _key_resp_43_allKeys]  # storing all keys
                key_resp_43.rt = [key.rt for key in _key_resp_43_allKeys]
                key_resp_43.duration = [key.duration for key in _key_resp_43_allKeys]
        
        # *target_11* updates
        
        # if target_11 is starting this frame...
        if target_11.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            target_11.frameNStart = frameN  # exact frame index
            target_11.tStart = t  # local t and not account for scr refresh
            target_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target_11.started')
            # update status
            target_11.status = STARTED
            target_11.setAutoDraw(True)
        
        # if target_11 is active this frame...
        if target_11.status == STARTED:
            # update params
            pass
        
        # if target_11 is stopping this frame...
        if target_11.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4-frameTolerance:
                # keep track of stop time/frame for later
                target_11.tStop = t  # not accounting for scr refresh
                target_11.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target_11.stopped')
                # update status
                target_11.status = FINISHED
                target_11.setAutoDraw(False)
        
        # *target2_11* updates
        
        # if target2_11 is starting this frame...
        if target2_11.status == NOT_STARTED and tThisFlip >= 8-frameTolerance:
            # keep track of start time/frame for later
            target2_11.frameNStart = frameN  # exact frame index
            target2_11.tStart = t  # local t and not account for scr refresh
            target2_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target2_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target2_11.started')
            # update status
            target2_11.status = STARTED
            target2_11.setAutoDraw(True)
        
        # if target2_11 is active this frame...
        if target2_11.status == STARTED:
            # update params
            pass
        
        # if target2_11 is stopping this frame...
        if target2_11.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 10-frameTolerance:
                # keep track of stop time/frame for later
                target2_11.tStop = t  # not accounting for scr refresh
                target2_11.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target2_11.stopped')
                # update status
                target2_11.status = FINISHED
                target2_11.setAutoDraw(False)
        
        # *target3_11* updates
        
        # if target3_11 is starting this frame...
        if target3_11.status == NOT_STARTED and tThisFlip >= 14-frameTolerance:
            # keep track of start time/frame for later
            target3_11.frameNStart = frameN  # exact frame index
            target3_11.tStart = t  # local t and not account for scr refresh
            target3_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target3_11, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target3_11.started')
            # update status
            target3_11.status = STARTED
            target3_11.setAutoDraw(True)
        
        # if target3_11 is active this frame...
        if target3_11.status == STARTED:
            # update params
            pass
        
        # if target3_11 is stopping this frame...
        if target3_11.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 16-frameTolerance:
                # keep track of stop time/frame for later
                target3_11.tStop = t  # not accounting for scr refresh
                target3_11.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target3_11.stopped')
                # update status
                target3_11.status = FINISHED
                target3_11.setAutoDraw(False)
        
        # *target4_11* updates
        
        # if target4_11 is starting this frame...
        if target4_11.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
            # keep track of start time/frame for later
            target4_11.frameNStart = frameN  # exact frame index
            target4_11.tStart = t  # local t and not account for scr refresh
            target4_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target4_11, 'tStartRefresh')  # time at next scr refresh
            # update status
            target4_11.status = STARTED
            target4_11.setAutoDraw(True)
        
        # if target4_11 is active this frame...
        if target4_11.status == STARTED:
            # update params
            pass
        
        # if target4_11 is stopping this frame...
        if target4_11.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 22-frameTolerance:
                # keep track of stop time/frame for later
                target4_11.tStop = t  # not accounting for scr refresh
                target4_11.frameNStop = frameN  # exact frame index
                # update status
                target4_11.status = FINISHED
                target4_11.setAutoDraw(False)
        
        # *target5_11* updates
        
        # if target5_11 is starting this frame...
        if target5_11.status == NOT_STARTED and tThisFlip >= 26-frameTolerance:
            # keep track of start time/frame for later
            target5_11.frameNStart = frameN  # exact frame index
            target5_11.tStart = t  # local t and not account for scr refresh
            target5_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target5_11, 'tStartRefresh')  # time at next scr refresh
            # update status
            target5_11.status = STARTED
            target5_11.setAutoDraw(True)
        
        # if target5_11 is active this frame...
        if target5_11.status == STARTED:
            # update params
            pass
        
        # if target5_11 is stopping this frame...
        if target5_11.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 28-frameTolerance:
                # keep track of stop time/frame for later
                target5_11.tStop = t  # not accounting for scr refresh
                target5_11.frameNStop = frameN  # exact frame index
                # update status
                target5_11.status = FINISHED
                target5_11.setAutoDraw(False)
        
        # *target6_11* updates
        
        # if target6_11 is starting this frame...
        if target6_11.status == NOT_STARTED and tThisFlip >= 32-frameTolerance:
            # keep track of start time/frame for later
            target6_11.frameNStart = frameN  # exact frame index
            target6_11.tStart = t  # local t and not account for scr refresh
            target6_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target6_11, 'tStartRefresh')  # time at next scr refresh
            # update status
            target6_11.status = STARTED
            target6_11.setAutoDraw(True)
        
        # if target6_11 is active this frame...
        if target6_11.status == STARTED:
            # update params
            pass
        
        # if target6_11 is stopping this frame...
        if target6_11.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 34-frameTolerance:
                # keep track of stop time/frame for later
                target6_11.tStop = t  # not accounting for scr refresh
                target6_11.frameNStop = frameN  # exact frame index
                # update status
                target6_11.status = FINISHED
                target6_11.setAutoDraw(False)
        
        # *target7_11* updates
        
        # if target7_11 is starting this frame...
        if target7_11.status == NOT_STARTED and tThisFlip >= 38-frameTolerance:
            # keep track of start time/frame for later
            target7_11.frameNStart = frameN  # exact frame index
            target7_11.tStart = t  # local t and not account for scr refresh
            target7_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target7_11, 'tStartRefresh')  # time at next scr refresh
            # update status
            target7_11.status = STARTED
            target7_11.setAutoDraw(True)
        
        # if target7_11 is active this frame...
        if target7_11.status == STARTED:
            # update params
            pass
        
        # if target7_11 is stopping this frame...
        if target7_11.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 40-frameTolerance:
                # keep track of stop time/frame for later
                target7_11.tStop = t  # not accounting for scr refresh
                target7_11.frameNStop = frameN  # exact frame index
                # update status
                target7_11.status = FINISHED
                target7_11.setAutoDraw(False)
        
        # *target8_11* updates
        
        # if target8_11 is starting this frame...
        if target8_11.status == NOT_STARTED and tThisFlip >= 44-frameTolerance:
            # keep track of start time/frame for later
            target8_11.frameNStart = frameN  # exact frame index
            target8_11.tStart = t  # local t and not account for scr refresh
            target8_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target8_11, 'tStartRefresh')  # time at next scr refresh
            # update status
            target8_11.status = STARTED
            target8_11.setAutoDraw(True)
        
        # if target8_11 is active this frame...
        if target8_11.status == STARTED:
            # update params
            pass
        
        # if target8_11 is stopping this frame...
        if target8_11.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 46-frameTolerance:
                # keep track of stop time/frame for later
                target8_11.tStop = t  # not accounting for scr refresh
                target8_11.frameNStop = frameN  # exact frame index
                # update status
                target8_11.status = FINISHED
                target8_11.setAutoDraw(False)
        
        # *target9_11* updates
        
        # if target9_11 is starting this frame...
        if target9_11.status == NOT_STARTED and tThisFlip >= 50-frameTolerance:
            # keep track of start time/frame for later
            target9_11.frameNStart = frameN  # exact frame index
            target9_11.tStart = t  # local t and not account for scr refresh
            target9_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target9_11, 'tStartRefresh')  # time at next scr refresh
            # update status
            target9_11.status = STARTED
            target9_11.setAutoDraw(True)
        
        # if target9_11 is active this frame...
        if target9_11.status == STARTED:
            # update params
            pass
        
        # if target9_11 is stopping this frame...
        if target9_11.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 52-frameTolerance:
                # keep track of stop time/frame for later
                target9_11.tStop = t  # not accounting for scr refresh
                target9_11.frameNStop = frameN  # exact frame index
                # update status
                target9_11.status = FINISHED
                target9_11.setAutoDraw(False)
        
        # *target10_11* updates
        
        # if target10_11 is starting this frame...
        if target10_11.status == NOT_STARTED and tThisFlip >= 56-frameTolerance:
            # keep track of start time/frame for later
            target10_11.frameNStart = frameN  # exact frame index
            target10_11.tStart = t  # local t and not account for scr refresh
            target10_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target10_11, 'tStartRefresh')  # time at next scr refresh
            # update status
            target10_11.status = STARTED
            target10_11.setAutoDraw(True)
        
        # if target10_11 is active this frame...
        if target10_11.status == STARTED:
            # update params
            pass
        
        # if target10_11 is stopping this frame...
        if target10_11.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 58-frameTolerance:
                # keep track of stop time/frame for later
                target10_11.tStop = t  # not accounting for scr refresh
                target10_11.frameNStop = frameN  # exact frame index
                # update status
                target10_11.status = FINISHED
                target10_11.setAutoDraw(False)
        
        # *target11_11* updates
        
        # if target11_11 is starting this frame...
        if target11_11.status == NOT_STARTED and tThisFlip >= 62-frameTolerance:
            # keep track of start time/frame for later
            target11_11.frameNStart = frameN  # exact frame index
            target11_11.tStart = t  # local t and not account for scr refresh
            target11_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target11_11, 'tStartRefresh')  # time at next scr refresh
            # update status
            target11_11.status = STARTED
            target11_11.setAutoDraw(True)
        
        # if target11_11 is active this frame...
        if target11_11.status == STARTED:
            # update params
            pass
        
        # if target11_11 is stopping this frame...
        if target11_11.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 64-frameTolerance:
                # keep track of stop time/frame for later
                target11_11.tStop = t  # not accounting for scr refresh
                target11_11.frameNStop = frameN  # exact frame index
                # update status
                target11_11.status = FINISHED
                target11_11.setAutoDraw(False)
        
        # *target12_11* updates
        
        # if target12_11 is starting this frame...
        if target12_11.status == NOT_STARTED and tThisFlip >= 68-frameTolerance:
            # keep track of start time/frame for later
            target12_11.frameNStart = frameN  # exact frame index
            target12_11.tStart = t  # local t and not account for scr refresh
            target12_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target12_11, 'tStartRefresh')  # time at next scr refresh
            # update status
            target12_11.status = STARTED
            target12_11.setAutoDraw(True)
        
        # if target12_11 is active this frame...
        if target12_11.status == STARTED:
            # update params
            pass
        
        # if target12_11 is stopping this frame...
        if target12_11.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 70-frameTolerance:
                # keep track of stop time/frame for later
                target12_11.tStop = t  # not accounting for scr refresh
                target12_11.frameNStop = frameN  # exact frame index
                # update status
                target12_11.status = FINISHED
                target12_11.setAutoDraw(False)
        
        # *target13_11* updates
        
        # if target13_11 is starting this frame...
        if target13_11.status == NOT_STARTED and tThisFlip >= 74-frameTolerance:
            # keep track of start time/frame for later
            target13_11.frameNStart = frameN  # exact frame index
            target13_11.tStart = t  # local t and not account for scr refresh
            target13_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target13_11, 'tStartRefresh')  # time at next scr refresh
            # update status
            target13_11.status = STARTED
            target13_11.setAutoDraw(True)
        
        # if target13_11 is active this frame...
        if target13_11.status == STARTED:
            # update params
            pass
        
        # if target13_11 is stopping this frame...
        if target13_11.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 76-frameTolerance:
                # keep track of stop time/frame for later
                target13_11.tStop = t  # not accounting for scr refresh
                target13_11.frameNStop = frameN  # exact frame index
                # update status
                target13_11.status = FINISHED
                target13_11.setAutoDraw(False)
        
        # *target14_11* updates
        
        # if target14_11 is starting this frame...
        if target14_11.status == NOT_STARTED and tThisFlip >= 80-frameTolerance:
            # keep track of start time/frame for later
            target14_11.frameNStart = frameN  # exact frame index
            target14_11.tStart = t  # local t and not account for scr refresh
            target14_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target14_11, 'tStartRefresh')  # time at next scr refresh
            # update status
            target14_11.status = STARTED
            target14_11.setAutoDraw(True)
        
        # if target14_11 is active this frame...
        if target14_11.status == STARTED:
            # update params
            pass
        
        # if target14_11 is stopping this frame...
        if target14_11.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 82-frameTolerance:
                # keep track of stop time/frame for later
                target14_11.tStop = t  # not accounting for scr refresh
                target14_11.frameNStop = frameN  # exact frame index
                # update status
                target14_11.status = FINISHED
                target14_11.setAutoDraw(False)
        
        # *target15_11* updates
        
        # if target15_11 is starting this frame...
        if target15_11.status == NOT_STARTED and tThisFlip >= 86-frameTolerance:
            # keep track of start time/frame for later
            target15_11.frameNStart = frameN  # exact frame index
            target15_11.tStart = t  # local t and not account for scr refresh
            target15_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target15_11, 'tStartRefresh')  # time at next scr refresh
            # update status
            target15_11.status = STARTED
            target15_11.setAutoDraw(True)
        
        # if target15_11 is active this frame...
        if target15_11.status == STARTED:
            # update params
            pass
        
        # if target15_11 is stopping this frame...
        if target15_11.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 88-frameTolerance:
                # keep track of stop time/frame for later
                target15_11.tStop = t  # not accounting for scr refresh
                target15_11.frameNStop = frameN  # exact frame index
                # update status
                target15_11.status = FINISHED
                target15_11.setAutoDraw(False)
        
        # *target16_11* updates
        
        # if target16_11 is starting this frame...
        if target16_11.status == NOT_STARTED and tThisFlip >= 92-frameTolerance:
            # keep track of start time/frame for later
            target16_11.frameNStart = frameN  # exact frame index
            target16_11.tStart = t  # local t and not account for scr refresh
            target16_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target16_11, 'tStartRefresh')  # time at next scr refresh
            # update status
            target16_11.status = STARTED
            target16_11.setAutoDraw(True)
        
        # if target16_11 is active this frame...
        if target16_11.status == STARTED:
            # update params
            pass
        
        # if target16_11 is stopping this frame...
        if target16_11.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 94-frameTolerance:
                # keep track of stop time/frame for later
                target16_11.tStop = t  # not accounting for scr refresh
                target16_11.frameNStop = frameN  # exact frame index
                # update status
                target16_11.status = FINISHED
                target16_11.setAutoDraw(False)
        
        # *target17_11* updates
        
        # if target17_11 is starting this frame...
        if target17_11.status == NOT_STARTED and tThisFlip >= 98-frameTolerance:
            # keep track of start time/frame for later
            target17_11.frameNStart = frameN  # exact frame index
            target17_11.tStart = t  # local t and not account for scr refresh
            target17_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target17_11, 'tStartRefresh')  # time at next scr refresh
            # update status
            target17_11.status = STARTED
            target17_11.setAutoDraw(True)
        
        # if target17_11 is active this frame...
        if target17_11.status == STARTED:
            # update params
            pass
        
        # if target17_11 is stopping this frame...
        if target17_11.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 100-frameTolerance:
                # keep track of stop time/frame for later
                target17_11.tStop = t  # not accounting for scr refresh
                target17_11.frameNStop = frameN  # exact frame index
                # update status
                target17_11.status = FINISHED
                target17_11.setAutoDraw(False)
        
        # *target18_11* updates
        
        # if target18_11 is starting this frame...
        if target18_11.status == NOT_STARTED and tThisFlip >= 104-frameTolerance:
            # keep track of start time/frame for later
            target18_11.frameNStart = frameN  # exact frame index
            target18_11.tStart = t  # local t and not account for scr refresh
            target18_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target18_11, 'tStartRefresh')  # time at next scr refresh
            # update status
            target18_11.status = STARTED
            target18_11.setAutoDraw(True)
        
        # if target18_11 is active this frame...
        if target18_11.status == STARTED:
            # update params
            pass
        
        # if target18_11 is stopping this frame...
        if target18_11.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 106-frameTolerance:
                # keep track of stop time/frame for later
                target18_11.tStop = t  # not accounting for scr refresh
                target18_11.frameNStop = frameN  # exact frame index
                # update status
                target18_11.status = FINISHED
                target18_11.setAutoDraw(False)
        
        # *target19_11* updates
        
        # if target19_11 is starting this frame...
        if target19_11.status == NOT_STARTED and tThisFlip >= 110-frameTolerance:
            # keep track of start time/frame for later
            target19_11.frameNStart = frameN  # exact frame index
            target19_11.tStart = t  # local t and not account for scr refresh
            target19_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target19_11, 'tStartRefresh')  # time at next scr refresh
            # update status
            target19_11.status = STARTED
            target19_11.setAutoDraw(True)
        
        # if target19_11 is active this frame...
        if target19_11.status == STARTED:
            # update params
            pass
        
        # if target19_11 is stopping this frame...
        if target19_11.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 112-frameTolerance:
                # keep track of stop time/frame for later
                target19_11.tStop = t  # not accounting for scr refresh
                target19_11.frameNStop = frameN  # exact frame index
                # update status
                target19_11.status = FINISHED
                target19_11.setAutoDraw(False)
        
        # *target20_11* updates
        
        # if target20_11 is starting this frame...
        if target20_11.status == NOT_STARTED and tThisFlip >= 116-frameTolerance:
            # keep track of start time/frame for later
            target20_11.frameNStart = frameN  # exact frame index
            target20_11.tStart = t  # local t and not account for scr refresh
            target20_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target20_11, 'tStartRefresh')  # time at next scr refresh
            # update status
            target20_11.status = STARTED
            target20_11.setAutoDraw(True)
        
        # if target20_11 is active this frame...
        if target20_11.status == STARTED:
            # update params
            pass
        
        # if target20_11 is stopping this frame...
        if target20_11.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 118-frameTolerance:
                # keep track of stop time/frame for later
                target20_11.tStop = t  # not accounting for scr refresh
                target20_11.frameNStop = frameN  # exact frame index
                # update status
                target20_11.status = FINISHED
                target20_11.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial1" ---
    for thisComponent in trial1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('trial1.stopped', globalClock.getTime())
    sound_18.pause()  # ensure sound has stopped at end of Routine
    # check responses
    if key_resp_43.keys in ['', [], None]:  # No response was made
        key_resp_43.keys = None
    thisExp.addData('key_resp_43.keys',key_resp_43.keys)
    if key_resp_43.keys != None:  # we had a response
        thisExp.addData('key_resp_43.rt', key_resp_43.rt)
        thisExp.addData('key_resp_43.duration', key_resp_43.duration)
    thisExp.nextEntry()
    # the Routine "trial1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "c1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('c1.started', globalClock.getTime())
    slider_1.reset()
    # keep track of which components have finished
    c1Components = [slider_1, text_4]
    for thisComponent in c1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "c1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 15.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 15-frameTolerance:
            continueRoutine = False
        
        # *slider_1* updates
        
        # if slider_1 is starting this frame...
        if slider_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_1.frameNStart = frameN  # exact frame index
            slider_1.tStart = t  # local t and not account for scr refresh
            slider_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider_1.started')
            # update status
            slider_1.status = STARTED
            slider_1.setAutoDraw(True)
        
        # if slider_1 is active this frame...
        if slider_1.status == STARTED:
            # update params
            pass
        
        # if slider_1 is stopping this frame...
        if slider_1.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 15-frameTolerance:
                # keep track of stop time/frame for later
                slider_1.tStop = t  # not accounting for scr refresh
                slider_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_1.stopped')
                # update status
                slider_1.status = FINISHED
                slider_1.setAutoDraw(False)
        
        # *text_4* updates
        
        # if text_4 is starting this frame...
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_4.status = STARTED
            text_4.setAutoDraw(True)
        
        # if text_4 is active this frame...
        if text_4.status == STARTED:
            # update params
            pass
        
        # if text_4 is stopping this frame...
        if text_4.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 15-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                # update status
                text_4.status = FINISHED
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in c1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "c1" ---
    for thisComponent in c1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('c1.stopped', globalClock.getTime())
    thisExp.addData('slider_1.response', slider_1.getRating())
    thisExp.addData('slider_1.rt', slider_1.getRT())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-15.000000)
    
    # --- Prepare to start Routine "trial2" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('trial2.started', globalClock.getTime())
    sound_19.setSound('C:/Users/fatma/OneDrive/Desktop/IITK BOOKS/Decision Making/DM Project/Stimulus/task_sound_stimulus/t2.ogg.opus', hamming=True)
    sound_19.setVolume(1.0, log=False)
    sound_19.seek(0)
    key_resp.keys = []
    key_resp.rt = []
    _key_resp_allKeys = []
    # keep track of which components have finished
    trial2Components = [sound_19, key_resp, target, target2, target3, target4, target5, target6, target7, target8, target9, target10, target11, target12, target13, target14, target15, target16, target17, target18, target19, target20]
    for thisComponent in trial2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 120-frameTolerance:
            continueRoutine = False
        
        # if sound_19 is starting this frame...
        if sound_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_19.frameNStart = frameN  # exact frame index
            sound_19.tStart = t  # local t and not account for scr refresh
            sound_19.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_19.started', tThisFlipGlobal)
            # update status
            sound_19.status = STARTED
            sound_19.play(when=win)  # sync with win flip
        # update sound_19 status according to whether it's playing
        if sound_19.isPlaying:
            sound_19.status = STARTED
        elif sound_19.isFinished:
            sound_19.status = FINISHED
        
        # *key_resp* updates
        waitOnFlip = False
        
        # if key_resp is starting this frame...
        if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp.frameNStart = frameN  # exact frame index
            key_resp.tStart = t  # local t and not account for scr refresh
            key_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp.started')
            # update status
            key_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        
        # if key_resp is stopping this frame...
        if key_resp.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 120-frameTolerance:
                # keep track of stop time/frame for later
                key_resp.tStop = t  # not accounting for scr refresh
                key_resp.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.stopped')
                # update status
                key_resp.status = FINISHED
                key_resp.status = FINISHED
        if key_resp.status == STARTED and not waitOnFlip:
            theseKeys = key_resp.getKeys(keyList=['left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_allKeys.extend(theseKeys)
            if len(_key_resp_allKeys):
                key_resp.keys = [key.name for key in _key_resp_allKeys]  # storing all keys
                key_resp.rt = [key.rt for key in _key_resp_allKeys]
                key_resp.duration = [key.duration for key in _key_resp_allKeys]
        
        # *target* updates
        
        # if target is starting this frame...
        if target.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            target.frameNStart = frameN  # exact frame index
            target.tStart = t  # local t and not account for scr refresh
            target.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target.started')
            # update status
            target.status = STARTED
            target.setAutoDraw(True)
        
        # if target is active this frame...
        if target.status == STARTED:
            # update params
            pass
        
        # if target is stopping this frame...
        if target.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4-frameTolerance:
                # keep track of stop time/frame for later
                target.tStop = t  # not accounting for scr refresh
                target.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target.stopped')
                # update status
                target.status = FINISHED
                target.setAutoDraw(False)
        
        # *target2* updates
        
        # if target2 is starting this frame...
        if target2.status == NOT_STARTED and tThisFlip >= 8-frameTolerance:
            # keep track of start time/frame for later
            target2.frameNStart = frameN  # exact frame index
            target2.tStart = t  # local t and not account for scr refresh
            target2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target2.started')
            # update status
            target2.status = STARTED
            target2.setAutoDraw(True)
        
        # if target2 is active this frame...
        if target2.status == STARTED:
            # update params
            pass
        
        # if target2 is stopping this frame...
        if target2.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 10-frameTolerance:
                # keep track of stop time/frame for later
                target2.tStop = t  # not accounting for scr refresh
                target2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target2.stopped')
                # update status
                target2.status = FINISHED
                target2.setAutoDraw(False)
        
        # *target3* updates
        
        # if target3 is starting this frame...
        if target3.status == NOT_STARTED and tThisFlip >= 14-frameTolerance:
            # keep track of start time/frame for later
            target3.frameNStart = frameN  # exact frame index
            target3.tStart = t  # local t and not account for scr refresh
            target3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target3.started')
            # update status
            target3.status = STARTED
            target3.setAutoDraw(True)
        
        # if target3 is active this frame...
        if target3.status == STARTED:
            # update params
            pass
        
        # if target3 is stopping this frame...
        if target3.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 16-frameTolerance:
                # keep track of stop time/frame for later
                target3.tStop = t  # not accounting for scr refresh
                target3.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target3.stopped')
                # update status
                target3.status = FINISHED
                target3.setAutoDraw(False)
        
        # *target4* updates
        
        # if target4 is starting this frame...
        if target4.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
            # keep track of start time/frame for later
            target4.frameNStart = frameN  # exact frame index
            target4.tStart = t  # local t and not account for scr refresh
            target4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target4, 'tStartRefresh')  # time at next scr refresh
            # update status
            target4.status = STARTED
            target4.setAutoDraw(True)
        
        # if target4 is active this frame...
        if target4.status == STARTED:
            # update params
            pass
        
        # if target4 is stopping this frame...
        if target4.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 22-frameTolerance:
                # keep track of stop time/frame for later
                target4.tStop = t  # not accounting for scr refresh
                target4.frameNStop = frameN  # exact frame index
                # update status
                target4.status = FINISHED
                target4.setAutoDraw(False)
        
        # *target5* updates
        
        # if target5 is starting this frame...
        if target5.status == NOT_STARTED and tThisFlip >= 26-frameTolerance:
            # keep track of start time/frame for later
            target5.frameNStart = frameN  # exact frame index
            target5.tStart = t  # local t and not account for scr refresh
            target5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target5, 'tStartRefresh')  # time at next scr refresh
            # update status
            target5.status = STARTED
            target5.setAutoDraw(True)
        
        # if target5 is active this frame...
        if target5.status == STARTED:
            # update params
            pass
        
        # if target5 is stopping this frame...
        if target5.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 28-frameTolerance:
                # keep track of stop time/frame for later
                target5.tStop = t  # not accounting for scr refresh
                target5.frameNStop = frameN  # exact frame index
                # update status
                target5.status = FINISHED
                target5.setAutoDraw(False)
        
        # *target6* updates
        
        # if target6 is starting this frame...
        if target6.status == NOT_STARTED and tThisFlip >= 32-frameTolerance:
            # keep track of start time/frame for later
            target6.frameNStart = frameN  # exact frame index
            target6.tStart = t  # local t and not account for scr refresh
            target6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target6, 'tStartRefresh')  # time at next scr refresh
            # update status
            target6.status = STARTED
            target6.setAutoDraw(True)
        
        # if target6 is active this frame...
        if target6.status == STARTED:
            # update params
            pass
        
        # if target6 is stopping this frame...
        if target6.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 34-frameTolerance:
                # keep track of stop time/frame for later
                target6.tStop = t  # not accounting for scr refresh
                target6.frameNStop = frameN  # exact frame index
                # update status
                target6.status = FINISHED
                target6.setAutoDraw(False)
        
        # *target7* updates
        
        # if target7 is starting this frame...
        if target7.status == NOT_STARTED and tThisFlip >= 38-frameTolerance:
            # keep track of start time/frame for later
            target7.frameNStart = frameN  # exact frame index
            target7.tStart = t  # local t and not account for scr refresh
            target7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target7, 'tStartRefresh')  # time at next scr refresh
            # update status
            target7.status = STARTED
            target7.setAutoDraw(True)
        
        # if target7 is active this frame...
        if target7.status == STARTED:
            # update params
            pass
        
        # if target7 is stopping this frame...
        if target7.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 40-frameTolerance:
                # keep track of stop time/frame for later
                target7.tStop = t  # not accounting for scr refresh
                target7.frameNStop = frameN  # exact frame index
                # update status
                target7.status = FINISHED
                target7.setAutoDraw(False)
        
        # *target8* updates
        
        # if target8 is starting this frame...
        if target8.status == NOT_STARTED and tThisFlip >= 44-frameTolerance:
            # keep track of start time/frame for later
            target8.frameNStart = frameN  # exact frame index
            target8.tStart = t  # local t and not account for scr refresh
            target8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target8, 'tStartRefresh')  # time at next scr refresh
            # update status
            target8.status = STARTED
            target8.setAutoDraw(True)
        
        # if target8 is active this frame...
        if target8.status == STARTED:
            # update params
            pass
        
        # if target8 is stopping this frame...
        if target8.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 46-frameTolerance:
                # keep track of stop time/frame for later
                target8.tStop = t  # not accounting for scr refresh
                target8.frameNStop = frameN  # exact frame index
                # update status
                target8.status = FINISHED
                target8.setAutoDraw(False)
        
        # *target9* updates
        
        # if target9 is starting this frame...
        if target9.status == NOT_STARTED and tThisFlip >= 50-frameTolerance:
            # keep track of start time/frame for later
            target9.frameNStart = frameN  # exact frame index
            target9.tStart = t  # local t and not account for scr refresh
            target9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target9, 'tStartRefresh')  # time at next scr refresh
            # update status
            target9.status = STARTED
            target9.setAutoDraw(True)
        
        # if target9 is active this frame...
        if target9.status == STARTED:
            # update params
            pass
        
        # if target9 is stopping this frame...
        if target9.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 52-frameTolerance:
                # keep track of stop time/frame for later
                target9.tStop = t  # not accounting for scr refresh
                target9.frameNStop = frameN  # exact frame index
                # update status
                target9.status = FINISHED
                target9.setAutoDraw(False)
        
        # *target10* updates
        
        # if target10 is starting this frame...
        if target10.status == NOT_STARTED and tThisFlip >= 56-frameTolerance:
            # keep track of start time/frame for later
            target10.frameNStart = frameN  # exact frame index
            target10.tStart = t  # local t and not account for scr refresh
            target10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target10, 'tStartRefresh')  # time at next scr refresh
            # update status
            target10.status = STARTED
            target10.setAutoDraw(True)
        
        # if target10 is active this frame...
        if target10.status == STARTED:
            # update params
            pass
        
        # if target10 is stopping this frame...
        if target10.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 58-frameTolerance:
                # keep track of stop time/frame for later
                target10.tStop = t  # not accounting for scr refresh
                target10.frameNStop = frameN  # exact frame index
                # update status
                target10.status = FINISHED
                target10.setAutoDraw(False)
        
        # *target11* updates
        
        # if target11 is starting this frame...
        if target11.status == NOT_STARTED and tThisFlip >= 62-frameTolerance:
            # keep track of start time/frame for later
            target11.frameNStart = frameN  # exact frame index
            target11.tStart = t  # local t and not account for scr refresh
            target11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target11, 'tStartRefresh')  # time at next scr refresh
            # update status
            target11.status = STARTED
            target11.setAutoDraw(True)
        
        # if target11 is active this frame...
        if target11.status == STARTED:
            # update params
            pass
        
        # if target11 is stopping this frame...
        if target11.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 64-frameTolerance:
                # keep track of stop time/frame for later
                target11.tStop = t  # not accounting for scr refresh
                target11.frameNStop = frameN  # exact frame index
                # update status
                target11.status = FINISHED
                target11.setAutoDraw(False)
        
        # *target12* updates
        
        # if target12 is starting this frame...
        if target12.status == NOT_STARTED and tThisFlip >= 68-frameTolerance:
            # keep track of start time/frame for later
            target12.frameNStart = frameN  # exact frame index
            target12.tStart = t  # local t and not account for scr refresh
            target12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target12, 'tStartRefresh')  # time at next scr refresh
            # update status
            target12.status = STARTED
            target12.setAutoDraw(True)
        
        # if target12 is active this frame...
        if target12.status == STARTED:
            # update params
            pass
        
        # if target12 is stopping this frame...
        if target12.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 70-frameTolerance:
                # keep track of stop time/frame for later
                target12.tStop = t  # not accounting for scr refresh
                target12.frameNStop = frameN  # exact frame index
                # update status
                target12.status = FINISHED
                target12.setAutoDraw(False)
        
        # *target13* updates
        
        # if target13 is starting this frame...
        if target13.status == NOT_STARTED and tThisFlip >= 74-frameTolerance:
            # keep track of start time/frame for later
            target13.frameNStart = frameN  # exact frame index
            target13.tStart = t  # local t and not account for scr refresh
            target13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target13, 'tStartRefresh')  # time at next scr refresh
            # update status
            target13.status = STARTED
            target13.setAutoDraw(True)
        
        # if target13 is active this frame...
        if target13.status == STARTED:
            # update params
            pass
        
        # if target13 is stopping this frame...
        if target13.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 76-frameTolerance:
                # keep track of stop time/frame for later
                target13.tStop = t  # not accounting for scr refresh
                target13.frameNStop = frameN  # exact frame index
                # update status
                target13.status = FINISHED
                target13.setAutoDraw(False)
        
        # *target14* updates
        
        # if target14 is starting this frame...
        if target14.status == NOT_STARTED and tThisFlip >= 80-frameTolerance:
            # keep track of start time/frame for later
            target14.frameNStart = frameN  # exact frame index
            target14.tStart = t  # local t and not account for scr refresh
            target14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target14, 'tStartRefresh')  # time at next scr refresh
            # update status
            target14.status = STARTED
            target14.setAutoDraw(True)
        
        # if target14 is active this frame...
        if target14.status == STARTED:
            # update params
            pass
        
        # if target14 is stopping this frame...
        if target14.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 82-frameTolerance:
                # keep track of stop time/frame for later
                target14.tStop = t  # not accounting for scr refresh
                target14.frameNStop = frameN  # exact frame index
                # update status
                target14.status = FINISHED
                target14.setAutoDraw(False)
        
        # *target15* updates
        
        # if target15 is starting this frame...
        if target15.status == NOT_STARTED and tThisFlip >= 86-frameTolerance:
            # keep track of start time/frame for later
            target15.frameNStart = frameN  # exact frame index
            target15.tStart = t  # local t and not account for scr refresh
            target15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target15, 'tStartRefresh')  # time at next scr refresh
            # update status
            target15.status = STARTED
            target15.setAutoDraw(True)
        
        # if target15 is active this frame...
        if target15.status == STARTED:
            # update params
            pass
        
        # if target15 is stopping this frame...
        if target15.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 88-frameTolerance:
                # keep track of stop time/frame for later
                target15.tStop = t  # not accounting for scr refresh
                target15.frameNStop = frameN  # exact frame index
                # update status
                target15.status = FINISHED
                target15.setAutoDraw(False)
        
        # *target16* updates
        
        # if target16 is starting this frame...
        if target16.status == NOT_STARTED and tThisFlip >= 92-frameTolerance:
            # keep track of start time/frame for later
            target16.frameNStart = frameN  # exact frame index
            target16.tStart = t  # local t and not account for scr refresh
            target16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target16, 'tStartRefresh')  # time at next scr refresh
            # update status
            target16.status = STARTED
            target16.setAutoDraw(True)
        
        # if target16 is active this frame...
        if target16.status == STARTED:
            # update params
            pass
        
        # if target16 is stopping this frame...
        if target16.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 94-frameTolerance:
                # keep track of stop time/frame for later
                target16.tStop = t  # not accounting for scr refresh
                target16.frameNStop = frameN  # exact frame index
                # update status
                target16.status = FINISHED
                target16.setAutoDraw(False)
        
        # *target17* updates
        
        # if target17 is starting this frame...
        if target17.status == NOT_STARTED and tThisFlip >= 98-frameTolerance:
            # keep track of start time/frame for later
            target17.frameNStart = frameN  # exact frame index
            target17.tStart = t  # local t and not account for scr refresh
            target17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target17, 'tStartRefresh')  # time at next scr refresh
            # update status
            target17.status = STARTED
            target17.setAutoDraw(True)
        
        # if target17 is active this frame...
        if target17.status == STARTED:
            # update params
            pass
        
        # if target17 is stopping this frame...
        if target17.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 100-frameTolerance:
                # keep track of stop time/frame for later
                target17.tStop = t  # not accounting for scr refresh
                target17.frameNStop = frameN  # exact frame index
                # update status
                target17.status = FINISHED
                target17.setAutoDraw(False)
        
        # *target18* updates
        
        # if target18 is starting this frame...
        if target18.status == NOT_STARTED and tThisFlip >= 104-frameTolerance:
            # keep track of start time/frame for later
            target18.frameNStart = frameN  # exact frame index
            target18.tStart = t  # local t and not account for scr refresh
            target18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target18, 'tStartRefresh')  # time at next scr refresh
            # update status
            target18.status = STARTED
            target18.setAutoDraw(True)
        
        # if target18 is active this frame...
        if target18.status == STARTED:
            # update params
            pass
        
        # if target18 is stopping this frame...
        if target18.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 106-frameTolerance:
                # keep track of stop time/frame for later
                target18.tStop = t  # not accounting for scr refresh
                target18.frameNStop = frameN  # exact frame index
                # update status
                target18.status = FINISHED
                target18.setAutoDraw(False)
        
        # *target19* updates
        
        # if target19 is starting this frame...
        if target19.status == NOT_STARTED and tThisFlip >= 110-frameTolerance:
            # keep track of start time/frame for later
            target19.frameNStart = frameN  # exact frame index
            target19.tStart = t  # local t and not account for scr refresh
            target19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target19, 'tStartRefresh')  # time at next scr refresh
            # update status
            target19.status = STARTED
            target19.setAutoDraw(True)
        
        # if target19 is active this frame...
        if target19.status == STARTED:
            # update params
            pass
        
        # if target19 is stopping this frame...
        if target19.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 112-frameTolerance:
                # keep track of stop time/frame for later
                target19.tStop = t  # not accounting for scr refresh
                target19.frameNStop = frameN  # exact frame index
                # update status
                target19.status = FINISHED
                target19.setAutoDraw(False)
        
        # *target20* updates
        
        # if target20 is starting this frame...
        if target20.status == NOT_STARTED and tThisFlip >= 116-frameTolerance:
            # keep track of start time/frame for later
            target20.frameNStart = frameN  # exact frame index
            target20.tStart = t  # local t and not account for scr refresh
            target20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target20, 'tStartRefresh')  # time at next scr refresh
            # update status
            target20.status = STARTED
            target20.setAutoDraw(True)
        
        # if target20 is active this frame...
        if target20.status == STARTED:
            # update params
            pass
        
        # if target20 is stopping this frame...
        if target20.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 118-frameTolerance:
                # keep track of stop time/frame for later
                target20.tStop = t  # not accounting for scr refresh
                target20.frameNStop = frameN  # exact frame index
                # update status
                target20.status = FINISHED
                target20.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial2" ---
    for thisComponent in trial2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('trial2.stopped', globalClock.getTime())
    sound_19.pause()  # ensure sound has stopped at end of Routine
    # check responses
    if key_resp.keys in ['', [], None]:  # No response was made
        key_resp.keys = None
    thisExp.addData('key_resp.keys',key_resp.keys)
    if key_resp.keys != None:  # we had a response
        thisExp.addData('key_resp.rt', key_resp.rt)
        thisExp.addData('key_resp.duration', key_resp.duration)
    thisExp.nextEntry()
    # the Routine "trial2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "c1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('c1.started', globalClock.getTime())
    slider_1.reset()
    # keep track of which components have finished
    c1Components = [slider_1, text_4]
    for thisComponent in c1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "c1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 15.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 15-frameTolerance:
            continueRoutine = False
        
        # *slider_1* updates
        
        # if slider_1 is starting this frame...
        if slider_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_1.frameNStart = frameN  # exact frame index
            slider_1.tStart = t  # local t and not account for scr refresh
            slider_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider_1.started')
            # update status
            slider_1.status = STARTED
            slider_1.setAutoDraw(True)
        
        # if slider_1 is active this frame...
        if slider_1.status == STARTED:
            # update params
            pass
        
        # if slider_1 is stopping this frame...
        if slider_1.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 15-frameTolerance:
                # keep track of stop time/frame for later
                slider_1.tStop = t  # not accounting for scr refresh
                slider_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_1.stopped')
                # update status
                slider_1.status = FINISHED
                slider_1.setAutoDraw(False)
        
        # *text_4* updates
        
        # if text_4 is starting this frame...
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_4.status = STARTED
            text_4.setAutoDraw(True)
        
        # if text_4 is active this frame...
        if text_4.status == STARTED:
            # update params
            pass
        
        # if text_4 is stopping this frame...
        if text_4.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 15-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                # update status
                text_4.status = FINISHED
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in c1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "c1" ---
    for thisComponent in c1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('c1.stopped', globalClock.getTime())
    thisExp.addData('slider_1.response', slider_1.getRating())
    thisExp.addData('slider_1.rt', slider_1.getRT())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-15.000000)
    
    # --- Prepare to start Routine "trial3" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('trial3.started', globalClock.getTime())
    sound_20.setSound('C:/Users/fatma/OneDrive/Desktop/IITK BOOKS/Decision Making/DM Project/Stimulus/task_sound_stimulus/t3.ogg.opus', hamming=True)
    sound_20.setVolume(1.0, log=False)
    sound_20.seek(0)
    key_resp_44.keys = []
    key_resp_44.rt = []
    _key_resp_44_allKeys = []
    # keep track of which components have finished
    trial3Components = [sound_20, key_resp_44, target_12, target2_12, target3_12, target4_12, target5_12, target6_12, target7_12, target8_12, target9_12, target10_12, target11_12, target12_12, target13_12, target14_12, target15_12, target16_12, target17_12, target18_12, target19_12, target20_12]
    for thisComponent in trial3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial3" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 120-frameTolerance:
            continueRoutine = False
        
        # if sound_20 is starting this frame...
        if sound_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_20.frameNStart = frameN  # exact frame index
            sound_20.tStart = t  # local t and not account for scr refresh
            sound_20.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_20.started', tThisFlipGlobal)
            # update status
            sound_20.status = STARTED
            sound_20.play(when=win)  # sync with win flip
        # update sound_20 status according to whether it's playing
        if sound_20.isPlaying:
            sound_20.status = STARTED
        elif sound_20.isFinished:
            sound_20.status = FINISHED
        
        # *key_resp_44* updates
        waitOnFlip = False
        
        # if key_resp_44 is starting this frame...
        if key_resp_44.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_44.frameNStart = frameN  # exact frame index
            key_resp_44.tStart = t  # local t and not account for scr refresh
            key_resp_44.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_44, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_44.started')
            # update status
            key_resp_44.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_44.clock.reset)  # t=0 on next screen flip
        
        # if key_resp_44 is stopping this frame...
        if key_resp_44.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 120-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_44.tStop = t  # not accounting for scr refresh
                key_resp_44.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_44.stopped')
                # update status
                key_resp_44.status = FINISHED
                key_resp_44.status = FINISHED
        if key_resp_44.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_44.getKeys(keyList=['left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_44_allKeys.extend(theseKeys)
            if len(_key_resp_44_allKeys):
                key_resp_44.keys = [key.name for key in _key_resp_44_allKeys]  # storing all keys
                key_resp_44.rt = [key.rt for key in _key_resp_44_allKeys]
                key_resp_44.duration = [key.duration for key in _key_resp_44_allKeys]
        
        # *target_12* updates
        
        # if target_12 is starting this frame...
        if target_12.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            target_12.frameNStart = frameN  # exact frame index
            target_12.tStart = t  # local t and not account for scr refresh
            target_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target_12.started')
            # update status
            target_12.status = STARTED
            target_12.setAutoDraw(True)
        
        # if target_12 is active this frame...
        if target_12.status == STARTED:
            # update params
            pass
        
        # if target_12 is stopping this frame...
        if target_12.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4-frameTolerance:
                # keep track of stop time/frame for later
                target_12.tStop = t  # not accounting for scr refresh
                target_12.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target_12.stopped')
                # update status
                target_12.status = FINISHED
                target_12.setAutoDraw(False)
        
        # *target2_12* updates
        
        # if target2_12 is starting this frame...
        if target2_12.status == NOT_STARTED and tThisFlip >= 8-frameTolerance:
            # keep track of start time/frame for later
            target2_12.frameNStart = frameN  # exact frame index
            target2_12.tStart = t  # local t and not account for scr refresh
            target2_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target2_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target2_12.started')
            # update status
            target2_12.status = STARTED
            target2_12.setAutoDraw(True)
        
        # if target2_12 is active this frame...
        if target2_12.status == STARTED:
            # update params
            pass
        
        # if target2_12 is stopping this frame...
        if target2_12.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 10-frameTolerance:
                # keep track of stop time/frame for later
                target2_12.tStop = t  # not accounting for scr refresh
                target2_12.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target2_12.stopped')
                # update status
                target2_12.status = FINISHED
                target2_12.setAutoDraw(False)
        
        # *target3_12* updates
        
        # if target3_12 is starting this frame...
        if target3_12.status == NOT_STARTED and tThisFlip >= 14-frameTolerance:
            # keep track of start time/frame for later
            target3_12.frameNStart = frameN  # exact frame index
            target3_12.tStart = t  # local t and not account for scr refresh
            target3_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target3_12, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target3_12.started')
            # update status
            target3_12.status = STARTED
            target3_12.setAutoDraw(True)
        
        # if target3_12 is active this frame...
        if target3_12.status == STARTED:
            # update params
            pass
        
        # if target3_12 is stopping this frame...
        if target3_12.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 16-frameTolerance:
                # keep track of stop time/frame for later
                target3_12.tStop = t  # not accounting for scr refresh
                target3_12.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target3_12.stopped')
                # update status
                target3_12.status = FINISHED
                target3_12.setAutoDraw(False)
        
        # *target4_12* updates
        
        # if target4_12 is starting this frame...
        if target4_12.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
            # keep track of start time/frame for later
            target4_12.frameNStart = frameN  # exact frame index
            target4_12.tStart = t  # local t and not account for scr refresh
            target4_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target4_12, 'tStartRefresh')  # time at next scr refresh
            # update status
            target4_12.status = STARTED
            target4_12.setAutoDraw(True)
        
        # if target4_12 is active this frame...
        if target4_12.status == STARTED:
            # update params
            pass
        
        # if target4_12 is stopping this frame...
        if target4_12.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 22-frameTolerance:
                # keep track of stop time/frame for later
                target4_12.tStop = t  # not accounting for scr refresh
                target4_12.frameNStop = frameN  # exact frame index
                # update status
                target4_12.status = FINISHED
                target4_12.setAutoDraw(False)
        
        # *target5_12* updates
        
        # if target5_12 is starting this frame...
        if target5_12.status == NOT_STARTED and tThisFlip >= 26-frameTolerance:
            # keep track of start time/frame for later
            target5_12.frameNStart = frameN  # exact frame index
            target5_12.tStart = t  # local t and not account for scr refresh
            target5_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target5_12, 'tStartRefresh')  # time at next scr refresh
            # update status
            target5_12.status = STARTED
            target5_12.setAutoDraw(True)
        
        # if target5_12 is active this frame...
        if target5_12.status == STARTED:
            # update params
            pass
        
        # if target5_12 is stopping this frame...
        if target5_12.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 28-frameTolerance:
                # keep track of stop time/frame for later
                target5_12.tStop = t  # not accounting for scr refresh
                target5_12.frameNStop = frameN  # exact frame index
                # update status
                target5_12.status = FINISHED
                target5_12.setAutoDraw(False)
        
        # *target6_12* updates
        
        # if target6_12 is starting this frame...
        if target6_12.status == NOT_STARTED and tThisFlip >= 32-frameTolerance:
            # keep track of start time/frame for later
            target6_12.frameNStart = frameN  # exact frame index
            target6_12.tStart = t  # local t and not account for scr refresh
            target6_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target6_12, 'tStartRefresh')  # time at next scr refresh
            # update status
            target6_12.status = STARTED
            target6_12.setAutoDraw(True)
        
        # if target6_12 is active this frame...
        if target6_12.status == STARTED:
            # update params
            pass
        
        # if target6_12 is stopping this frame...
        if target6_12.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 34-frameTolerance:
                # keep track of stop time/frame for later
                target6_12.tStop = t  # not accounting for scr refresh
                target6_12.frameNStop = frameN  # exact frame index
                # update status
                target6_12.status = FINISHED
                target6_12.setAutoDraw(False)
        
        # *target7_12* updates
        
        # if target7_12 is starting this frame...
        if target7_12.status == NOT_STARTED and tThisFlip >= 38-frameTolerance:
            # keep track of start time/frame for later
            target7_12.frameNStart = frameN  # exact frame index
            target7_12.tStart = t  # local t and not account for scr refresh
            target7_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target7_12, 'tStartRefresh')  # time at next scr refresh
            # update status
            target7_12.status = STARTED
            target7_12.setAutoDraw(True)
        
        # if target7_12 is active this frame...
        if target7_12.status == STARTED:
            # update params
            pass
        
        # if target7_12 is stopping this frame...
        if target7_12.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 40-frameTolerance:
                # keep track of stop time/frame for later
                target7_12.tStop = t  # not accounting for scr refresh
                target7_12.frameNStop = frameN  # exact frame index
                # update status
                target7_12.status = FINISHED
                target7_12.setAutoDraw(False)
        
        # *target8_12* updates
        
        # if target8_12 is starting this frame...
        if target8_12.status == NOT_STARTED and tThisFlip >= 44-frameTolerance:
            # keep track of start time/frame for later
            target8_12.frameNStart = frameN  # exact frame index
            target8_12.tStart = t  # local t and not account for scr refresh
            target8_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target8_12, 'tStartRefresh')  # time at next scr refresh
            # update status
            target8_12.status = STARTED
            target8_12.setAutoDraw(True)
        
        # if target8_12 is active this frame...
        if target8_12.status == STARTED:
            # update params
            pass
        
        # if target8_12 is stopping this frame...
        if target8_12.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 46-frameTolerance:
                # keep track of stop time/frame for later
                target8_12.tStop = t  # not accounting for scr refresh
                target8_12.frameNStop = frameN  # exact frame index
                # update status
                target8_12.status = FINISHED
                target8_12.setAutoDraw(False)
        
        # *target9_12* updates
        
        # if target9_12 is starting this frame...
        if target9_12.status == NOT_STARTED and tThisFlip >= 50-frameTolerance:
            # keep track of start time/frame for later
            target9_12.frameNStart = frameN  # exact frame index
            target9_12.tStart = t  # local t and not account for scr refresh
            target9_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target9_12, 'tStartRefresh')  # time at next scr refresh
            # update status
            target9_12.status = STARTED
            target9_12.setAutoDraw(True)
        
        # if target9_12 is active this frame...
        if target9_12.status == STARTED:
            # update params
            pass
        
        # if target9_12 is stopping this frame...
        if target9_12.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 52-frameTolerance:
                # keep track of stop time/frame for later
                target9_12.tStop = t  # not accounting for scr refresh
                target9_12.frameNStop = frameN  # exact frame index
                # update status
                target9_12.status = FINISHED
                target9_12.setAutoDraw(False)
        
        # *target10_12* updates
        
        # if target10_12 is starting this frame...
        if target10_12.status == NOT_STARTED and tThisFlip >= 56-frameTolerance:
            # keep track of start time/frame for later
            target10_12.frameNStart = frameN  # exact frame index
            target10_12.tStart = t  # local t and not account for scr refresh
            target10_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target10_12, 'tStartRefresh')  # time at next scr refresh
            # update status
            target10_12.status = STARTED
            target10_12.setAutoDraw(True)
        
        # if target10_12 is active this frame...
        if target10_12.status == STARTED:
            # update params
            pass
        
        # if target10_12 is stopping this frame...
        if target10_12.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 58-frameTolerance:
                # keep track of stop time/frame for later
                target10_12.tStop = t  # not accounting for scr refresh
                target10_12.frameNStop = frameN  # exact frame index
                # update status
                target10_12.status = FINISHED
                target10_12.setAutoDraw(False)
        
        # *target11_12* updates
        
        # if target11_12 is starting this frame...
        if target11_12.status == NOT_STARTED and tThisFlip >= 62-frameTolerance:
            # keep track of start time/frame for later
            target11_12.frameNStart = frameN  # exact frame index
            target11_12.tStart = t  # local t and not account for scr refresh
            target11_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target11_12, 'tStartRefresh')  # time at next scr refresh
            # update status
            target11_12.status = STARTED
            target11_12.setAutoDraw(True)
        
        # if target11_12 is active this frame...
        if target11_12.status == STARTED:
            # update params
            pass
        
        # if target11_12 is stopping this frame...
        if target11_12.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 64-frameTolerance:
                # keep track of stop time/frame for later
                target11_12.tStop = t  # not accounting for scr refresh
                target11_12.frameNStop = frameN  # exact frame index
                # update status
                target11_12.status = FINISHED
                target11_12.setAutoDraw(False)
        
        # *target12_12* updates
        
        # if target12_12 is starting this frame...
        if target12_12.status == NOT_STARTED and tThisFlip >= 68-frameTolerance:
            # keep track of start time/frame for later
            target12_12.frameNStart = frameN  # exact frame index
            target12_12.tStart = t  # local t and not account for scr refresh
            target12_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target12_12, 'tStartRefresh')  # time at next scr refresh
            # update status
            target12_12.status = STARTED
            target12_12.setAutoDraw(True)
        
        # if target12_12 is active this frame...
        if target12_12.status == STARTED:
            # update params
            pass
        
        # if target12_12 is stopping this frame...
        if target12_12.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 70-frameTolerance:
                # keep track of stop time/frame for later
                target12_12.tStop = t  # not accounting for scr refresh
                target12_12.frameNStop = frameN  # exact frame index
                # update status
                target12_12.status = FINISHED
                target12_12.setAutoDraw(False)
        
        # *target13_12* updates
        
        # if target13_12 is starting this frame...
        if target13_12.status == NOT_STARTED and tThisFlip >= 74-frameTolerance:
            # keep track of start time/frame for later
            target13_12.frameNStart = frameN  # exact frame index
            target13_12.tStart = t  # local t and not account for scr refresh
            target13_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target13_12, 'tStartRefresh')  # time at next scr refresh
            # update status
            target13_12.status = STARTED
            target13_12.setAutoDraw(True)
        
        # if target13_12 is active this frame...
        if target13_12.status == STARTED:
            # update params
            pass
        
        # if target13_12 is stopping this frame...
        if target13_12.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 76-frameTolerance:
                # keep track of stop time/frame for later
                target13_12.tStop = t  # not accounting for scr refresh
                target13_12.frameNStop = frameN  # exact frame index
                # update status
                target13_12.status = FINISHED
                target13_12.setAutoDraw(False)
        
        # *target14_12* updates
        
        # if target14_12 is starting this frame...
        if target14_12.status == NOT_STARTED and tThisFlip >= 80-frameTolerance:
            # keep track of start time/frame for later
            target14_12.frameNStart = frameN  # exact frame index
            target14_12.tStart = t  # local t and not account for scr refresh
            target14_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target14_12, 'tStartRefresh')  # time at next scr refresh
            # update status
            target14_12.status = STARTED
            target14_12.setAutoDraw(True)
        
        # if target14_12 is active this frame...
        if target14_12.status == STARTED:
            # update params
            pass
        
        # if target14_12 is stopping this frame...
        if target14_12.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 82-frameTolerance:
                # keep track of stop time/frame for later
                target14_12.tStop = t  # not accounting for scr refresh
                target14_12.frameNStop = frameN  # exact frame index
                # update status
                target14_12.status = FINISHED
                target14_12.setAutoDraw(False)
        
        # *target15_12* updates
        
        # if target15_12 is starting this frame...
        if target15_12.status == NOT_STARTED and tThisFlip >= 86-frameTolerance:
            # keep track of start time/frame for later
            target15_12.frameNStart = frameN  # exact frame index
            target15_12.tStart = t  # local t and not account for scr refresh
            target15_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target15_12, 'tStartRefresh')  # time at next scr refresh
            # update status
            target15_12.status = STARTED
            target15_12.setAutoDraw(True)
        
        # if target15_12 is active this frame...
        if target15_12.status == STARTED:
            # update params
            pass
        
        # if target15_12 is stopping this frame...
        if target15_12.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 88-frameTolerance:
                # keep track of stop time/frame for later
                target15_12.tStop = t  # not accounting for scr refresh
                target15_12.frameNStop = frameN  # exact frame index
                # update status
                target15_12.status = FINISHED
                target15_12.setAutoDraw(False)
        
        # *target16_12* updates
        
        # if target16_12 is starting this frame...
        if target16_12.status == NOT_STARTED and tThisFlip >= 92-frameTolerance:
            # keep track of start time/frame for later
            target16_12.frameNStart = frameN  # exact frame index
            target16_12.tStart = t  # local t and not account for scr refresh
            target16_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target16_12, 'tStartRefresh')  # time at next scr refresh
            # update status
            target16_12.status = STARTED
            target16_12.setAutoDraw(True)
        
        # if target16_12 is active this frame...
        if target16_12.status == STARTED:
            # update params
            pass
        
        # if target16_12 is stopping this frame...
        if target16_12.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 94-frameTolerance:
                # keep track of stop time/frame for later
                target16_12.tStop = t  # not accounting for scr refresh
                target16_12.frameNStop = frameN  # exact frame index
                # update status
                target16_12.status = FINISHED
                target16_12.setAutoDraw(False)
        
        # *target17_12* updates
        
        # if target17_12 is starting this frame...
        if target17_12.status == NOT_STARTED and tThisFlip >= 98-frameTolerance:
            # keep track of start time/frame for later
            target17_12.frameNStart = frameN  # exact frame index
            target17_12.tStart = t  # local t and not account for scr refresh
            target17_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target17_12, 'tStartRefresh')  # time at next scr refresh
            # update status
            target17_12.status = STARTED
            target17_12.setAutoDraw(True)
        
        # if target17_12 is active this frame...
        if target17_12.status == STARTED:
            # update params
            pass
        
        # if target17_12 is stopping this frame...
        if target17_12.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 100-frameTolerance:
                # keep track of stop time/frame for later
                target17_12.tStop = t  # not accounting for scr refresh
                target17_12.frameNStop = frameN  # exact frame index
                # update status
                target17_12.status = FINISHED
                target17_12.setAutoDraw(False)
        
        # *target18_12* updates
        
        # if target18_12 is starting this frame...
        if target18_12.status == NOT_STARTED and tThisFlip >= 104-frameTolerance:
            # keep track of start time/frame for later
            target18_12.frameNStart = frameN  # exact frame index
            target18_12.tStart = t  # local t and not account for scr refresh
            target18_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target18_12, 'tStartRefresh')  # time at next scr refresh
            # update status
            target18_12.status = STARTED
            target18_12.setAutoDraw(True)
        
        # if target18_12 is active this frame...
        if target18_12.status == STARTED:
            # update params
            pass
        
        # if target18_12 is stopping this frame...
        if target18_12.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 106-frameTolerance:
                # keep track of stop time/frame for later
                target18_12.tStop = t  # not accounting for scr refresh
                target18_12.frameNStop = frameN  # exact frame index
                # update status
                target18_12.status = FINISHED
                target18_12.setAutoDraw(False)
        
        # *target19_12* updates
        
        # if target19_12 is starting this frame...
        if target19_12.status == NOT_STARTED and tThisFlip >= 110-frameTolerance:
            # keep track of start time/frame for later
            target19_12.frameNStart = frameN  # exact frame index
            target19_12.tStart = t  # local t and not account for scr refresh
            target19_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target19_12, 'tStartRefresh')  # time at next scr refresh
            # update status
            target19_12.status = STARTED
            target19_12.setAutoDraw(True)
        
        # if target19_12 is active this frame...
        if target19_12.status == STARTED:
            # update params
            pass
        
        # if target19_12 is stopping this frame...
        if target19_12.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 112-frameTolerance:
                # keep track of stop time/frame for later
                target19_12.tStop = t  # not accounting for scr refresh
                target19_12.frameNStop = frameN  # exact frame index
                # update status
                target19_12.status = FINISHED
                target19_12.setAutoDraw(False)
        
        # *target20_12* updates
        
        # if target20_12 is starting this frame...
        if target20_12.status == NOT_STARTED and tThisFlip >= 116-frameTolerance:
            # keep track of start time/frame for later
            target20_12.frameNStart = frameN  # exact frame index
            target20_12.tStart = t  # local t and not account for scr refresh
            target20_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target20_12, 'tStartRefresh')  # time at next scr refresh
            # update status
            target20_12.status = STARTED
            target20_12.setAutoDraw(True)
        
        # if target20_12 is active this frame...
        if target20_12.status == STARTED:
            # update params
            pass
        
        # if target20_12 is stopping this frame...
        if target20_12.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 118-frameTolerance:
                # keep track of stop time/frame for later
                target20_12.tStop = t  # not accounting for scr refresh
                target20_12.frameNStop = frameN  # exact frame index
                # update status
                target20_12.status = FINISHED
                target20_12.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial3" ---
    for thisComponent in trial3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('trial3.stopped', globalClock.getTime())
    sound_20.pause()  # ensure sound has stopped at end of Routine
    # check responses
    if key_resp_44.keys in ['', [], None]:  # No response was made
        key_resp_44.keys = None
    thisExp.addData('key_resp_44.keys',key_resp_44.keys)
    if key_resp_44.keys != None:  # we had a response
        thisExp.addData('key_resp_44.rt', key_resp_44.rt)
        thisExp.addData('key_resp_44.duration', key_resp_44.duration)
    thisExp.nextEntry()
    # the Routine "trial3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "c1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('c1.started', globalClock.getTime())
    slider_1.reset()
    # keep track of which components have finished
    c1Components = [slider_1, text_4]
    for thisComponent in c1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "c1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 15.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 15-frameTolerance:
            continueRoutine = False
        
        # *slider_1* updates
        
        # if slider_1 is starting this frame...
        if slider_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_1.frameNStart = frameN  # exact frame index
            slider_1.tStart = t  # local t and not account for scr refresh
            slider_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider_1.started')
            # update status
            slider_1.status = STARTED
            slider_1.setAutoDraw(True)
        
        # if slider_1 is active this frame...
        if slider_1.status == STARTED:
            # update params
            pass
        
        # if slider_1 is stopping this frame...
        if slider_1.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 15-frameTolerance:
                # keep track of stop time/frame for later
                slider_1.tStop = t  # not accounting for scr refresh
                slider_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_1.stopped')
                # update status
                slider_1.status = FINISHED
                slider_1.setAutoDraw(False)
        
        # *text_4* updates
        
        # if text_4 is starting this frame...
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_4.status = STARTED
            text_4.setAutoDraw(True)
        
        # if text_4 is active this frame...
        if text_4.status == STARTED:
            # update params
            pass
        
        # if text_4 is stopping this frame...
        if text_4.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 15-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                # update status
                text_4.status = FINISHED
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in c1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "c1" ---
    for thisComponent in c1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('c1.stopped', globalClock.getTime())
    thisExp.addData('slider_1.response', slider_1.getRating())
    thisExp.addData('slider_1.rt', slider_1.getRT())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-15.000000)
    
    # --- Prepare to start Routine "trial4" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('trial4.started', globalClock.getTime())
    sound_21.setSound('C:/Users/fatma/OneDrive/Desktop/IITK BOOKS/Decision Making/DM Project/Stimulus/task_sound_stimulus/t4.ogg.opus', hamming=True)
    sound_21.setVolume(1.0, log=False)
    sound_21.seek(0)
    key_resp_45.keys = []
    key_resp_45.rt = []
    _key_resp_45_allKeys = []
    # keep track of which components have finished
    trial4Components = [sound_21, key_resp_45, target_13, target2_13, target3_13, target4_13, target5_13, target6_13, target7_13, target8_13, target9_13, target10_13, target11_13, target12_13, target13_13, target14_13, target15_13, target16_13, target17_13, target18_13, target19_13, target20_13]
    for thisComponent in trial4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial4" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 120-frameTolerance:
            continueRoutine = False
        
        # if sound_21 is starting this frame...
        if sound_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_21.frameNStart = frameN  # exact frame index
            sound_21.tStart = t  # local t and not account for scr refresh
            sound_21.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_21.started', tThisFlipGlobal)
            # update status
            sound_21.status = STARTED
            sound_21.play(when=win)  # sync with win flip
        # update sound_21 status according to whether it's playing
        if sound_21.isPlaying:
            sound_21.status = STARTED
        elif sound_21.isFinished:
            sound_21.status = FINISHED
        
        # *key_resp_45* updates
        waitOnFlip = False
        
        # if key_resp_45 is starting this frame...
        if key_resp_45.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_45.frameNStart = frameN  # exact frame index
            key_resp_45.tStart = t  # local t and not account for scr refresh
            key_resp_45.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_45, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_45.started')
            # update status
            key_resp_45.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_45.clock.reset)  # t=0 on next screen flip
        
        # if key_resp_45 is stopping this frame...
        if key_resp_45.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 120-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_45.tStop = t  # not accounting for scr refresh
                key_resp_45.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_45.stopped')
                # update status
                key_resp_45.status = FINISHED
                key_resp_45.status = FINISHED
        if key_resp_45.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_45.getKeys(keyList=['left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_45_allKeys.extend(theseKeys)
            if len(_key_resp_45_allKeys):
                key_resp_45.keys = [key.name for key in _key_resp_45_allKeys]  # storing all keys
                key_resp_45.rt = [key.rt for key in _key_resp_45_allKeys]
                key_resp_45.duration = [key.duration for key in _key_resp_45_allKeys]
        
        # *target_13* updates
        
        # if target_13 is starting this frame...
        if target_13.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            target_13.frameNStart = frameN  # exact frame index
            target_13.tStart = t  # local t and not account for scr refresh
            target_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target_13.started')
            # update status
            target_13.status = STARTED
            target_13.setAutoDraw(True)
        
        # if target_13 is active this frame...
        if target_13.status == STARTED:
            # update params
            pass
        
        # if target_13 is stopping this frame...
        if target_13.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4-frameTolerance:
                # keep track of stop time/frame for later
                target_13.tStop = t  # not accounting for scr refresh
                target_13.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target_13.stopped')
                # update status
                target_13.status = FINISHED
                target_13.setAutoDraw(False)
        
        # *target2_13* updates
        
        # if target2_13 is starting this frame...
        if target2_13.status == NOT_STARTED and tThisFlip >= 8-frameTolerance:
            # keep track of start time/frame for later
            target2_13.frameNStart = frameN  # exact frame index
            target2_13.tStart = t  # local t and not account for scr refresh
            target2_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target2_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target2_13.started')
            # update status
            target2_13.status = STARTED
            target2_13.setAutoDraw(True)
        
        # if target2_13 is active this frame...
        if target2_13.status == STARTED:
            # update params
            pass
        
        # if target2_13 is stopping this frame...
        if target2_13.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 10-frameTolerance:
                # keep track of stop time/frame for later
                target2_13.tStop = t  # not accounting for scr refresh
                target2_13.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target2_13.stopped')
                # update status
                target2_13.status = FINISHED
                target2_13.setAutoDraw(False)
        
        # *target3_13* updates
        
        # if target3_13 is starting this frame...
        if target3_13.status == NOT_STARTED and tThisFlip >= 14-frameTolerance:
            # keep track of start time/frame for later
            target3_13.frameNStart = frameN  # exact frame index
            target3_13.tStart = t  # local t and not account for scr refresh
            target3_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target3_13, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target3_13.started')
            # update status
            target3_13.status = STARTED
            target3_13.setAutoDraw(True)
        
        # if target3_13 is active this frame...
        if target3_13.status == STARTED:
            # update params
            pass
        
        # if target3_13 is stopping this frame...
        if target3_13.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 16-frameTolerance:
                # keep track of stop time/frame for later
                target3_13.tStop = t  # not accounting for scr refresh
                target3_13.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target3_13.stopped')
                # update status
                target3_13.status = FINISHED
                target3_13.setAutoDraw(False)
        
        # *target4_13* updates
        
        # if target4_13 is starting this frame...
        if target4_13.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
            # keep track of start time/frame for later
            target4_13.frameNStart = frameN  # exact frame index
            target4_13.tStart = t  # local t and not account for scr refresh
            target4_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target4_13, 'tStartRefresh')  # time at next scr refresh
            # update status
            target4_13.status = STARTED
            target4_13.setAutoDraw(True)
        
        # if target4_13 is active this frame...
        if target4_13.status == STARTED:
            # update params
            pass
        
        # if target4_13 is stopping this frame...
        if target4_13.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 22-frameTolerance:
                # keep track of stop time/frame for later
                target4_13.tStop = t  # not accounting for scr refresh
                target4_13.frameNStop = frameN  # exact frame index
                # update status
                target4_13.status = FINISHED
                target4_13.setAutoDraw(False)
        
        # *target5_13* updates
        
        # if target5_13 is starting this frame...
        if target5_13.status == NOT_STARTED and tThisFlip >= 26-frameTolerance:
            # keep track of start time/frame for later
            target5_13.frameNStart = frameN  # exact frame index
            target5_13.tStart = t  # local t and not account for scr refresh
            target5_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target5_13, 'tStartRefresh')  # time at next scr refresh
            # update status
            target5_13.status = STARTED
            target5_13.setAutoDraw(True)
        
        # if target5_13 is active this frame...
        if target5_13.status == STARTED:
            # update params
            pass
        
        # if target5_13 is stopping this frame...
        if target5_13.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 28-frameTolerance:
                # keep track of stop time/frame for later
                target5_13.tStop = t  # not accounting for scr refresh
                target5_13.frameNStop = frameN  # exact frame index
                # update status
                target5_13.status = FINISHED
                target5_13.setAutoDraw(False)
        
        # *target6_13* updates
        
        # if target6_13 is starting this frame...
        if target6_13.status == NOT_STARTED and tThisFlip >= 32-frameTolerance:
            # keep track of start time/frame for later
            target6_13.frameNStart = frameN  # exact frame index
            target6_13.tStart = t  # local t and not account for scr refresh
            target6_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target6_13, 'tStartRefresh')  # time at next scr refresh
            # update status
            target6_13.status = STARTED
            target6_13.setAutoDraw(True)
        
        # if target6_13 is active this frame...
        if target6_13.status == STARTED:
            # update params
            pass
        
        # if target6_13 is stopping this frame...
        if target6_13.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 34-frameTolerance:
                # keep track of stop time/frame for later
                target6_13.tStop = t  # not accounting for scr refresh
                target6_13.frameNStop = frameN  # exact frame index
                # update status
                target6_13.status = FINISHED
                target6_13.setAutoDraw(False)
        
        # *target7_13* updates
        
        # if target7_13 is starting this frame...
        if target7_13.status == NOT_STARTED and tThisFlip >= 38-frameTolerance:
            # keep track of start time/frame for later
            target7_13.frameNStart = frameN  # exact frame index
            target7_13.tStart = t  # local t and not account for scr refresh
            target7_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target7_13, 'tStartRefresh')  # time at next scr refresh
            # update status
            target7_13.status = STARTED
            target7_13.setAutoDraw(True)
        
        # if target7_13 is active this frame...
        if target7_13.status == STARTED:
            # update params
            pass
        
        # if target7_13 is stopping this frame...
        if target7_13.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 40-frameTolerance:
                # keep track of stop time/frame for later
                target7_13.tStop = t  # not accounting for scr refresh
                target7_13.frameNStop = frameN  # exact frame index
                # update status
                target7_13.status = FINISHED
                target7_13.setAutoDraw(False)
        
        # *target8_13* updates
        
        # if target8_13 is starting this frame...
        if target8_13.status == NOT_STARTED and tThisFlip >= 44-frameTolerance:
            # keep track of start time/frame for later
            target8_13.frameNStart = frameN  # exact frame index
            target8_13.tStart = t  # local t and not account for scr refresh
            target8_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target8_13, 'tStartRefresh')  # time at next scr refresh
            # update status
            target8_13.status = STARTED
            target8_13.setAutoDraw(True)
        
        # if target8_13 is active this frame...
        if target8_13.status == STARTED:
            # update params
            pass
        
        # if target8_13 is stopping this frame...
        if target8_13.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 46-frameTolerance:
                # keep track of stop time/frame for later
                target8_13.tStop = t  # not accounting for scr refresh
                target8_13.frameNStop = frameN  # exact frame index
                # update status
                target8_13.status = FINISHED
                target8_13.setAutoDraw(False)
        
        # *target9_13* updates
        
        # if target9_13 is starting this frame...
        if target9_13.status == NOT_STARTED and tThisFlip >= 50-frameTolerance:
            # keep track of start time/frame for later
            target9_13.frameNStart = frameN  # exact frame index
            target9_13.tStart = t  # local t and not account for scr refresh
            target9_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target9_13, 'tStartRefresh')  # time at next scr refresh
            # update status
            target9_13.status = STARTED
            target9_13.setAutoDraw(True)
        
        # if target9_13 is active this frame...
        if target9_13.status == STARTED:
            # update params
            pass
        
        # if target9_13 is stopping this frame...
        if target9_13.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 52-frameTolerance:
                # keep track of stop time/frame for later
                target9_13.tStop = t  # not accounting for scr refresh
                target9_13.frameNStop = frameN  # exact frame index
                # update status
                target9_13.status = FINISHED
                target9_13.setAutoDraw(False)
        
        # *target10_13* updates
        
        # if target10_13 is starting this frame...
        if target10_13.status == NOT_STARTED and tThisFlip >= 56-frameTolerance:
            # keep track of start time/frame for later
            target10_13.frameNStart = frameN  # exact frame index
            target10_13.tStart = t  # local t and not account for scr refresh
            target10_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target10_13, 'tStartRefresh')  # time at next scr refresh
            # update status
            target10_13.status = STARTED
            target10_13.setAutoDraw(True)
        
        # if target10_13 is active this frame...
        if target10_13.status == STARTED:
            # update params
            pass
        
        # if target10_13 is stopping this frame...
        if target10_13.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 58-frameTolerance:
                # keep track of stop time/frame for later
                target10_13.tStop = t  # not accounting for scr refresh
                target10_13.frameNStop = frameN  # exact frame index
                # update status
                target10_13.status = FINISHED
                target10_13.setAutoDraw(False)
        
        # *target11_13* updates
        
        # if target11_13 is starting this frame...
        if target11_13.status == NOT_STARTED and tThisFlip >= 62-frameTolerance:
            # keep track of start time/frame for later
            target11_13.frameNStart = frameN  # exact frame index
            target11_13.tStart = t  # local t and not account for scr refresh
            target11_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target11_13, 'tStartRefresh')  # time at next scr refresh
            # update status
            target11_13.status = STARTED
            target11_13.setAutoDraw(True)
        
        # if target11_13 is active this frame...
        if target11_13.status == STARTED:
            # update params
            pass
        
        # if target11_13 is stopping this frame...
        if target11_13.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 64-frameTolerance:
                # keep track of stop time/frame for later
                target11_13.tStop = t  # not accounting for scr refresh
                target11_13.frameNStop = frameN  # exact frame index
                # update status
                target11_13.status = FINISHED
                target11_13.setAutoDraw(False)
        
        # *target12_13* updates
        
        # if target12_13 is starting this frame...
        if target12_13.status == NOT_STARTED and tThisFlip >= 68-frameTolerance:
            # keep track of start time/frame for later
            target12_13.frameNStart = frameN  # exact frame index
            target12_13.tStart = t  # local t and not account for scr refresh
            target12_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target12_13, 'tStartRefresh')  # time at next scr refresh
            # update status
            target12_13.status = STARTED
            target12_13.setAutoDraw(True)
        
        # if target12_13 is active this frame...
        if target12_13.status == STARTED:
            # update params
            pass
        
        # if target12_13 is stopping this frame...
        if target12_13.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 70-frameTolerance:
                # keep track of stop time/frame for later
                target12_13.tStop = t  # not accounting for scr refresh
                target12_13.frameNStop = frameN  # exact frame index
                # update status
                target12_13.status = FINISHED
                target12_13.setAutoDraw(False)
        
        # *target13_13* updates
        
        # if target13_13 is starting this frame...
        if target13_13.status == NOT_STARTED and tThisFlip >= 74-frameTolerance:
            # keep track of start time/frame for later
            target13_13.frameNStart = frameN  # exact frame index
            target13_13.tStart = t  # local t and not account for scr refresh
            target13_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target13_13, 'tStartRefresh')  # time at next scr refresh
            # update status
            target13_13.status = STARTED
            target13_13.setAutoDraw(True)
        
        # if target13_13 is active this frame...
        if target13_13.status == STARTED:
            # update params
            pass
        
        # if target13_13 is stopping this frame...
        if target13_13.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 76-frameTolerance:
                # keep track of stop time/frame for later
                target13_13.tStop = t  # not accounting for scr refresh
                target13_13.frameNStop = frameN  # exact frame index
                # update status
                target13_13.status = FINISHED
                target13_13.setAutoDraw(False)
        
        # *target14_13* updates
        
        # if target14_13 is starting this frame...
        if target14_13.status == NOT_STARTED and tThisFlip >= 80-frameTolerance:
            # keep track of start time/frame for later
            target14_13.frameNStart = frameN  # exact frame index
            target14_13.tStart = t  # local t and not account for scr refresh
            target14_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target14_13, 'tStartRefresh')  # time at next scr refresh
            # update status
            target14_13.status = STARTED
            target14_13.setAutoDraw(True)
        
        # if target14_13 is active this frame...
        if target14_13.status == STARTED:
            # update params
            pass
        
        # if target14_13 is stopping this frame...
        if target14_13.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 82-frameTolerance:
                # keep track of stop time/frame for later
                target14_13.tStop = t  # not accounting for scr refresh
                target14_13.frameNStop = frameN  # exact frame index
                # update status
                target14_13.status = FINISHED
                target14_13.setAutoDraw(False)
        
        # *target15_13* updates
        
        # if target15_13 is starting this frame...
        if target15_13.status == NOT_STARTED and tThisFlip >= 86-frameTolerance:
            # keep track of start time/frame for later
            target15_13.frameNStart = frameN  # exact frame index
            target15_13.tStart = t  # local t and not account for scr refresh
            target15_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target15_13, 'tStartRefresh')  # time at next scr refresh
            # update status
            target15_13.status = STARTED
            target15_13.setAutoDraw(True)
        
        # if target15_13 is active this frame...
        if target15_13.status == STARTED:
            # update params
            pass
        
        # if target15_13 is stopping this frame...
        if target15_13.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 88-frameTolerance:
                # keep track of stop time/frame for later
                target15_13.tStop = t  # not accounting for scr refresh
                target15_13.frameNStop = frameN  # exact frame index
                # update status
                target15_13.status = FINISHED
                target15_13.setAutoDraw(False)
        
        # *target16_13* updates
        
        # if target16_13 is starting this frame...
        if target16_13.status == NOT_STARTED and tThisFlip >= 92-frameTolerance:
            # keep track of start time/frame for later
            target16_13.frameNStart = frameN  # exact frame index
            target16_13.tStart = t  # local t and not account for scr refresh
            target16_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target16_13, 'tStartRefresh')  # time at next scr refresh
            # update status
            target16_13.status = STARTED
            target16_13.setAutoDraw(True)
        
        # if target16_13 is active this frame...
        if target16_13.status == STARTED:
            # update params
            pass
        
        # if target16_13 is stopping this frame...
        if target16_13.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 94-frameTolerance:
                # keep track of stop time/frame for later
                target16_13.tStop = t  # not accounting for scr refresh
                target16_13.frameNStop = frameN  # exact frame index
                # update status
                target16_13.status = FINISHED
                target16_13.setAutoDraw(False)
        
        # *target17_13* updates
        
        # if target17_13 is starting this frame...
        if target17_13.status == NOT_STARTED and tThisFlip >= 98-frameTolerance:
            # keep track of start time/frame for later
            target17_13.frameNStart = frameN  # exact frame index
            target17_13.tStart = t  # local t and not account for scr refresh
            target17_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target17_13, 'tStartRefresh')  # time at next scr refresh
            # update status
            target17_13.status = STARTED
            target17_13.setAutoDraw(True)
        
        # if target17_13 is active this frame...
        if target17_13.status == STARTED:
            # update params
            pass
        
        # if target17_13 is stopping this frame...
        if target17_13.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 100-frameTolerance:
                # keep track of stop time/frame for later
                target17_13.tStop = t  # not accounting for scr refresh
                target17_13.frameNStop = frameN  # exact frame index
                # update status
                target17_13.status = FINISHED
                target17_13.setAutoDraw(False)
        
        # *target18_13* updates
        
        # if target18_13 is starting this frame...
        if target18_13.status == NOT_STARTED and tThisFlip >= 104-frameTolerance:
            # keep track of start time/frame for later
            target18_13.frameNStart = frameN  # exact frame index
            target18_13.tStart = t  # local t and not account for scr refresh
            target18_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target18_13, 'tStartRefresh')  # time at next scr refresh
            # update status
            target18_13.status = STARTED
            target18_13.setAutoDraw(True)
        
        # if target18_13 is active this frame...
        if target18_13.status == STARTED:
            # update params
            pass
        
        # if target18_13 is stopping this frame...
        if target18_13.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 106-frameTolerance:
                # keep track of stop time/frame for later
                target18_13.tStop = t  # not accounting for scr refresh
                target18_13.frameNStop = frameN  # exact frame index
                # update status
                target18_13.status = FINISHED
                target18_13.setAutoDraw(False)
        
        # *target19_13* updates
        
        # if target19_13 is starting this frame...
        if target19_13.status == NOT_STARTED and tThisFlip >= 110-frameTolerance:
            # keep track of start time/frame for later
            target19_13.frameNStart = frameN  # exact frame index
            target19_13.tStart = t  # local t and not account for scr refresh
            target19_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target19_13, 'tStartRefresh')  # time at next scr refresh
            # update status
            target19_13.status = STARTED
            target19_13.setAutoDraw(True)
        
        # if target19_13 is active this frame...
        if target19_13.status == STARTED:
            # update params
            pass
        
        # if target19_13 is stopping this frame...
        if target19_13.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 112-frameTolerance:
                # keep track of stop time/frame for later
                target19_13.tStop = t  # not accounting for scr refresh
                target19_13.frameNStop = frameN  # exact frame index
                # update status
                target19_13.status = FINISHED
                target19_13.setAutoDraw(False)
        
        # *target20_13* updates
        
        # if target20_13 is starting this frame...
        if target20_13.status == NOT_STARTED and tThisFlip >= 116-frameTolerance:
            # keep track of start time/frame for later
            target20_13.frameNStart = frameN  # exact frame index
            target20_13.tStart = t  # local t and not account for scr refresh
            target20_13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target20_13, 'tStartRefresh')  # time at next scr refresh
            # update status
            target20_13.status = STARTED
            target20_13.setAutoDraw(True)
        
        # if target20_13 is active this frame...
        if target20_13.status == STARTED:
            # update params
            pass
        
        # if target20_13 is stopping this frame...
        if target20_13.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 118-frameTolerance:
                # keep track of stop time/frame for later
                target20_13.tStop = t  # not accounting for scr refresh
                target20_13.frameNStop = frameN  # exact frame index
                # update status
                target20_13.status = FINISHED
                target20_13.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial4" ---
    for thisComponent in trial4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('trial4.stopped', globalClock.getTime())
    sound_21.pause()  # ensure sound has stopped at end of Routine
    # check responses
    if key_resp_45.keys in ['', [], None]:  # No response was made
        key_resp_45.keys = None
    thisExp.addData('key_resp_45.keys',key_resp_45.keys)
    if key_resp_45.keys != None:  # we had a response
        thisExp.addData('key_resp_45.rt', key_resp_45.rt)
        thisExp.addData('key_resp_45.duration', key_resp_45.duration)
    thisExp.nextEntry()
    # the Routine "trial4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "c1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('c1.started', globalClock.getTime())
    slider_1.reset()
    # keep track of which components have finished
    c1Components = [slider_1, text_4]
    for thisComponent in c1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "c1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 15.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 15-frameTolerance:
            continueRoutine = False
        
        # *slider_1* updates
        
        # if slider_1 is starting this frame...
        if slider_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_1.frameNStart = frameN  # exact frame index
            slider_1.tStart = t  # local t and not account for scr refresh
            slider_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider_1.started')
            # update status
            slider_1.status = STARTED
            slider_1.setAutoDraw(True)
        
        # if slider_1 is active this frame...
        if slider_1.status == STARTED:
            # update params
            pass
        
        # if slider_1 is stopping this frame...
        if slider_1.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 15-frameTolerance:
                # keep track of stop time/frame for later
                slider_1.tStop = t  # not accounting for scr refresh
                slider_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_1.stopped')
                # update status
                slider_1.status = FINISHED
                slider_1.setAutoDraw(False)
        
        # *text_4* updates
        
        # if text_4 is starting this frame...
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_4.status = STARTED
            text_4.setAutoDraw(True)
        
        # if text_4 is active this frame...
        if text_4.status == STARTED:
            # update params
            pass
        
        # if text_4 is stopping this frame...
        if text_4.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 15-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                # update status
                text_4.status = FINISHED
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in c1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "c1" ---
    for thisComponent in c1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('c1.stopped', globalClock.getTime())
    thisExp.addData('slider_1.response', slider_1.getRating())
    thisExp.addData('slider_1.rt', slider_1.getRT())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-15.000000)
    
    # --- Prepare to start Routine "trial5" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('trial5.started', globalClock.getTime())
    sound_23.setSound('C:/Users/fatma/OneDrive/Desktop/IITK BOOKS/Decision Making/DM Project/Stimulus/task_sound_stimulus/t5.ogg.opus', hamming=True)
    sound_23.setVolume(1.0, log=False)
    sound_23.seek(0)
    key_resp_47.keys = []
    key_resp_47.rt = []
    _key_resp_47_allKeys = []
    # keep track of which components have finished
    trial5Components = [sound_23, key_resp_47, target_15, target2_15, target3_15, target4_15, target5_15, target6_15, target7_15, target8_15, target9_15, target10_15, target11_15, target12_15, target13_15, target14_15, target15_15, target16_15, target17_15, target18_15, target19_15, target20_15]
    for thisComponent in trial5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial5" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 120-frameTolerance:
            continueRoutine = False
        
        # if sound_23 is starting this frame...
        if sound_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_23.frameNStart = frameN  # exact frame index
            sound_23.tStart = t  # local t and not account for scr refresh
            sound_23.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_23.started', tThisFlipGlobal)
            # update status
            sound_23.status = STARTED
            sound_23.play(when=win)  # sync with win flip
        # update sound_23 status according to whether it's playing
        if sound_23.isPlaying:
            sound_23.status = STARTED
        elif sound_23.isFinished:
            sound_23.status = FINISHED
        
        # *key_resp_47* updates
        waitOnFlip = False
        
        # if key_resp_47 is starting this frame...
        if key_resp_47.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_47.frameNStart = frameN  # exact frame index
            key_resp_47.tStart = t  # local t and not account for scr refresh
            key_resp_47.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_47, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_47.started')
            # update status
            key_resp_47.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_47.clock.reset)  # t=0 on next screen flip
        
        # if key_resp_47 is stopping this frame...
        if key_resp_47.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 120-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_47.tStop = t  # not accounting for scr refresh
                key_resp_47.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_47.stopped')
                # update status
                key_resp_47.status = FINISHED
                key_resp_47.status = FINISHED
        if key_resp_47.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_47.getKeys(keyList=['left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_47_allKeys.extend(theseKeys)
            if len(_key_resp_47_allKeys):
                key_resp_47.keys = [key.name for key in _key_resp_47_allKeys]  # storing all keys
                key_resp_47.rt = [key.rt for key in _key_resp_47_allKeys]
                key_resp_47.duration = [key.duration for key in _key_resp_47_allKeys]
        
        # *target_15* updates
        
        # if target_15 is starting this frame...
        if target_15.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            target_15.frameNStart = frameN  # exact frame index
            target_15.tStart = t  # local t and not account for scr refresh
            target_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target_15.started')
            # update status
            target_15.status = STARTED
            target_15.setAutoDraw(True)
        
        # if target_15 is active this frame...
        if target_15.status == STARTED:
            # update params
            pass
        
        # if target_15 is stopping this frame...
        if target_15.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4-frameTolerance:
                # keep track of stop time/frame for later
                target_15.tStop = t  # not accounting for scr refresh
                target_15.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target_15.stopped')
                # update status
                target_15.status = FINISHED
                target_15.setAutoDraw(False)
        
        # *target2_15* updates
        
        # if target2_15 is starting this frame...
        if target2_15.status == NOT_STARTED and tThisFlip >= 8-frameTolerance:
            # keep track of start time/frame for later
            target2_15.frameNStart = frameN  # exact frame index
            target2_15.tStart = t  # local t and not account for scr refresh
            target2_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target2_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target2_15.started')
            # update status
            target2_15.status = STARTED
            target2_15.setAutoDraw(True)
        
        # if target2_15 is active this frame...
        if target2_15.status == STARTED:
            # update params
            pass
        
        # if target2_15 is stopping this frame...
        if target2_15.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 10-frameTolerance:
                # keep track of stop time/frame for later
                target2_15.tStop = t  # not accounting for scr refresh
                target2_15.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target2_15.stopped')
                # update status
                target2_15.status = FINISHED
                target2_15.setAutoDraw(False)
        
        # *target3_15* updates
        
        # if target3_15 is starting this frame...
        if target3_15.status == NOT_STARTED and tThisFlip >= 14-frameTolerance:
            # keep track of start time/frame for later
            target3_15.frameNStart = frameN  # exact frame index
            target3_15.tStart = t  # local t and not account for scr refresh
            target3_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target3_15, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target3_15.started')
            # update status
            target3_15.status = STARTED
            target3_15.setAutoDraw(True)
        
        # if target3_15 is active this frame...
        if target3_15.status == STARTED:
            # update params
            pass
        
        # if target3_15 is stopping this frame...
        if target3_15.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 16-frameTolerance:
                # keep track of stop time/frame for later
                target3_15.tStop = t  # not accounting for scr refresh
                target3_15.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target3_15.stopped')
                # update status
                target3_15.status = FINISHED
                target3_15.setAutoDraw(False)
        
        # *target4_15* updates
        
        # if target4_15 is starting this frame...
        if target4_15.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
            # keep track of start time/frame for later
            target4_15.frameNStart = frameN  # exact frame index
            target4_15.tStart = t  # local t and not account for scr refresh
            target4_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target4_15, 'tStartRefresh')  # time at next scr refresh
            # update status
            target4_15.status = STARTED
            target4_15.setAutoDraw(True)
        
        # if target4_15 is active this frame...
        if target4_15.status == STARTED:
            # update params
            pass
        
        # if target4_15 is stopping this frame...
        if target4_15.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 22-frameTolerance:
                # keep track of stop time/frame for later
                target4_15.tStop = t  # not accounting for scr refresh
                target4_15.frameNStop = frameN  # exact frame index
                # update status
                target4_15.status = FINISHED
                target4_15.setAutoDraw(False)
        
        # *target5_15* updates
        
        # if target5_15 is starting this frame...
        if target5_15.status == NOT_STARTED and tThisFlip >= 26-frameTolerance:
            # keep track of start time/frame for later
            target5_15.frameNStart = frameN  # exact frame index
            target5_15.tStart = t  # local t and not account for scr refresh
            target5_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target5_15, 'tStartRefresh')  # time at next scr refresh
            # update status
            target5_15.status = STARTED
            target5_15.setAutoDraw(True)
        
        # if target5_15 is active this frame...
        if target5_15.status == STARTED:
            # update params
            pass
        
        # if target5_15 is stopping this frame...
        if target5_15.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 28-frameTolerance:
                # keep track of stop time/frame for later
                target5_15.tStop = t  # not accounting for scr refresh
                target5_15.frameNStop = frameN  # exact frame index
                # update status
                target5_15.status = FINISHED
                target5_15.setAutoDraw(False)
        
        # *target6_15* updates
        
        # if target6_15 is starting this frame...
        if target6_15.status == NOT_STARTED and tThisFlip >= 32-frameTolerance:
            # keep track of start time/frame for later
            target6_15.frameNStart = frameN  # exact frame index
            target6_15.tStart = t  # local t and not account for scr refresh
            target6_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target6_15, 'tStartRefresh')  # time at next scr refresh
            # update status
            target6_15.status = STARTED
            target6_15.setAutoDraw(True)
        
        # if target6_15 is active this frame...
        if target6_15.status == STARTED:
            # update params
            pass
        
        # if target6_15 is stopping this frame...
        if target6_15.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 34-frameTolerance:
                # keep track of stop time/frame for later
                target6_15.tStop = t  # not accounting for scr refresh
                target6_15.frameNStop = frameN  # exact frame index
                # update status
                target6_15.status = FINISHED
                target6_15.setAutoDraw(False)
        
        # *target7_15* updates
        
        # if target7_15 is starting this frame...
        if target7_15.status == NOT_STARTED and tThisFlip >= 38-frameTolerance:
            # keep track of start time/frame for later
            target7_15.frameNStart = frameN  # exact frame index
            target7_15.tStart = t  # local t and not account for scr refresh
            target7_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target7_15, 'tStartRefresh')  # time at next scr refresh
            # update status
            target7_15.status = STARTED
            target7_15.setAutoDraw(True)
        
        # if target7_15 is active this frame...
        if target7_15.status == STARTED:
            # update params
            pass
        
        # if target7_15 is stopping this frame...
        if target7_15.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 40-frameTolerance:
                # keep track of stop time/frame for later
                target7_15.tStop = t  # not accounting for scr refresh
                target7_15.frameNStop = frameN  # exact frame index
                # update status
                target7_15.status = FINISHED
                target7_15.setAutoDraw(False)
        
        # *target8_15* updates
        
        # if target8_15 is starting this frame...
        if target8_15.status == NOT_STARTED and tThisFlip >= 44-frameTolerance:
            # keep track of start time/frame for later
            target8_15.frameNStart = frameN  # exact frame index
            target8_15.tStart = t  # local t and not account for scr refresh
            target8_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target8_15, 'tStartRefresh')  # time at next scr refresh
            # update status
            target8_15.status = STARTED
            target8_15.setAutoDraw(True)
        
        # if target8_15 is active this frame...
        if target8_15.status == STARTED:
            # update params
            pass
        
        # if target8_15 is stopping this frame...
        if target8_15.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 46-frameTolerance:
                # keep track of stop time/frame for later
                target8_15.tStop = t  # not accounting for scr refresh
                target8_15.frameNStop = frameN  # exact frame index
                # update status
                target8_15.status = FINISHED
                target8_15.setAutoDraw(False)
        
        # *target9_15* updates
        
        # if target9_15 is starting this frame...
        if target9_15.status == NOT_STARTED and tThisFlip >= 50-frameTolerance:
            # keep track of start time/frame for later
            target9_15.frameNStart = frameN  # exact frame index
            target9_15.tStart = t  # local t and not account for scr refresh
            target9_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target9_15, 'tStartRefresh')  # time at next scr refresh
            # update status
            target9_15.status = STARTED
            target9_15.setAutoDraw(True)
        
        # if target9_15 is active this frame...
        if target9_15.status == STARTED:
            # update params
            pass
        
        # if target9_15 is stopping this frame...
        if target9_15.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 52-frameTolerance:
                # keep track of stop time/frame for later
                target9_15.tStop = t  # not accounting for scr refresh
                target9_15.frameNStop = frameN  # exact frame index
                # update status
                target9_15.status = FINISHED
                target9_15.setAutoDraw(False)
        
        # *target10_15* updates
        
        # if target10_15 is starting this frame...
        if target10_15.status == NOT_STARTED and tThisFlip >= 56-frameTolerance:
            # keep track of start time/frame for later
            target10_15.frameNStart = frameN  # exact frame index
            target10_15.tStart = t  # local t and not account for scr refresh
            target10_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target10_15, 'tStartRefresh')  # time at next scr refresh
            # update status
            target10_15.status = STARTED
            target10_15.setAutoDraw(True)
        
        # if target10_15 is active this frame...
        if target10_15.status == STARTED:
            # update params
            pass
        
        # if target10_15 is stopping this frame...
        if target10_15.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 58-frameTolerance:
                # keep track of stop time/frame for later
                target10_15.tStop = t  # not accounting for scr refresh
                target10_15.frameNStop = frameN  # exact frame index
                # update status
                target10_15.status = FINISHED
                target10_15.setAutoDraw(False)
        
        # *target11_15* updates
        
        # if target11_15 is starting this frame...
        if target11_15.status == NOT_STARTED and tThisFlip >= 62-frameTolerance:
            # keep track of start time/frame for later
            target11_15.frameNStart = frameN  # exact frame index
            target11_15.tStart = t  # local t and not account for scr refresh
            target11_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target11_15, 'tStartRefresh')  # time at next scr refresh
            # update status
            target11_15.status = STARTED
            target11_15.setAutoDraw(True)
        
        # if target11_15 is active this frame...
        if target11_15.status == STARTED:
            # update params
            pass
        
        # if target11_15 is stopping this frame...
        if target11_15.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 64-frameTolerance:
                # keep track of stop time/frame for later
                target11_15.tStop = t  # not accounting for scr refresh
                target11_15.frameNStop = frameN  # exact frame index
                # update status
                target11_15.status = FINISHED
                target11_15.setAutoDraw(False)
        
        # *target12_15* updates
        
        # if target12_15 is starting this frame...
        if target12_15.status == NOT_STARTED and tThisFlip >= 68-frameTolerance:
            # keep track of start time/frame for later
            target12_15.frameNStart = frameN  # exact frame index
            target12_15.tStart = t  # local t and not account for scr refresh
            target12_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target12_15, 'tStartRefresh')  # time at next scr refresh
            # update status
            target12_15.status = STARTED
            target12_15.setAutoDraw(True)
        
        # if target12_15 is active this frame...
        if target12_15.status == STARTED:
            # update params
            pass
        
        # if target12_15 is stopping this frame...
        if target12_15.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 70-frameTolerance:
                # keep track of stop time/frame for later
                target12_15.tStop = t  # not accounting for scr refresh
                target12_15.frameNStop = frameN  # exact frame index
                # update status
                target12_15.status = FINISHED
                target12_15.setAutoDraw(False)
        
        # *target13_15* updates
        
        # if target13_15 is starting this frame...
        if target13_15.status == NOT_STARTED and tThisFlip >= 74-frameTolerance:
            # keep track of start time/frame for later
            target13_15.frameNStart = frameN  # exact frame index
            target13_15.tStart = t  # local t and not account for scr refresh
            target13_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target13_15, 'tStartRefresh')  # time at next scr refresh
            # update status
            target13_15.status = STARTED
            target13_15.setAutoDraw(True)
        
        # if target13_15 is active this frame...
        if target13_15.status == STARTED:
            # update params
            pass
        
        # if target13_15 is stopping this frame...
        if target13_15.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 76-frameTolerance:
                # keep track of stop time/frame for later
                target13_15.tStop = t  # not accounting for scr refresh
                target13_15.frameNStop = frameN  # exact frame index
                # update status
                target13_15.status = FINISHED
                target13_15.setAutoDraw(False)
        
        # *target14_15* updates
        
        # if target14_15 is starting this frame...
        if target14_15.status == NOT_STARTED and tThisFlip >= 80-frameTolerance:
            # keep track of start time/frame for later
            target14_15.frameNStart = frameN  # exact frame index
            target14_15.tStart = t  # local t and not account for scr refresh
            target14_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target14_15, 'tStartRefresh')  # time at next scr refresh
            # update status
            target14_15.status = STARTED
            target14_15.setAutoDraw(True)
        
        # if target14_15 is active this frame...
        if target14_15.status == STARTED:
            # update params
            pass
        
        # if target14_15 is stopping this frame...
        if target14_15.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 82-frameTolerance:
                # keep track of stop time/frame for later
                target14_15.tStop = t  # not accounting for scr refresh
                target14_15.frameNStop = frameN  # exact frame index
                # update status
                target14_15.status = FINISHED
                target14_15.setAutoDraw(False)
        
        # *target15_15* updates
        
        # if target15_15 is starting this frame...
        if target15_15.status == NOT_STARTED and tThisFlip >= 86-frameTolerance:
            # keep track of start time/frame for later
            target15_15.frameNStart = frameN  # exact frame index
            target15_15.tStart = t  # local t and not account for scr refresh
            target15_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target15_15, 'tStartRefresh')  # time at next scr refresh
            # update status
            target15_15.status = STARTED
            target15_15.setAutoDraw(True)
        
        # if target15_15 is active this frame...
        if target15_15.status == STARTED:
            # update params
            pass
        
        # if target15_15 is stopping this frame...
        if target15_15.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 88-frameTolerance:
                # keep track of stop time/frame for later
                target15_15.tStop = t  # not accounting for scr refresh
                target15_15.frameNStop = frameN  # exact frame index
                # update status
                target15_15.status = FINISHED
                target15_15.setAutoDraw(False)
        
        # *target16_15* updates
        
        # if target16_15 is starting this frame...
        if target16_15.status == NOT_STARTED and tThisFlip >= 92-frameTolerance:
            # keep track of start time/frame for later
            target16_15.frameNStart = frameN  # exact frame index
            target16_15.tStart = t  # local t and not account for scr refresh
            target16_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target16_15, 'tStartRefresh')  # time at next scr refresh
            # update status
            target16_15.status = STARTED
            target16_15.setAutoDraw(True)
        
        # if target16_15 is active this frame...
        if target16_15.status == STARTED:
            # update params
            pass
        
        # if target16_15 is stopping this frame...
        if target16_15.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 94-frameTolerance:
                # keep track of stop time/frame for later
                target16_15.tStop = t  # not accounting for scr refresh
                target16_15.frameNStop = frameN  # exact frame index
                # update status
                target16_15.status = FINISHED
                target16_15.setAutoDraw(False)
        
        # *target17_15* updates
        
        # if target17_15 is starting this frame...
        if target17_15.status == NOT_STARTED and tThisFlip >= 98-frameTolerance:
            # keep track of start time/frame for later
            target17_15.frameNStart = frameN  # exact frame index
            target17_15.tStart = t  # local t and not account for scr refresh
            target17_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target17_15, 'tStartRefresh')  # time at next scr refresh
            # update status
            target17_15.status = STARTED
            target17_15.setAutoDraw(True)
        
        # if target17_15 is active this frame...
        if target17_15.status == STARTED:
            # update params
            pass
        
        # if target17_15 is stopping this frame...
        if target17_15.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 100-frameTolerance:
                # keep track of stop time/frame for later
                target17_15.tStop = t  # not accounting for scr refresh
                target17_15.frameNStop = frameN  # exact frame index
                # update status
                target17_15.status = FINISHED
                target17_15.setAutoDraw(False)
        
        # *target18_15* updates
        
        # if target18_15 is starting this frame...
        if target18_15.status == NOT_STARTED and tThisFlip >= 104-frameTolerance:
            # keep track of start time/frame for later
            target18_15.frameNStart = frameN  # exact frame index
            target18_15.tStart = t  # local t and not account for scr refresh
            target18_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target18_15, 'tStartRefresh')  # time at next scr refresh
            # update status
            target18_15.status = STARTED
            target18_15.setAutoDraw(True)
        
        # if target18_15 is active this frame...
        if target18_15.status == STARTED:
            # update params
            pass
        
        # if target18_15 is stopping this frame...
        if target18_15.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 106-frameTolerance:
                # keep track of stop time/frame for later
                target18_15.tStop = t  # not accounting for scr refresh
                target18_15.frameNStop = frameN  # exact frame index
                # update status
                target18_15.status = FINISHED
                target18_15.setAutoDraw(False)
        
        # *target19_15* updates
        
        # if target19_15 is starting this frame...
        if target19_15.status == NOT_STARTED and tThisFlip >= 110-frameTolerance:
            # keep track of start time/frame for later
            target19_15.frameNStart = frameN  # exact frame index
            target19_15.tStart = t  # local t and not account for scr refresh
            target19_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target19_15, 'tStartRefresh')  # time at next scr refresh
            # update status
            target19_15.status = STARTED
            target19_15.setAutoDraw(True)
        
        # if target19_15 is active this frame...
        if target19_15.status == STARTED:
            # update params
            pass
        
        # if target19_15 is stopping this frame...
        if target19_15.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 112-frameTolerance:
                # keep track of stop time/frame for later
                target19_15.tStop = t  # not accounting for scr refresh
                target19_15.frameNStop = frameN  # exact frame index
                # update status
                target19_15.status = FINISHED
                target19_15.setAutoDraw(False)
        
        # *target20_15* updates
        
        # if target20_15 is starting this frame...
        if target20_15.status == NOT_STARTED and tThisFlip >= 116-frameTolerance:
            # keep track of start time/frame for later
            target20_15.frameNStart = frameN  # exact frame index
            target20_15.tStart = t  # local t and not account for scr refresh
            target20_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target20_15, 'tStartRefresh')  # time at next scr refresh
            # update status
            target20_15.status = STARTED
            target20_15.setAutoDraw(True)
        
        # if target20_15 is active this frame...
        if target20_15.status == STARTED:
            # update params
            pass
        
        # if target20_15 is stopping this frame...
        if target20_15.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 118-frameTolerance:
                # keep track of stop time/frame for later
                target20_15.tStop = t  # not accounting for scr refresh
                target20_15.frameNStop = frameN  # exact frame index
                # update status
                target20_15.status = FINISHED
                target20_15.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial5" ---
    for thisComponent in trial5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('trial5.stopped', globalClock.getTime())
    sound_23.pause()  # ensure sound has stopped at end of Routine
    # check responses
    if key_resp_47.keys in ['', [], None]:  # No response was made
        key_resp_47.keys = None
    thisExp.addData('key_resp_47.keys',key_resp_47.keys)
    if key_resp_47.keys != None:  # we had a response
        thisExp.addData('key_resp_47.rt', key_resp_47.rt)
        thisExp.addData('key_resp_47.duration', key_resp_47.duration)
    thisExp.nextEntry()
    # the Routine "trial5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "c1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('c1.started', globalClock.getTime())
    slider_1.reset()
    # keep track of which components have finished
    c1Components = [slider_1, text_4]
    for thisComponent in c1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "c1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 15.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 15-frameTolerance:
            continueRoutine = False
        
        # *slider_1* updates
        
        # if slider_1 is starting this frame...
        if slider_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_1.frameNStart = frameN  # exact frame index
            slider_1.tStart = t  # local t and not account for scr refresh
            slider_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider_1.started')
            # update status
            slider_1.status = STARTED
            slider_1.setAutoDraw(True)
        
        # if slider_1 is active this frame...
        if slider_1.status == STARTED:
            # update params
            pass
        
        # if slider_1 is stopping this frame...
        if slider_1.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 15-frameTolerance:
                # keep track of stop time/frame for later
                slider_1.tStop = t  # not accounting for scr refresh
                slider_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_1.stopped')
                # update status
                slider_1.status = FINISHED
                slider_1.setAutoDraw(False)
        
        # *text_4* updates
        
        # if text_4 is starting this frame...
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_4.status = STARTED
            text_4.setAutoDraw(True)
        
        # if text_4 is active this frame...
        if text_4.status == STARTED:
            # update params
            pass
        
        # if text_4 is stopping this frame...
        if text_4.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 15-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                # update status
                text_4.status = FINISHED
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in c1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "c1" ---
    for thisComponent in c1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('c1.stopped', globalClock.getTime())
    thisExp.addData('slider_1.response', slider_1.getRating())
    thisExp.addData('slider_1.rt', slider_1.getRT())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-15.000000)
    
    # --- Prepare to start Routine "catch1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('catch1.started', globalClock.getTime())
    sound_14.setSound('C:/Users/fatma/OneDrive/Desktop/IITK BOOKS/Decision Making/DM Project/Stimulus/task_sound_stimulus/catch_trail.ogg.opus', secs=30, hamming=True)
    sound_14.setVolume(1.0, log=False)
    sound_14.seek(0)
    key_resp_20.keys = []
    key_resp_20.rt = []
    _key_resp_20_allKeys = []
    # keep track of which components have finished
    catch1Components = [sound_14, key_resp_20, ct1_2, ct2_2, ct3_2, ct4_2, ct5_2]
    for thisComponent in catch1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "catch1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 30.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 30-frameTolerance:
            continueRoutine = False
        
        # if sound_14 is starting this frame...
        if sound_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_14.frameNStart = frameN  # exact frame index
            sound_14.tStart = t  # local t and not account for scr refresh
            sound_14.tStartRefresh = tThisFlipGlobal  # on global time
            # update status
            sound_14.status = STARTED
            sound_14.play(when=win)  # sync with win flip
        
        # if sound_14 is stopping this frame...
        if sound_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_14.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                sound_14.tStop = t  # not accounting for scr refresh
                sound_14.frameNStop = frameN  # exact frame index
                # update status
                sound_14.status = FINISHED
                sound_14.stop()
        # update sound_14 status according to whether it's playing
        if sound_14.isPlaying:
            sound_14.status = STARTED
        elif sound_14.isFinished:
            sound_14.status = FINISHED
        
        # *key_resp_20* updates
        waitOnFlip = False
        
        # if key_resp_20 is starting this frame...
        if key_resp_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_20.frameNStart = frameN  # exact frame index
            key_resp_20.tStart = t  # local t and not account for scr refresh
            key_resp_20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_20, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_20.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_20.clock.reset)  # t=0 on next screen flip
        
        # if key_resp_20 is stopping this frame...
        if key_resp_20.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 30-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_20.tStop = t  # not accounting for scr refresh
                key_resp_20.frameNStop = frameN  # exact frame index
                # update status
                key_resp_20.status = FINISHED
                key_resp_20.status = FINISHED
        if key_resp_20.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_20.getKeys(keyList=['left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_20_allKeys.extend(theseKeys)
            if len(_key_resp_20_allKeys):
                key_resp_20.keys = [key.name for key in _key_resp_20_allKeys]  # storing all keys
                key_resp_20.rt = [key.rt for key in _key_resp_20_allKeys]
                key_resp_20.duration = [key.duration for key in _key_resp_20_allKeys]
        
        # *ct1_2* updates
        
        # if ct1_2 is starting this frame...
        if ct1_2.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            ct1_2.frameNStart = frameN  # exact frame index
            ct1_2.tStart = t  # local t and not account for scr refresh
            ct1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ct1_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ct1_2.started')
            # update status
            ct1_2.status = STARTED
            ct1_2.setAutoDraw(True)
        
        # if ct1_2 is active this frame...
        if ct1_2.status == STARTED:
            # update params
            pass
        
        # if ct1_2 is stopping this frame...
        if ct1_2.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4-frameTolerance:
                # keep track of stop time/frame for later
                ct1_2.tStop = t  # not accounting for scr refresh
                ct1_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ct1_2.stopped')
                # update status
                ct1_2.status = FINISHED
                ct1_2.setAutoDraw(False)
        
        # *ct2_2* updates
        
        # if ct2_2 is starting this frame...
        if ct2_2.status == NOT_STARTED and tThisFlip >= 8-frameTolerance:
            # keep track of start time/frame for later
            ct2_2.frameNStart = frameN  # exact frame index
            ct2_2.tStart = t  # local t and not account for scr refresh
            ct2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ct2_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ct2_2.started')
            # update status
            ct2_2.status = STARTED
            ct2_2.setAutoDraw(True)
        
        # if ct2_2 is active this frame...
        if ct2_2.status == STARTED:
            # update params
            pass
        
        # if ct2_2 is stopping this frame...
        if ct2_2.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 10-frameTolerance:
                # keep track of stop time/frame for later
                ct2_2.tStop = t  # not accounting for scr refresh
                ct2_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ct2_2.stopped')
                # update status
                ct2_2.status = FINISHED
                ct2_2.setAutoDraw(False)
        
        # *ct3_2* updates
        
        # if ct3_2 is starting this frame...
        if ct3_2.status == NOT_STARTED and tThisFlip >= 14-frameTolerance:
            # keep track of start time/frame for later
            ct3_2.frameNStart = frameN  # exact frame index
            ct3_2.tStart = t  # local t and not account for scr refresh
            ct3_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ct3_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ct3_2.started')
            # update status
            ct3_2.status = STARTED
            ct3_2.setAutoDraw(True)
        
        # if ct3_2 is active this frame...
        if ct3_2.status == STARTED:
            # update params
            pass
        
        # if ct3_2 is stopping this frame...
        if ct3_2.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 16-frameTolerance:
                # keep track of stop time/frame for later
                ct3_2.tStop = t  # not accounting for scr refresh
                ct3_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ct3_2.stopped')
                # update status
                ct3_2.status = FINISHED
                ct3_2.setAutoDraw(False)
        
        # *ct4_2* updates
        
        # if ct4_2 is starting this frame...
        if ct4_2.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
            # keep track of start time/frame for later
            ct4_2.frameNStart = frameN  # exact frame index
            ct4_2.tStart = t  # local t and not account for scr refresh
            ct4_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ct4_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ct4_2.started')
            # update status
            ct4_2.status = STARTED
            ct4_2.setAutoDraw(True)
        
        # if ct4_2 is active this frame...
        if ct4_2.status == STARTED:
            # update params
            pass
        
        # if ct4_2 is stopping this frame...
        if ct4_2.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 22-frameTolerance:
                # keep track of stop time/frame for later
                ct4_2.tStop = t  # not accounting for scr refresh
                ct4_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ct4_2.stopped')
                # update status
                ct4_2.status = FINISHED
                ct4_2.setAutoDraw(False)
        
        # *ct5_2* updates
        
        # if ct5_2 is starting this frame...
        if ct5_2.status == NOT_STARTED and tThisFlip >= 26-frameTolerance:
            # keep track of start time/frame for later
            ct5_2.frameNStart = frameN  # exact frame index
            ct5_2.tStart = t  # local t and not account for scr refresh
            ct5_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(ct5_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'ct5_2.started')
            # update status
            ct5_2.status = STARTED
            ct5_2.setAutoDraw(True)
        
        # if ct5_2 is active this frame...
        if ct5_2.status == STARTED:
            # update params
            pass
        
        # if ct5_2 is stopping this frame...
        if ct5_2.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 28-frameTolerance:
                # keep track of stop time/frame for later
                ct5_2.tStop = t  # not accounting for scr refresh
                ct5_2.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'ct5_2.stopped')
                # update status
                ct5_2.status = FINISHED
                ct5_2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in catch1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "catch1" ---
    for thisComponent in catch1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('catch1.stopped', globalClock.getTime())
    sound_14.pause()  # ensure sound has stopped at end of Routine
    # check responses
    if key_resp_20.keys in ['', [], None]:  # No response was made
        key_resp_20.keys = None
    thisExp.addData('key_resp_20.keys',key_resp_20.keys)
    if key_resp_20.keys != None:  # we had a response
        thisExp.addData('key_resp_20.rt', key_resp_20.rt)
        thisExp.addData('key_resp_20.duration', key_resp_20.duration)
    thisExp.nextEntry()
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-30.000000)
    
    # --- Prepare to start Routine "c1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('c1.started', globalClock.getTime())
    slider_1.reset()
    # keep track of which components have finished
    c1Components = [slider_1, text_4]
    for thisComponent in c1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "c1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 15.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 15-frameTolerance:
            continueRoutine = False
        
        # *slider_1* updates
        
        # if slider_1 is starting this frame...
        if slider_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_1.frameNStart = frameN  # exact frame index
            slider_1.tStart = t  # local t and not account for scr refresh
            slider_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider_1.started')
            # update status
            slider_1.status = STARTED
            slider_1.setAutoDraw(True)
        
        # if slider_1 is active this frame...
        if slider_1.status == STARTED:
            # update params
            pass
        
        # if slider_1 is stopping this frame...
        if slider_1.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 15-frameTolerance:
                # keep track of stop time/frame for later
                slider_1.tStop = t  # not accounting for scr refresh
                slider_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_1.stopped')
                # update status
                slider_1.status = FINISHED
                slider_1.setAutoDraw(False)
        
        # *text_4* updates
        
        # if text_4 is starting this frame...
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_4.status = STARTED
            text_4.setAutoDraw(True)
        
        # if text_4 is active this frame...
        if text_4.status == STARTED:
            # update params
            pass
        
        # if text_4 is stopping this frame...
        if text_4.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 15-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                # update status
                text_4.status = FINISHED
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in c1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "c1" ---
    for thisComponent in c1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('c1.stopped', globalClock.getTime())
    thisExp.addData('slider_1.response', slider_1.getRating())
    thisExp.addData('slider_1.rt', slider_1.getRT())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-15.000000)
    
    # --- Prepare to start Routine "trial6" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('trial6.started', globalClock.getTime())
    sound_22.setSound('C:/Users/fatma/OneDrive/Desktop/IITK BOOKS/Decision Making/DM Project/Stimulus/task_sound_stimulus/t6.ogg.opus', hamming=True)
    sound_22.setVolume(1.0, log=False)
    sound_22.seek(0)
    key_resp_46.keys = []
    key_resp_46.rt = []
    _key_resp_46_allKeys = []
    # keep track of which components have finished
    trial6Components = [sound_22, key_resp_46, target_14, target2_14, target3_14, target4_14, target5_14, target6_14, target7_14, target8_14, target9_14, target10_14, target11_14, target12_14, target13_14, target14_14, target15_14, target16_14, target17_14, target18_14, target19_14, target20_14]
    for thisComponent in trial6Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial6" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 120-frameTolerance:
            continueRoutine = False
        
        # if sound_22 is starting this frame...
        if sound_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_22.frameNStart = frameN  # exact frame index
            sound_22.tStart = t  # local t and not account for scr refresh
            sound_22.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_22.started', tThisFlipGlobal)
            # update status
            sound_22.status = STARTED
            sound_22.play(when=win)  # sync with win flip
        # update sound_22 status according to whether it's playing
        if sound_22.isPlaying:
            sound_22.status = STARTED
        elif sound_22.isFinished:
            sound_22.status = FINISHED
        
        # *key_resp_46* updates
        waitOnFlip = False
        
        # if key_resp_46 is starting this frame...
        if key_resp_46.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_46.frameNStart = frameN  # exact frame index
            key_resp_46.tStart = t  # local t and not account for scr refresh
            key_resp_46.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_46, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_46.started')
            # update status
            key_resp_46.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_46.clock.reset)  # t=0 on next screen flip
        
        # if key_resp_46 is stopping this frame...
        if key_resp_46.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 120-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_46.tStop = t  # not accounting for scr refresh
                key_resp_46.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_46.stopped')
                # update status
                key_resp_46.status = FINISHED
                key_resp_46.status = FINISHED
        if key_resp_46.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_46.getKeys(keyList=['left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_46_allKeys.extend(theseKeys)
            if len(_key_resp_46_allKeys):
                key_resp_46.keys = [key.name for key in _key_resp_46_allKeys]  # storing all keys
                key_resp_46.rt = [key.rt for key in _key_resp_46_allKeys]
                key_resp_46.duration = [key.duration for key in _key_resp_46_allKeys]
        
        # *target_14* updates
        
        # if target_14 is starting this frame...
        if target_14.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            target_14.frameNStart = frameN  # exact frame index
            target_14.tStart = t  # local t and not account for scr refresh
            target_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target_14.started')
            # update status
            target_14.status = STARTED
            target_14.setAutoDraw(True)
        
        # if target_14 is active this frame...
        if target_14.status == STARTED:
            # update params
            pass
        
        # if target_14 is stopping this frame...
        if target_14.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4-frameTolerance:
                # keep track of stop time/frame for later
                target_14.tStop = t  # not accounting for scr refresh
                target_14.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target_14.stopped')
                # update status
                target_14.status = FINISHED
                target_14.setAutoDraw(False)
        
        # *target2_14* updates
        
        # if target2_14 is starting this frame...
        if target2_14.status == NOT_STARTED and tThisFlip >= 8-frameTolerance:
            # keep track of start time/frame for later
            target2_14.frameNStart = frameN  # exact frame index
            target2_14.tStart = t  # local t and not account for scr refresh
            target2_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target2_14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target2_14.started')
            # update status
            target2_14.status = STARTED
            target2_14.setAutoDraw(True)
        
        # if target2_14 is active this frame...
        if target2_14.status == STARTED:
            # update params
            pass
        
        # if target2_14 is stopping this frame...
        if target2_14.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 10-frameTolerance:
                # keep track of stop time/frame for later
                target2_14.tStop = t  # not accounting for scr refresh
                target2_14.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target2_14.stopped')
                # update status
                target2_14.status = FINISHED
                target2_14.setAutoDraw(False)
        
        # *target3_14* updates
        
        # if target3_14 is starting this frame...
        if target3_14.status == NOT_STARTED and tThisFlip >= 14-frameTolerance:
            # keep track of start time/frame for later
            target3_14.frameNStart = frameN  # exact frame index
            target3_14.tStart = t  # local t and not account for scr refresh
            target3_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target3_14, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target3_14.started')
            # update status
            target3_14.status = STARTED
            target3_14.setAutoDraw(True)
        
        # if target3_14 is active this frame...
        if target3_14.status == STARTED:
            # update params
            pass
        
        # if target3_14 is stopping this frame...
        if target3_14.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 16-frameTolerance:
                # keep track of stop time/frame for later
                target3_14.tStop = t  # not accounting for scr refresh
                target3_14.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target3_14.stopped')
                # update status
                target3_14.status = FINISHED
                target3_14.setAutoDraw(False)
        
        # *target4_14* updates
        
        # if target4_14 is starting this frame...
        if target4_14.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
            # keep track of start time/frame for later
            target4_14.frameNStart = frameN  # exact frame index
            target4_14.tStart = t  # local t and not account for scr refresh
            target4_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target4_14, 'tStartRefresh')  # time at next scr refresh
            # update status
            target4_14.status = STARTED
            target4_14.setAutoDraw(True)
        
        # if target4_14 is active this frame...
        if target4_14.status == STARTED:
            # update params
            pass
        
        # if target4_14 is stopping this frame...
        if target4_14.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 22-frameTolerance:
                # keep track of stop time/frame for later
                target4_14.tStop = t  # not accounting for scr refresh
                target4_14.frameNStop = frameN  # exact frame index
                # update status
                target4_14.status = FINISHED
                target4_14.setAutoDraw(False)
        
        # *target5_14* updates
        
        # if target5_14 is starting this frame...
        if target5_14.status == NOT_STARTED and tThisFlip >= 26-frameTolerance:
            # keep track of start time/frame for later
            target5_14.frameNStart = frameN  # exact frame index
            target5_14.tStart = t  # local t and not account for scr refresh
            target5_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target5_14, 'tStartRefresh')  # time at next scr refresh
            # update status
            target5_14.status = STARTED
            target5_14.setAutoDraw(True)
        
        # if target5_14 is active this frame...
        if target5_14.status == STARTED:
            # update params
            pass
        
        # if target5_14 is stopping this frame...
        if target5_14.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 28-frameTolerance:
                # keep track of stop time/frame for later
                target5_14.tStop = t  # not accounting for scr refresh
                target5_14.frameNStop = frameN  # exact frame index
                # update status
                target5_14.status = FINISHED
                target5_14.setAutoDraw(False)
        
        # *target6_14* updates
        
        # if target6_14 is starting this frame...
        if target6_14.status == NOT_STARTED and tThisFlip >= 32-frameTolerance:
            # keep track of start time/frame for later
            target6_14.frameNStart = frameN  # exact frame index
            target6_14.tStart = t  # local t and not account for scr refresh
            target6_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target6_14, 'tStartRefresh')  # time at next scr refresh
            # update status
            target6_14.status = STARTED
            target6_14.setAutoDraw(True)
        
        # if target6_14 is active this frame...
        if target6_14.status == STARTED:
            # update params
            pass
        
        # if target6_14 is stopping this frame...
        if target6_14.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 34-frameTolerance:
                # keep track of stop time/frame for later
                target6_14.tStop = t  # not accounting for scr refresh
                target6_14.frameNStop = frameN  # exact frame index
                # update status
                target6_14.status = FINISHED
                target6_14.setAutoDraw(False)
        
        # *target7_14* updates
        
        # if target7_14 is starting this frame...
        if target7_14.status == NOT_STARTED and tThisFlip >= 38-frameTolerance:
            # keep track of start time/frame for later
            target7_14.frameNStart = frameN  # exact frame index
            target7_14.tStart = t  # local t and not account for scr refresh
            target7_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target7_14, 'tStartRefresh')  # time at next scr refresh
            # update status
            target7_14.status = STARTED
            target7_14.setAutoDraw(True)
        
        # if target7_14 is active this frame...
        if target7_14.status == STARTED:
            # update params
            pass
        
        # if target7_14 is stopping this frame...
        if target7_14.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 40-frameTolerance:
                # keep track of stop time/frame for later
                target7_14.tStop = t  # not accounting for scr refresh
                target7_14.frameNStop = frameN  # exact frame index
                # update status
                target7_14.status = FINISHED
                target7_14.setAutoDraw(False)
        
        # *target8_14* updates
        
        # if target8_14 is starting this frame...
        if target8_14.status == NOT_STARTED and tThisFlip >= 44-frameTolerance:
            # keep track of start time/frame for later
            target8_14.frameNStart = frameN  # exact frame index
            target8_14.tStart = t  # local t and not account for scr refresh
            target8_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target8_14, 'tStartRefresh')  # time at next scr refresh
            # update status
            target8_14.status = STARTED
            target8_14.setAutoDraw(True)
        
        # if target8_14 is active this frame...
        if target8_14.status == STARTED:
            # update params
            pass
        
        # if target8_14 is stopping this frame...
        if target8_14.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 46-frameTolerance:
                # keep track of stop time/frame for later
                target8_14.tStop = t  # not accounting for scr refresh
                target8_14.frameNStop = frameN  # exact frame index
                # update status
                target8_14.status = FINISHED
                target8_14.setAutoDraw(False)
        
        # *target9_14* updates
        
        # if target9_14 is starting this frame...
        if target9_14.status == NOT_STARTED and tThisFlip >= 50-frameTolerance:
            # keep track of start time/frame for later
            target9_14.frameNStart = frameN  # exact frame index
            target9_14.tStart = t  # local t and not account for scr refresh
            target9_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target9_14, 'tStartRefresh')  # time at next scr refresh
            # update status
            target9_14.status = STARTED
            target9_14.setAutoDraw(True)
        
        # if target9_14 is active this frame...
        if target9_14.status == STARTED:
            # update params
            pass
        
        # if target9_14 is stopping this frame...
        if target9_14.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 52-frameTolerance:
                # keep track of stop time/frame for later
                target9_14.tStop = t  # not accounting for scr refresh
                target9_14.frameNStop = frameN  # exact frame index
                # update status
                target9_14.status = FINISHED
                target9_14.setAutoDraw(False)
        
        # *target10_14* updates
        
        # if target10_14 is starting this frame...
        if target10_14.status == NOT_STARTED and tThisFlip >= 56-frameTolerance:
            # keep track of start time/frame for later
            target10_14.frameNStart = frameN  # exact frame index
            target10_14.tStart = t  # local t and not account for scr refresh
            target10_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target10_14, 'tStartRefresh')  # time at next scr refresh
            # update status
            target10_14.status = STARTED
            target10_14.setAutoDraw(True)
        
        # if target10_14 is active this frame...
        if target10_14.status == STARTED:
            # update params
            pass
        
        # if target10_14 is stopping this frame...
        if target10_14.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 58-frameTolerance:
                # keep track of stop time/frame for later
                target10_14.tStop = t  # not accounting for scr refresh
                target10_14.frameNStop = frameN  # exact frame index
                # update status
                target10_14.status = FINISHED
                target10_14.setAutoDraw(False)
        
        # *target11_14* updates
        
        # if target11_14 is starting this frame...
        if target11_14.status == NOT_STARTED and tThisFlip >= 62-frameTolerance:
            # keep track of start time/frame for later
            target11_14.frameNStart = frameN  # exact frame index
            target11_14.tStart = t  # local t and not account for scr refresh
            target11_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target11_14, 'tStartRefresh')  # time at next scr refresh
            # update status
            target11_14.status = STARTED
            target11_14.setAutoDraw(True)
        
        # if target11_14 is active this frame...
        if target11_14.status == STARTED:
            # update params
            pass
        
        # if target11_14 is stopping this frame...
        if target11_14.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 64-frameTolerance:
                # keep track of stop time/frame for later
                target11_14.tStop = t  # not accounting for scr refresh
                target11_14.frameNStop = frameN  # exact frame index
                # update status
                target11_14.status = FINISHED
                target11_14.setAutoDraw(False)
        
        # *target12_14* updates
        
        # if target12_14 is starting this frame...
        if target12_14.status == NOT_STARTED and tThisFlip >= 68-frameTolerance:
            # keep track of start time/frame for later
            target12_14.frameNStart = frameN  # exact frame index
            target12_14.tStart = t  # local t and not account for scr refresh
            target12_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target12_14, 'tStartRefresh')  # time at next scr refresh
            # update status
            target12_14.status = STARTED
            target12_14.setAutoDraw(True)
        
        # if target12_14 is active this frame...
        if target12_14.status == STARTED:
            # update params
            pass
        
        # if target12_14 is stopping this frame...
        if target12_14.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 70-frameTolerance:
                # keep track of stop time/frame for later
                target12_14.tStop = t  # not accounting for scr refresh
                target12_14.frameNStop = frameN  # exact frame index
                # update status
                target12_14.status = FINISHED
                target12_14.setAutoDraw(False)
        
        # *target13_14* updates
        
        # if target13_14 is starting this frame...
        if target13_14.status == NOT_STARTED and tThisFlip >= 74-frameTolerance:
            # keep track of start time/frame for later
            target13_14.frameNStart = frameN  # exact frame index
            target13_14.tStart = t  # local t and not account for scr refresh
            target13_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target13_14, 'tStartRefresh')  # time at next scr refresh
            # update status
            target13_14.status = STARTED
            target13_14.setAutoDraw(True)
        
        # if target13_14 is active this frame...
        if target13_14.status == STARTED:
            # update params
            pass
        
        # if target13_14 is stopping this frame...
        if target13_14.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 76-frameTolerance:
                # keep track of stop time/frame for later
                target13_14.tStop = t  # not accounting for scr refresh
                target13_14.frameNStop = frameN  # exact frame index
                # update status
                target13_14.status = FINISHED
                target13_14.setAutoDraw(False)
        
        # *target14_14* updates
        
        # if target14_14 is starting this frame...
        if target14_14.status == NOT_STARTED and tThisFlip >= 80-frameTolerance:
            # keep track of start time/frame for later
            target14_14.frameNStart = frameN  # exact frame index
            target14_14.tStart = t  # local t and not account for scr refresh
            target14_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target14_14, 'tStartRefresh')  # time at next scr refresh
            # update status
            target14_14.status = STARTED
            target14_14.setAutoDraw(True)
        
        # if target14_14 is active this frame...
        if target14_14.status == STARTED:
            # update params
            pass
        
        # if target14_14 is stopping this frame...
        if target14_14.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 82-frameTolerance:
                # keep track of stop time/frame for later
                target14_14.tStop = t  # not accounting for scr refresh
                target14_14.frameNStop = frameN  # exact frame index
                # update status
                target14_14.status = FINISHED
                target14_14.setAutoDraw(False)
        
        # *target15_14* updates
        
        # if target15_14 is starting this frame...
        if target15_14.status == NOT_STARTED and tThisFlip >= 86-frameTolerance:
            # keep track of start time/frame for later
            target15_14.frameNStart = frameN  # exact frame index
            target15_14.tStart = t  # local t and not account for scr refresh
            target15_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target15_14, 'tStartRefresh')  # time at next scr refresh
            # update status
            target15_14.status = STARTED
            target15_14.setAutoDraw(True)
        
        # if target15_14 is active this frame...
        if target15_14.status == STARTED:
            # update params
            pass
        
        # if target15_14 is stopping this frame...
        if target15_14.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 88-frameTolerance:
                # keep track of stop time/frame for later
                target15_14.tStop = t  # not accounting for scr refresh
                target15_14.frameNStop = frameN  # exact frame index
                # update status
                target15_14.status = FINISHED
                target15_14.setAutoDraw(False)
        
        # *target16_14* updates
        
        # if target16_14 is starting this frame...
        if target16_14.status == NOT_STARTED and tThisFlip >= 92-frameTolerance:
            # keep track of start time/frame for later
            target16_14.frameNStart = frameN  # exact frame index
            target16_14.tStart = t  # local t and not account for scr refresh
            target16_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target16_14, 'tStartRefresh')  # time at next scr refresh
            # update status
            target16_14.status = STARTED
            target16_14.setAutoDraw(True)
        
        # if target16_14 is active this frame...
        if target16_14.status == STARTED:
            # update params
            pass
        
        # if target16_14 is stopping this frame...
        if target16_14.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 94-frameTolerance:
                # keep track of stop time/frame for later
                target16_14.tStop = t  # not accounting for scr refresh
                target16_14.frameNStop = frameN  # exact frame index
                # update status
                target16_14.status = FINISHED
                target16_14.setAutoDraw(False)
        
        # *target17_14* updates
        
        # if target17_14 is starting this frame...
        if target17_14.status == NOT_STARTED and tThisFlip >= 98-frameTolerance:
            # keep track of start time/frame for later
            target17_14.frameNStart = frameN  # exact frame index
            target17_14.tStart = t  # local t and not account for scr refresh
            target17_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target17_14, 'tStartRefresh')  # time at next scr refresh
            # update status
            target17_14.status = STARTED
            target17_14.setAutoDraw(True)
        
        # if target17_14 is active this frame...
        if target17_14.status == STARTED:
            # update params
            pass
        
        # if target17_14 is stopping this frame...
        if target17_14.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 100-frameTolerance:
                # keep track of stop time/frame for later
                target17_14.tStop = t  # not accounting for scr refresh
                target17_14.frameNStop = frameN  # exact frame index
                # update status
                target17_14.status = FINISHED
                target17_14.setAutoDraw(False)
        
        # *target18_14* updates
        
        # if target18_14 is starting this frame...
        if target18_14.status == NOT_STARTED and tThisFlip >= 104-frameTolerance:
            # keep track of start time/frame for later
            target18_14.frameNStart = frameN  # exact frame index
            target18_14.tStart = t  # local t and not account for scr refresh
            target18_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target18_14, 'tStartRefresh')  # time at next scr refresh
            # update status
            target18_14.status = STARTED
            target18_14.setAutoDraw(True)
        
        # if target18_14 is active this frame...
        if target18_14.status == STARTED:
            # update params
            pass
        
        # if target18_14 is stopping this frame...
        if target18_14.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 106-frameTolerance:
                # keep track of stop time/frame for later
                target18_14.tStop = t  # not accounting for scr refresh
                target18_14.frameNStop = frameN  # exact frame index
                # update status
                target18_14.status = FINISHED
                target18_14.setAutoDraw(False)
        
        # *target19_14* updates
        
        # if target19_14 is starting this frame...
        if target19_14.status == NOT_STARTED and tThisFlip >= 110-frameTolerance:
            # keep track of start time/frame for later
            target19_14.frameNStart = frameN  # exact frame index
            target19_14.tStart = t  # local t and not account for scr refresh
            target19_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target19_14, 'tStartRefresh')  # time at next scr refresh
            # update status
            target19_14.status = STARTED
            target19_14.setAutoDraw(True)
        
        # if target19_14 is active this frame...
        if target19_14.status == STARTED:
            # update params
            pass
        
        # if target19_14 is stopping this frame...
        if target19_14.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 112-frameTolerance:
                # keep track of stop time/frame for later
                target19_14.tStop = t  # not accounting for scr refresh
                target19_14.frameNStop = frameN  # exact frame index
                # update status
                target19_14.status = FINISHED
                target19_14.setAutoDraw(False)
        
        # *target20_14* updates
        
        # if target20_14 is starting this frame...
        if target20_14.status == NOT_STARTED and tThisFlip >= 116-frameTolerance:
            # keep track of start time/frame for later
            target20_14.frameNStart = frameN  # exact frame index
            target20_14.tStart = t  # local t and not account for scr refresh
            target20_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target20_14, 'tStartRefresh')  # time at next scr refresh
            # update status
            target20_14.status = STARTED
            target20_14.setAutoDraw(True)
        
        # if target20_14 is active this frame...
        if target20_14.status == STARTED:
            # update params
            pass
        
        # if target20_14 is stopping this frame...
        if target20_14.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 118-frameTolerance:
                # keep track of stop time/frame for later
                target20_14.tStop = t  # not accounting for scr refresh
                target20_14.frameNStop = frameN  # exact frame index
                # update status
                target20_14.status = FINISHED
                target20_14.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial6" ---
    for thisComponent in trial6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('trial6.stopped', globalClock.getTime())
    sound_22.pause()  # ensure sound has stopped at end of Routine
    # check responses
    if key_resp_46.keys in ['', [], None]:  # No response was made
        key_resp_46.keys = None
    thisExp.addData('key_resp_46.keys',key_resp_46.keys)
    if key_resp_46.keys != None:  # we had a response
        thisExp.addData('key_resp_46.rt', key_resp_46.rt)
        thisExp.addData('key_resp_46.duration', key_resp_46.duration)
    thisExp.nextEntry()
    # the Routine "trial6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "c1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('c1.started', globalClock.getTime())
    slider_1.reset()
    # keep track of which components have finished
    c1Components = [slider_1, text_4]
    for thisComponent in c1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "c1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 15.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 15-frameTolerance:
            continueRoutine = False
        
        # *slider_1* updates
        
        # if slider_1 is starting this frame...
        if slider_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_1.frameNStart = frameN  # exact frame index
            slider_1.tStart = t  # local t and not account for scr refresh
            slider_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider_1.started')
            # update status
            slider_1.status = STARTED
            slider_1.setAutoDraw(True)
        
        # if slider_1 is active this frame...
        if slider_1.status == STARTED:
            # update params
            pass
        
        # if slider_1 is stopping this frame...
        if slider_1.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 15-frameTolerance:
                # keep track of stop time/frame for later
                slider_1.tStop = t  # not accounting for scr refresh
                slider_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_1.stopped')
                # update status
                slider_1.status = FINISHED
                slider_1.setAutoDraw(False)
        
        # *text_4* updates
        
        # if text_4 is starting this frame...
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_4.status = STARTED
            text_4.setAutoDraw(True)
        
        # if text_4 is active this frame...
        if text_4.status == STARTED:
            # update params
            pass
        
        # if text_4 is stopping this frame...
        if text_4.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 15-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                # update status
                text_4.status = FINISHED
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in c1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "c1" ---
    for thisComponent in c1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('c1.stopped', globalClock.getTime())
    thisExp.addData('slider_1.response', slider_1.getRating())
    thisExp.addData('slider_1.rt', slider_1.getRT())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-15.000000)
    
    # --- Prepare to start Routine "trial7" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('trial7.started', globalClock.getTime())
    sound_24.setSound('C:/Users/fatma/OneDrive/Desktop/IITK BOOKS/Decision Making/DM Project/Stimulus/task_sound_stimulus/t7.ogg.opus', hamming=True)
    sound_24.setVolume(1.0, log=False)
    sound_24.seek(0)
    key_resp_48.keys = []
    key_resp_48.rt = []
    _key_resp_48_allKeys = []
    # keep track of which components have finished
    trial7Components = [sound_24, key_resp_48, target_16, target2_16, target3_16, target4_16, target5_16, target6_16, target7_16, target8_16, target9_16, target10_16, target11_16, target12_16, target13_16, target14_16, target15_16, target16_16, target17_16, target18_16, target19_16, target20_16]
    for thisComponent in trial7Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial7" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 120-frameTolerance:
            continueRoutine = False
        
        # if sound_24 is starting this frame...
        if sound_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_24.frameNStart = frameN  # exact frame index
            sound_24.tStart = t  # local t and not account for scr refresh
            sound_24.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_24.started', tThisFlipGlobal)
            # update status
            sound_24.status = STARTED
            sound_24.play(when=win)  # sync with win flip
        # update sound_24 status according to whether it's playing
        if sound_24.isPlaying:
            sound_24.status = STARTED
        elif sound_24.isFinished:
            sound_24.status = FINISHED
        
        # *key_resp_48* updates
        waitOnFlip = False
        
        # if key_resp_48 is starting this frame...
        if key_resp_48.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_48.frameNStart = frameN  # exact frame index
            key_resp_48.tStart = t  # local t and not account for scr refresh
            key_resp_48.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_48, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_48.started')
            # update status
            key_resp_48.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_48.clock.reset)  # t=0 on next screen flip
        
        # if key_resp_48 is stopping this frame...
        if key_resp_48.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 120-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_48.tStop = t  # not accounting for scr refresh
                key_resp_48.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_48.stopped')
                # update status
                key_resp_48.status = FINISHED
                key_resp_48.status = FINISHED
        if key_resp_48.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_48.getKeys(keyList=['left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_48_allKeys.extend(theseKeys)
            if len(_key_resp_48_allKeys):
                key_resp_48.keys = [key.name for key in _key_resp_48_allKeys]  # storing all keys
                key_resp_48.rt = [key.rt for key in _key_resp_48_allKeys]
                key_resp_48.duration = [key.duration for key in _key_resp_48_allKeys]
        
        # *target_16* updates
        
        # if target_16 is starting this frame...
        if target_16.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            target_16.frameNStart = frameN  # exact frame index
            target_16.tStart = t  # local t and not account for scr refresh
            target_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target_16.started')
            # update status
            target_16.status = STARTED
            target_16.setAutoDraw(True)
        
        # if target_16 is active this frame...
        if target_16.status == STARTED:
            # update params
            pass
        
        # if target_16 is stopping this frame...
        if target_16.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4-frameTolerance:
                # keep track of stop time/frame for later
                target_16.tStop = t  # not accounting for scr refresh
                target_16.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target_16.stopped')
                # update status
                target_16.status = FINISHED
                target_16.setAutoDraw(False)
        
        # *target2_16* updates
        
        # if target2_16 is starting this frame...
        if target2_16.status == NOT_STARTED and tThisFlip >= 8-frameTolerance:
            # keep track of start time/frame for later
            target2_16.frameNStart = frameN  # exact frame index
            target2_16.tStart = t  # local t and not account for scr refresh
            target2_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target2_16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target2_16.started')
            # update status
            target2_16.status = STARTED
            target2_16.setAutoDraw(True)
        
        # if target2_16 is active this frame...
        if target2_16.status == STARTED:
            # update params
            pass
        
        # if target2_16 is stopping this frame...
        if target2_16.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 10-frameTolerance:
                # keep track of stop time/frame for later
                target2_16.tStop = t  # not accounting for scr refresh
                target2_16.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target2_16.stopped')
                # update status
                target2_16.status = FINISHED
                target2_16.setAutoDraw(False)
        
        # *target3_16* updates
        
        # if target3_16 is starting this frame...
        if target3_16.status == NOT_STARTED and tThisFlip >= 14-frameTolerance:
            # keep track of start time/frame for later
            target3_16.frameNStart = frameN  # exact frame index
            target3_16.tStart = t  # local t and not account for scr refresh
            target3_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target3_16, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target3_16.started')
            # update status
            target3_16.status = STARTED
            target3_16.setAutoDraw(True)
        
        # if target3_16 is active this frame...
        if target3_16.status == STARTED:
            # update params
            pass
        
        # if target3_16 is stopping this frame...
        if target3_16.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 16-frameTolerance:
                # keep track of stop time/frame for later
                target3_16.tStop = t  # not accounting for scr refresh
                target3_16.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target3_16.stopped')
                # update status
                target3_16.status = FINISHED
                target3_16.setAutoDraw(False)
        
        # *target4_16* updates
        
        # if target4_16 is starting this frame...
        if target4_16.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
            # keep track of start time/frame for later
            target4_16.frameNStart = frameN  # exact frame index
            target4_16.tStart = t  # local t and not account for scr refresh
            target4_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target4_16, 'tStartRefresh')  # time at next scr refresh
            # update status
            target4_16.status = STARTED
            target4_16.setAutoDraw(True)
        
        # if target4_16 is active this frame...
        if target4_16.status == STARTED:
            # update params
            pass
        
        # if target4_16 is stopping this frame...
        if target4_16.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 22-frameTolerance:
                # keep track of stop time/frame for later
                target4_16.tStop = t  # not accounting for scr refresh
                target4_16.frameNStop = frameN  # exact frame index
                # update status
                target4_16.status = FINISHED
                target4_16.setAutoDraw(False)
        
        # *target5_16* updates
        
        # if target5_16 is starting this frame...
        if target5_16.status == NOT_STARTED and tThisFlip >= 26-frameTolerance:
            # keep track of start time/frame for later
            target5_16.frameNStart = frameN  # exact frame index
            target5_16.tStart = t  # local t and not account for scr refresh
            target5_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target5_16, 'tStartRefresh')  # time at next scr refresh
            # update status
            target5_16.status = STARTED
            target5_16.setAutoDraw(True)
        
        # if target5_16 is active this frame...
        if target5_16.status == STARTED:
            # update params
            pass
        
        # if target5_16 is stopping this frame...
        if target5_16.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 28-frameTolerance:
                # keep track of stop time/frame for later
                target5_16.tStop = t  # not accounting for scr refresh
                target5_16.frameNStop = frameN  # exact frame index
                # update status
                target5_16.status = FINISHED
                target5_16.setAutoDraw(False)
        
        # *target6_16* updates
        
        # if target6_16 is starting this frame...
        if target6_16.status == NOT_STARTED and tThisFlip >= 32-frameTolerance:
            # keep track of start time/frame for later
            target6_16.frameNStart = frameN  # exact frame index
            target6_16.tStart = t  # local t and not account for scr refresh
            target6_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target6_16, 'tStartRefresh')  # time at next scr refresh
            # update status
            target6_16.status = STARTED
            target6_16.setAutoDraw(True)
        
        # if target6_16 is active this frame...
        if target6_16.status == STARTED:
            # update params
            pass
        
        # if target6_16 is stopping this frame...
        if target6_16.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 34-frameTolerance:
                # keep track of stop time/frame for later
                target6_16.tStop = t  # not accounting for scr refresh
                target6_16.frameNStop = frameN  # exact frame index
                # update status
                target6_16.status = FINISHED
                target6_16.setAutoDraw(False)
        
        # *target7_16* updates
        
        # if target7_16 is starting this frame...
        if target7_16.status == NOT_STARTED and tThisFlip >= 38-frameTolerance:
            # keep track of start time/frame for later
            target7_16.frameNStart = frameN  # exact frame index
            target7_16.tStart = t  # local t and not account for scr refresh
            target7_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target7_16, 'tStartRefresh')  # time at next scr refresh
            # update status
            target7_16.status = STARTED
            target7_16.setAutoDraw(True)
        
        # if target7_16 is active this frame...
        if target7_16.status == STARTED:
            # update params
            pass
        
        # if target7_16 is stopping this frame...
        if target7_16.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 40-frameTolerance:
                # keep track of stop time/frame for later
                target7_16.tStop = t  # not accounting for scr refresh
                target7_16.frameNStop = frameN  # exact frame index
                # update status
                target7_16.status = FINISHED
                target7_16.setAutoDraw(False)
        
        # *target8_16* updates
        
        # if target8_16 is starting this frame...
        if target8_16.status == NOT_STARTED and tThisFlip >= 44-frameTolerance:
            # keep track of start time/frame for later
            target8_16.frameNStart = frameN  # exact frame index
            target8_16.tStart = t  # local t and not account for scr refresh
            target8_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target8_16, 'tStartRefresh')  # time at next scr refresh
            # update status
            target8_16.status = STARTED
            target8_16.setAutoDraw(True)
        
        # if target8_16 is active this frame...
        if target8_16.status == STARTED:
            # update params
            pass
        
        # if target8_16 is stopping this frame...
        if target8_16.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 46-frameTolerance:
                # keep track of stop time/frame for later
                target8_16.tStop = t  # not accounting for scr refresh
                target8_16.frameNStop = frameN  # exact frame index
                # update status
                target8_16.status = FINISHED
                target8_16.setAutoDraw(False)
        
        # *target9_16* updates
        
        # if target9_16 is starting this frame...
        if target9_16.status == NOT_STARTED and tThisFlip >= 50-frameTolerance:
            # keep track of start time/frame for later
            target9_16.frameNStart = frameN  # exact frame index
            target9_16.tStart = t  # local t and not account for scr refresh
            target9_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target9_16, 'tStartRefresh')  # time at next scr refresh
            # update status
            target9_16.status = STARTED
            target9_16.setAutoDraw(True)
        
        # if target9_16 is active this frame...
        if target9_16.status == STARTED:
            # update params
            pass
        
        # if target9_16 is stopping this frame...
        if target9_16.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 52-frameTolerance:
                # keep track of stop time/frame for later
                target9_16.tStop = t  # not accounting for scr refresh
                target9_16.frameNStop = frameN  # exact frame index
                # update status
                target9_16.status = FINISHED
                target9_16.setAutoDraw(False)
        
        # *target10_16* updates
        
        # if target10_16 is starting this frame...
        if target10_16.status == NOT_STARTED and tThisFlip >= 56-frameTolerance:
            # keep track of start time/frame for later
            target10_16.frameNStart = frameN  # exact frame index
            target10_16.tStart = t  # local t and not account for scr refresh
            target10_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target10_16, 'tStartRefresh')  # time at next scr refresh
            # update status
            target10_16.status = STARTED
            target10_16.setAutoDraw(True)
        
        # if target10_16 is active this frame...
        if target10_16.status == STARTED:
            # update params
            pass
        
        # if target10_16 is stopping this frame...
        if target10_16.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 58-frameTolerance:
                # keep track of stop time/frame for later
                target10_16.tStop = t  # not accounting for scr refresh
                target10_16.frameNStop = frameN  # exact frame index
                # update status
                target10_16.status = FINISHED
                target10_16.setAutoDraw(False)
        
        # *target11_16* updates
        
        # if target11_16 is starting this frame...
        if target11_16.status == NOT_STARTED and tThisFlip >= 62-frameTolerance:
            # keep track of start time/frame for later
            target11_16.frameNStart = frameN  # exact frame index
            target11_16.tStart = t  # local t and not account for scr refresh
            target11_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target11_16, 'tStartRefresh')  # time at next scr refresh
            # update status
            target11_16.status = STARTED
            target11_16.setAutoDraw(True)
        
        # if target11_16 is active this frame...
        if target11_16.status == STARTED:
            # update params
            pass
        
        # if target11_16 is stopping this frame...
        if target11_16.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 64-frameTolerance:
                # keep track of stop time/frame for later
                target11_16.tStop = t  # not accounting for scr refresh
                target11_16.frameNStop = frameN  # exact frame index
                # update status
                target11_16.status = FINISHED
                target11_16.setAutoDraw(False)
        
        # *target12_16* updates
        
        # if target12_16 is starting this frame...
        if target12_16.status == NOT_STARTED and tThisFlip >= 68-frameTolerance:
            # keep track of start time/frame for later
            target12_16.frameNStart = frameN  # exact frame index
            target12_16.tStart = t  # local t and not account for scr refresh
            target12_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target12_16, 'tStartRefresh')  # time at next scr refresh
            # update status
            target12_16.status = STARTED
            target12_16.setAutoDraw(True)
        
        # if target12_16 is active this frame...
        if target12_16.status == STARTED:
            # update params
            pass
        
        # if target12_16 is stopping this frame...
        if target12_16.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 70-frameTolerance:
                # keep track of stop time/frame for later
                target12_16.tStop = t  # not accounting for scr refresh
                target12_16.frameNStop = frameN  # exact frame index
                # update status
                target12_16.status = FINISHED
                target12_16.setAutoDraw(False)
        
        # *target13_16* updates
        
        # if target13_16 is starting this frame...
        if target13_16.status == NOT_STARTED and tThisFlip >= 74-frameTolerance:
            # keep track of start time/frame for later
            target13_16.frameNStart = frameN  # exact frame index
            target13_16.tStart = t  # local t and not account for scr refresh
            target13_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target13_16, 'tStartRefresh')  # time at next scr refresh
            # update status
            target13_16.status = STARTED
            target13_16.setAutoDraw(True)
        
        # if target13_16 is active this frame...
        if target13_16.status == STARTED:
            # update params
            pass
        
        # if target13_16 is stopping this frame...
        if target13_16.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 76-frameTolerance:
                # keep track of stop time/frame for later
                target13_16.tStop = t  # not accounting for scr refresh
                target13_16.frameNStop = frameN  # exact frame index
                # update status
                target13_16.status = FINISHED
                target13_16.setAutoDraw(False)
        
        # *target14_16* updates
        
        # if target14_16 is starting this frame...
        if target14_16.status == NOT_STARTED and tThisFlip >= 80-frameTolerance:
            # keep track of start time/frame for later
            target14_16.frameNStart = frameN  # exact frame index
            target14_16.tStart = t  # local t and not account for scr refresh
            target14_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target14_16, 'tStartRefresh')  # time at next scr refresh
            # update status
            target14_16.status = STARTED
            target14_16.setAutoDraw(True)
        
        # if target14_16 is active this frame...
        if target14_16.status == STARTED:
            # update params
            pass
        
        # if target14_16 is stopping this frame...
        if target14_16.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 82-frameTolerance:
                # keep track of stop time/frame for later
                target14_16.tStop = t  # not accounting for scr refresh
                target14_16.frameNStop = frameN  # exact frame index
                # update status
                target14_16.status = FINISHED
                target14_16.setAutoDraw(False)
        
        # *target15_16* updates
        
        # if target15_16 is starting this frame...
        if target15_16.status == NOT_STARTED and tThisFlip >= 86-frameTolerance:
            # keep track of start time/frame for later
            target15_16.frameNStart = frameN  # exact frame index
            target15_16.tStart = t  # local t and not account for scr refresh
            target15_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target15_16, 'tStartRefresh')  # time at next scr refresh
            # update status
            target15_16.status = STARTED
            target15_16.setAutoDraw(True)
        
        # if target15_16 is active this frame...
        if target15_16.status == STARTED:
            # update params
            pass
        
        # if target15_16 is stopping this frame...
        if target15_16.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 88-frameTolerance:
                # keep track of stop time/frame for later
                target15_16.tStop = t  # not accounting for scr refresh
                target15_16.frameNStop = frameN  # exact frame index
                # update status
                target15_16.status = FINISHED
                target15_16.setAutoDraw(False)
        
        # *target16_16* updates
        
        # if target16_16 is starting this frame...
        if target16_16.status == NOT_STARTED and tThisFlip >= 92-frameTolerance:
            # keep track of start time/frame for later
            target16_16.frameNStart = frameN  # exact frame index
            target16_16.tStart = t  # local t and not account for scr refresh
            target16_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target16_16, 'tStartRefresh')  # time at next scr refresh
            # update status
            target16_16.status = STARTED
            target16_16.setAutoDraw(True)
        
        # if target16_16 is active this frame...
        if target16_16.status == STARTED:
            # update params
            pass
        
        # if target16_16 is stopping this frame...
        if target16_16.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 94-frameTolerance:
                # keep track of stop time/frame for later
                target16_16.tStop = t  # not accounting for scr refresh
                target16_16.frameNStop = frameN  # exact frame index
                # update status
                target16_16.status = FINISHED
                target16_16.setAutoDraw(False)
        
        # *target17_16* updates
        
        # if target17_16 is starting this frame...
        if target17_16.status == NOT_STARTED and tThisFlip >= 98-frameTolerance:
            # keep track of start time/frame for later
            target17_16.frameNStart = frameN  # exact frame index
            target17_16.tStart = t  # local t and not account for scr refresh
            target17_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target17_16, 'tStartRefresh')  # time at next scr refresh
            # update status
            target17_16.status = STARTED
            target17_16.setAutoDraw(True)
        
        # if target17_16 is active this frame...
        if target17_16.status == STARTED:
            # update params
            pass
        
        # if target17_16 is stopping this frame...
        if target17_16.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 100-frameTolerance:
                # keep track of stop time/frame for later
                target17_16.tStop = t  # not accounting for scr refresh
                target17_16.frameNStop = frameN  # exact frame index
                # update status
                target17_16.status = FINISHED
                target17_16.setAutoDraw(False)
        
        # *target18_16* updates
        
        # if target18_16 is starting this frame...
        if target18_16.status == NOT_STARTED and tThisFlip >= 104-frameTolerance:
            # keep track of start time/frame for later
            target18_16.frameNStart = frameN  # exact frame index
            target18_16.tStart = t  # local t and not account for scr refresh
            target18_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target18_16, 'tStartRefresh')  # time at next scr refresh
            # update status
            target18_16.status = STARTED
            target18_16.setAutoDraw(True)
        
        # if target18_16 is active this frame...
        if target18_16.status == STARTED:
            # update params
            pass
        
        # if target18_16 is stopping this frame...
        if target18_16.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 106-frameTolerance:
                # keep track of stop time/frame for later
                target18_16.tStop = t  # not accounting for scr refresh
                target18_16.frameNStop = frameN  # exact frame index
                # update status
                target18_16.status = FINISHED
                target18_16.setAutoDraw(False)
        
        # *target19_16* updates
        
        # if target19_16 is starting this frame...
        if target19_16.status == NOT_STARTED and tThisFlip >= 110-frameTolerance:
            # keep track of start time/frame for later
            target19_16.frameNStart = frameN  # exact frame index
            target19_16.tStart = t  # local t and not account for scr refresh
            target19_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target19_16, 'tStartRefresh')  # time at next scr refresh
            # update status
            target19_16.status = STARTED
            target19_16.setAutoDraw(True)
        
        # if target19_16 is active this frame...
        if target19_16.status == STARTED:
            # update params
            pass
        
        # if target19_16 is stopping this frame...
        if target19_16.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 112-frameTolerance:
                # keep track of stop time/frame for later
                target19_16.tStop = t  # not accounting for scr refresh
                target19_16.frameNStop = frameN  # exact frame index
                # update status
                target19_16.status = FINISHED
                target19_16.setAutoDraw(False)
        
        # *target20_16* updates
        
        # if target20_16 is starting this frame...
        if target20_16.status == NOT_STARTED and tThisFlip >= 116-frameTolerance:
            # keep track of start time/frame for later
            target20_16.frameNStart = frameN  # exact frame index
            target20_16.tStart = t  # local t and not account for scr refresh
            target20_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target20_16, 'tStartRefresh')  # time at next scr refresh
            # update status
            target20_16.status = STARTED
            target20_16.setAutoDraw(True)
        
        # if target20_16 is active this frame...
        if target20_16.status == STARTED:
            # update params
            pass
        
        # if target20_16 is stopping this frame...
        if target20_16.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 118-frameTolerance:
                # keep track of stop time/frame for later
                target20_16.tStop = t  # not accounting for scr refresh
                target20_16.frameNStop = frameN  # exact frame index
                # update status
                target20_16.status = FINISHED
                target20_16.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial7Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial7" ---
    for thisComponent in trial7Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('trial7.stopped', globalClock.getTime())
    sound_24.pause()  # ensure sound has stopped at end of Routine
    # check responses
    if key_resp_48.keys in ['', [], None]:  # No response was made
        key_resp_48.keys = None
    thisExp.addData('key_resp_48.keys',key_resp_48.keys)
    if key_resp_48.keys != None:  # we had a response
        thisExp.addData('key_resp_48.rt', key_resp_48.rt)
        thisExp.addData('key_resp_48.duration', key_resp_48.duration)
    thisExp.nextEntry()
    # the Routine "trial7" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "c1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('c1.started', globalClock.getTime())
    slider_1.reset()
    # keep track of which components have finished
    c1Components = [slider_1, text_4]
    for thisComponent in c1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "c1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 15.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 15-frameTolerance:
            continueRoutine = False
        
        # *slider_1* updates
        
        # if slider_1 is starting this frame...
        if slider_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_1.frameNStart = frameN  # exact frame index
            slider_1.tStart = t  # local t and not account for scr refresh
            slider_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider_1.started')
            # update status
            slider_1.status = STARTED
            slider_1.setAutoDraw(True)
        
        # if slider_1 is active this frame...
        if slider_1.status == STARTED:
            # update params
            pass
        
        # if slider_1 is stopping this frame...
        if slider_1.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 15-frameTolerance:
                # keep track of stop time/frame for later
                slider_1.tStop = t  # not accounting for scr refresh
                slider_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_1.stopped')
                # update status
                slider_1.status = FINISHED
                slider_1.setAutoDraw(False)
        
        # *text_4* updates
        
        # if text_4 is starting this frame...
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_4.status = STARTED
            text_4.setAutoDraw(True)
        
        # if text_4 is active this frame...
        if text_4.status == STARTED:
            # update params
            pass
        
        # if text_4 is stopping this frame...
        if text_4.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 15-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                # update status
                text_4.status = FINISHED
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in c1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "c1" ---
    for thisComponent in c1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('c1.stopped', globalClock.getTime())
    thisExp.addData('slider_1.response', slider_1.getRating())
    thisExp.addData('slider_1.rt', slider_1.getRT())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-15.000000)
    
    # --- Prepare to start Routine "trial8" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('trial8.started', globalClock.getTime())
    sound_25.setSound('C:/Users/fatma/OneDrive/Desktop/IITK BOOKS/Decision Making/DM Project/Stimulus/task_sound_stimulus/t8.ogg.opus', hamming=True)
    sound_25.setVolume(1.0, log=False)
    sound_25.seek(0)
    key_resp_49.keys = []
    key_resp_49.rt = []
    _key_resp_49_allKeys = []
    # keep track of which components have finished
    trial8Components = [sound_25, key_resp_49, target_17, target2_17, target3_17, target4_17, target5_17, target6_17, target7_17, target8_17, target9_17, target10_17, target11_17, target12_17, target13_17, target14_17, target15_17, target16_17, target17_17, target18_17, target19_17, target20_17]
    for thisComponent in trial8Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial8" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 120-frameTolerance:
            continueRoutine = False
        
        # if sound_25 is starting this frame...
        if sound_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_25.frameNStart = frameN  # exact frame index
            sound_25.tStart = t  # local t and not account for scr refresh
            sound_25.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_25.started', tThisFlipGlobal)
            # update status
            sound_25.status = STARTED
            sound_25.play(when=win)  # sync with win flip
        # update sound_25 status according to whether it's playing
        if sound_25.isPlaying:
            sound_25.status = STARTED
        elif sound_25.isFinished:
            sound_25.status = FINISHED
        
        # *key_resp_49* updates
        waitOnFlip = False
        
        # if key_resp_49 is starting this frame...
        if key_resp_49.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_49.frameNStart = frameN  # exact frame index
            key_resp_49.tStart = t  # local t and not account for scr refresh
            key_resp_49.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_49, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_49.started')
            # update status
            key_resp_49.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_49.clock.reset)  # t=0 on next screen flip
        
        # if key_resp_49 is stopping this frame...
        if key_resp_49.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 120-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_49.tStop = t  # not accounting for scr refresh
                key_resp_49.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_49.stopped')
                # update status
                key_resp_49.status = FINISHED
                key_resp_49.status = FINISHED
        if key_resp_49.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_49.getKeys(keyList=['left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_49_allKeys.extend(theseKeys)
            if len(_key_resp_49_allKeys):
                key_resp_49.keys = [key.name for key in _key_resp_49_allKeys]  # storing all keys
                key_resp_49.rt = [key.rt for key in _key_resp_49_allKeys]
                key_resp_49.duration = [key.duration for key in _key_resp_49_allKeys]
        
        # *target_17* updates
        
        # if target_17 is starting this frame...
        if target_17.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            target_17.frameNStart = frameN  # exact frame index
            target_17.tStart = t  # local t and not account for scr refresh
            target_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_17, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target_17.started')
            # update status
            target_17.status = STARTED
            target_17.setAutoDraw(True)
        
        # if target_17 is active this frame...
        if target_17.status == STARTED:
            # update params
            pass
        
        # if target_17 is stopping this frame...
        if target_17.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4-frameTolerance:
                # keep track of stop time/frame for later
                target_17.tStop = t  # not accounting for scr refresh
                target_17.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target_17.stopped')
                # update status
                target_17.status = FINISHED
                target_17.setAutoDraw(False)
        
        # *target2_17* updates
        
        # if target2_17 is starting this frame...
        if target2_17.status == NOT_STARTED and tThisFlip >= 8-frameTolerance:
            # keep track of start time/frame for later
            target2_17.frameNStart = frameN  # exact frame index
            target2_17.tStart = t  # local t and not account for scr refresh
            target2_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target2_17, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target2_17.started')
            # update status
            target2_17.status = STARTED
            target2_17.setAutoDraw(True)
        
        # if target2_17 is active this frame...
        if target2_17.status == STARTED:
            # update params
            pass
        
        # if target2_17 is stopping this frame...
        if target2_17.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 10-frameTolerance:
                # keep track of stop time/frame for later
                target2_17.tStop = t  # not accounting for scr refresh
                target2_17.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target2_17.stopped')
                # update status
                target2_17.status = FINISHED
                target2_17.setAutoDraw(False)
        
        # *target3_17* updates
        
        # if target3_17 is starting this frame...
        if target3_17.status == NOT_STARTED and tThisFlip >= 14-frameTolerance:
            # keep track of start time/frame for later
            target3_17.frameNStart = frameN  # exact frame index
            target3_17.tStart = t  # local t and not account for scr refresh
            target3_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target3_17, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target3_17.started')
            # update status
            target3_17.status = STARTED
            target3_17.setAutoDraw(True)
        
        # if target3_17 is active this frame...
        if target3_17.status == STARTED:
            # update params
            pass
        
        # if target3_17 is stopping this frame...
        if target3_17.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 16-frameTolerance:
                # keep track of stop time/frame for later
                target3_17.tStop = t  # not accounting for scr refresh
                target3_17.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target3_17.stopped')
                # update status
                target3_17.status = FINISHED
                target3_17.setAutoDraw(False)
        
        # *target4_17* updates
        
        # if target4_17 is starting this frame...
        if target4_17.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
            # keep track of start time/frame for later
            target4_17.frameNStart = frameN  # exact frame index
            target4_17.tStart = t  # local t and not account for scr refresh
            target4_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target4_17, 'tStartRefresh')  # time at next scr refresh
            # update status
            target4_17.status = STARTED
            target4_17.setAutoDraw(True)
        
        # if target4_17 is active this frame...
        if target4_17.status == STARTED:
            # update params
            pass
        
        # if target4_17 is stopping this frame...
        if target4_17.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 22-frameTolerance:
                # keep track of stop time/frame for later
                target4_17.tStop = t  # not accounting for scr refresh
                target4_17.frameNStop = frameN  # exact frame index
                # update status
                target4_17.status = FINISHED
                target4_17.setAutoDraw(False)
        
        # *target5_17* updates
        
        # if target5_17 is starting this frame...
        if target5_17.status == NOT_STARTED and tThisFlip >= 26-frameTolerance:
            # keep track of start time/frame for later
            target5_17.frameNStart = frameN  # exact frame index
            target5_17.tStart = t  # local t and not account for scr refresh
            target5_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target5_17, 'tStartRefresh')  # time at next scr refresh
            # update status
            target5_17.status = STARTED
            target5_17.setAutoDraw(True)
        
        # if target5_17 is active this frame...
        if target5_17.status == STARTED:
            # update params
            pass
        
        # if target5_17 is stopping this frame...
        if target5_17.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 28-frameTolerance:
                # keep track of stop time/frame for later
                target5_17.tStop = t  # not accounting for scr refresh
                target5_17.frameNStop = frameN  # exact frame index
                # update status
                target5_17.status = FINISHED
                target5_17.setAutoDraw(False)
        
        # *target6_17* updates
        
        # if target6_17 is starting this frame...
        if target6_17.status == NOT_STARTED and tThisFlip >= 32-frameTolerance:
            # keep track of start time/frame for later
            target6_17.frameNStart = frameN  # exact frame index
            target6_17.tStart = t  # local t and not account for scr refresh
            target6_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target6_17, 'tStartRefresh')  # time at next scr refresh
            # update status
            target6_17.status = STARTED
            target6_17.setAutoDraw(True)
        
        # if target6_17 is active this frame...
        if target6_17.status == STARTED:
            # update params
            pass
        
        # if target6_17 is stopping this frame...
        if target6_17.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 34-frameTolerance:
                # keep track of stop time/frame for later
                target6_17.tStop = t  # not accounting for scr refresh
                target6_17.frameNStop = frameN  # exact frame index
                # update status
                target6_17.status = FINISHED
                target6_17.setAutoDraw(False)
        
        # *target7_17* updates
        
        # if target7_17 is starting this frame...
        if target7_17.status == NOT_STARTED and tThisFlip >= 38-frameTolerance:
            # keep track of start time/frame for later
            target7_17.frameNStart = frameN  # exact frame index
            target7_17.tStart = t  # local t and not account for scr refresh
            target7_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target7_17, 'tStartRefresh')  # time at next scr refresh
            # update status
            target7_17.status = STARTED
            target7_17.setAutoDraw(True)
        
        # if target7_17 is active this frame...
        if target7_17.status == STARTED:
            # update params
            pass
        
        # if target7_17 is stopping this frame...
        if target7_17.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 40-frameTolerance:
                # keep track of stop time/frame for later
                target7_17.tStop = t  # not accounting for scr refresh
                target7_17.frameNStop = frameN  # exact frame index
                # update status
                target7_17.status = FINISHED
                target7_17.setAutoDraw(False)
        
        # *target8_17* updates
        
        # if target8_17 is starting this frame...
        if target8_17.status == NOT_STARTED and tThisFlip >= 44-frameTolerance:
            # keep track of start time/frame for later
            target8_17.frameNStart = frameN  # exact frame index
            target8_17.tStart = t  # local t and not account for scr refresh
            target8_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target8_17, 'tStartRefresh')  # time at next scr refresh
            # update status
            target8_17.status = STARTED
            target8_17.setAutoDraw(True)
        
        # if target8_17 is active this frame...
        if target8_17.status == STARTED:
            # update params
            pass
        
        # if target8_17 is stopping this frame...
        if target8_17.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 46-frameTolerance:
                # keep track of stop time/frame for later
                target8_17.tStop = t  # not accounting for scr refresh
                target8_17.frameNStop = frameN  # exact frame index
                # update status
                target8_17.status = FINISHED
                target8_17.setAutoDraw(False)
        
        # *target9_17* updates
        
        # if target9_17 is starting this frame...
        if target9_17.status == NOT_STARTED and tThisFlip >= 50-frameTolerance:
            # keep track of start time/frame for later
            target9_17.frameNStart = frameN  # exact frame index
            target9_17.tStart = t  # local t and not account for scr refresh
            target9_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target9_17, 'tStartRefresh')  # time at next scr refresh
            # update status
            target9_17.status = STARTED
            target9_17.setAutoDraw(True)
        
        # if target9_17 is active this frame...
        if target9_17.status == STARTED:
            # update params
            pass
        
        # if target9_17 is stopping this frame...
        if target9_17.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 52-frameTolerance:
                # keep track of stop time/frame for later
                target9_17.tStop = t  # not accounting for scr refresh
                target9_17.frameNStop = frameN  # exact frame index
                # update status
                target9_17.status = FINISHED
                target9_17.setAutoDraw(False)
        
        # *target10_17* updates
        
        # if target10_17 is starting this frame...
        if target10_17.status == NOT_STARTED and tThisFlip >= 56-frameTolerance:
            # keep track of start time/frame for later
            target10_17.frameNStart = frameN  # exact frame index
            target10_17.tStart = t  # local t and not account for scr refresh
            target10_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target10_17, 'tStartRefresh')  # time at next scr refresh
            # update status
            target10_17.status = STARTED
            target10_17.setAutoDraw(True)
        
        # if target10_17 is active this frame...
        if target10_17.status == STARTED:
            # update params
            pass
        
        # if target10_17 is stopping this frame...
        if target10_17.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 58-frameTolerance:
                # keep track of stop time/frame for later
                target10_17.tStop = t  # not accounting for scr refresh
                target10_17.frameNStop = frameN  # exact frame index
                # update status
                target10_17.status = FINISHED
                target10_17.setAutoDraw(False)
        
        # *target11_17* updates
        
        # if target11_17 is starting this frame...
        if target11_17.status == NOT_STARTED and tThisFlip >= 62-frameTolerance:
            # keep track of start time/frame for later
            target11_17.frameNStart = frameN  # exact frame index
            target11_17.tStart = t  # local t and not account for scr refresh
            target11_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target11_17, 'tStartRefresh')  # time at next scr refresh
            # update status
            target11_17.status = STARTED
            target11_17.setAutoDraw(True)
        
        # if target11_17 is active this frame...
        if target11_17.status == STARTED:
            # update params
            pass
        
        # if target11_17 is stopping this frame...
        if target11_17.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 64-frameTolerance:
                # keep track of stop time/frame for later
                target11_17.tStop = t  # not accounting for scr refresh
                target11_17.frameNStop = frameN  # exact frame index
                # update status
                target11_17.status = FINISHED
                target11_17.setAutoDraw(False)
        
        # *target12_17* updates
        
        # if target12_17 is starting this frame...
        if target12_17.status == NOT_STARTED and tThisFlip >= 68-frameTolerance:
            # keep track of start time/frame for later
            target12_17.frameNStart = frameN  # exact frame index
            target12_17.tStart = t  # local t and not account for scr refresh
            target12_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target12_17, 'tStartRefresh')  # time at next scr refresh
            # update status
            target12_17.status = STARTED
            target12_17.setAutoDraw(True)
        
        # if target12_17 is active this frame...
        if target12_17.status == STARTED:
            # update params
            pass
        
        # if target12_17 is stopping this frame...
        if target12_17.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 70-frameTolerance:
                # keep track of stop time/frame for later
                target12_17.tStop = t  # not accounting for scr refresh
                target12_17.frameNStop = frameN  # exact frame index
                # update status
                target12_17.status = FINISHED
                target12_17.setAutoDraw(False)
        
        # *target13_17* updates
        
        # if target13_17 is starting this frame...
        if target13_17.status == NOT_STARTED and tThisFlip >= 74-frameTolerance:
            # keep track of start time/frame for later
            target13_17.frameNStart = frameN  # exact frame index
            target13_17.tStart = t  # local t and not account for scr refresh
            target13_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target13_17, 'tStartRefresh')  # time at next scr refresh
            # update status
            target13_17.status = STARTED
            target13_17.setAutoDraw(True)
        
        # if target13_17 is active this frame...
        if target13_17.status == STARTED:
            # update params
            pass
        
        # if target13_17 is stopping this frame...
        if target13_17.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 76-frameTolerance:
                # keep track of stop time/frame for later
                target13_17.tStop = t  # not accounting for scr refresh
                target13_17.frameNStop = frameN  # exact frame index
                # update status
                target13_17.status = FINISHED
                target13_17.setAutoDraw(False)
        
        # *target14_17* updates
        
        # if target14_17 is starting this frame...
        if target14_17.status == NOT_STARTED and tThisFlip >= 80-frameTolerance:
            # keep track of start time/frame for later
            target14_17.frameNStart = frameN  # exact frame index
            target14_17.tStart = t  # local t and not account for scr refresh
            target14_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target14_17, 'tStartRefresh')  # time at next scr refresh
            # update status
            target14_17.status = STARTED
            target14_17.setAutoDraw(True)
        
        # if target14_17 is active this frame...
        if target14_17.status == STARTED:
            # update params
            pass
        
        # if target14_17 is stopping this frame...
        if target14_17.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 82-frameTolerance:
                # keep track of stop time/frame for later
                target14_17.tStop = t  # not accounting for scr refresh
                target14_17.frameNStop = frameN  # exact frame index
                # update status
                target14_17.status = FINISHED
                target14_17.setAutoDraw(False)
        
        # *target15_17* updates
        
        # if target15_17 is starting this frame...
        if target15_17.status == NOT_STARTED and tThisFlip >= 86-frameTolerance:
            # keep track of start time/frame for later
            target15_17.frameNStart = frameN  # exact frame index
            target15_17.tStart = t  # local t and not account for scr refresh
            target15_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target15_17, 'tStartRefresh')  # time at next scr refresh
            # update status
            target15_17.status = STARTED
            target15_17.setAutoDraw(True)
        
        # if target15_17 is active this frame...
        if target15_17.status == STARTED:
            # update params
            pass
        
        # if target15_17 is stopping this frame...
        if target15_17.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 88-frameTolerance:
                # keep track of stop time/frame for later
                target15_17.tStop = t  # not accounting for scr refresh
                target15_17.frameNStop = frameN  # exact frame index
                # update status
                target15_17.status = FINISHED
                target15_17.setAutoDraw(False)
        
        # *target16_17* updates
        
        # if target16_17 is starting this frame...
        if target16_17.status == NOT_STARTED and tThisFlip >= 92-frameTolerance:
            # keep track of start time/frame for later
            target16_17.frameNStart = frameN  # exact frame index
            target16_17.tStart = t  # local t and not account for scr refresh
            target16_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target16_17, 'tStartRefresh')  # time at next scr refresh
            # update status
            target16_17.status = STARTED
            target16_17.setAutoDraw(True)
        
        # if target16_17 is active this frame...
        if target16_17.status == STARTED:
            # update params
            pass
        
        # if target16_17 is stopping this frame...
        if target16_17.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 94-frameTolerance:
                # keep track of stop time/frame for later
                target16_17.tStop = t  # not accounting for scr refresh
                target16_17.frameNStop = frameN  # exact frame index
                # update status
                target16_17.status = FINISHED
                target16_17.setAutoDraw(False)
        
        # *target17_17* updates
        
        # if target17_17 is starting this frame...
        if target17_17.status == NOT_STARTED and tThisFlip >= 98-frameTolerance:
            # keep track of start time/frame for later
            target17_17.frameNStart = frameN  # exact frame index
            target17_17.tStart = t  # local t and not account for scr refresh
            target17_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target17_17, 'tStartRefresh')  # time at next scr refresh
            # update status
            target17_17.status = STARTED
            target17_17.setAutoDraw(True)
        
        # if target17_17 is active this frame...
        if target17_17.status == STARTED:
            # update params
            pass
        
        # if target17_17 is stopping this frame...
        if target17_17.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 100-frameTolerance:
                # keep track of stop time/frame for later
                target17_17.tStop = t  # not accounting for scr refresh
                target17_17.frameNStop = frameN  # exact frame index
                # update status
                target17_17.status = FINISHED
                target17_17.setAutoDraw(False)
        
        # *target18_17* updates
        
        # if target18_17 is starting this frame...
        if target18_17.status == NOT_STARTED and tThisFlip >= 104-frameTolerance:
            # keep track of start time/frame for later
            target18_17.frameNStart = frameN  # exact frame index
            target18_17.tStart = t  # local t and not account for scr refresh
            target18_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target18_17, 'tStartRefresh')  # time at next scr refresh
            # update status
            target18_17.status = STARTED
            target18_17.setAutoDraw(True)
        
        # if target18_17 is active this frame...
        if target18_17.status == STARTED:
            # update params
            pass
        
        # if target18_17 is stopping this frame...
        if target18_17.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 106-frameTolerance:
                # keep track of stop time/frame for later
                target18_17.tStop = t  # not accounting for scr refresh
                target18_17.frameNStop = frameN  # exact frame index
                # update status
                target18_17.status = FINISHED
                target18_17.setAutoDraw(False)
        
        # *target19_17* updates
        
        # if target19_17 is starting this frame...
        if target19_17.status == NOT_STARTED and tThisFlip >= 110-frameTolerance:
            # keep track of start time/frame for later
            target19_17.frameNStart = frameN  # exact frame index
            target19_17.tStart = t  # local t and not account for scr refresh
            target19_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target19_17, 'tStartRefresh')  # time at next scr refresh
            # update status
            target19_17.status = STARTED
            target19_17.setAutoDraw(True)
        
        # if target19_17 is active this frame...
        if target19_17.status == STARTED:
            # update params
            pass
        
        # if target19_17 is stopping this frame...
        if target19_17.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 112-frameTolerance:
                # keep track of stop time/frame for later
                target19_17.tStop = t  # not accounting for scr refresh
                target19_17.frameNStop = frameN  # exact frame index
                # update status
                target19_17.status = FINISHED
                target19_17.setAutoDraw(False)
        
        # *target20_17* updates
        
        # if target20_17 is starting this frame...
        if target20_17.status == NOT_STARTED and tThisFlip >= 116-frameTolerance:
            # keep track of start time/frame for later
            target20_17.frameNStart = frameN  # exact frame index
            target20_17.tStart = t  # local t and not account for scr refresh
            target20_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target20_17, 'tStartRefresh')  # time at next scr refresh
            # update status
            target20_17.status = STARTED
            target20_17.setAutoDraw(True)
        
        # if target20_17 is active this frame...
        if target20_17.status == STARTED:
            # update params
            pass
        
        # if target20_17 is stopping this frame...
        if target20_17.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 118-frameTolerance:
                # keep track of stop time/frame for later
                target20_17.tStop = t  # not accounting for scr refresh
                target20_17.frameNStop = frameN  # exact frame index
                # update status
                target20_17.status = FINISHED
                target20_17.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial8Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial8" ---
    for thisComponent in trial8Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('trial8.stopped', globalClock.getTime())
    sound_25.pause()  # ensure sound has stopped at end of Routine
    # check responses
    if key_resp_49.keys in ['', [], None]:  # No response was made
        key_resp_49.keys = None
    thisExp.addData('key_resp_49.keys',key_resp_49.keys)
    if key_resp_49.keys != None:  # we had a response
        thisExp.addData('key_resp_49.rt', key_resp_49.rt)
        thisExp.addData('key_resp_49.duration', key_resp_49.duration)
    thisExp.nextEntry()
    # the Routine "trial8" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "c1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('c1.started', globalClock.getTime())
    slider_1.reset()
    # keep track of which components have finished
    c1Components = [slider_1, text_4]
    for thisComponent in c1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "c1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 15.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 15-frameTolerance:
            continueRoutine = False
        
        # *slider_1* updates
        
        # if slider_1 is starting this frame...
        if slider_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_1.frameNStart = frameN  # exact frame index
            slider_1.tStart = t  # local t and not account for scr refresh
            slider_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider_1.started')
            # update status
            slider_1.status = STARTED
            slider_1.setAutoDraw(True)
        
        # if slider_1 is active this frame...
        if slider_1.status == STARTED:
            # update params
            pass
        
        # if slider_1 is stopping this frame...
        if slider_1.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 15-frameTolerance:
                # keep track of stop time/frame for later
                slider_1.tStop = t  # not accounting for scr refresh
                slider_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_1.stopped')
                # update status
                slider_1.status = FINISHED
                slider_1.setAutoDraw(False)
        
        # *text_4* updates
        
        # if text_4 is starting this frame...
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_4.status = STARTED
            text_4.setAutoDraw(True)
        
        # if text_4 is active this frame...
        if text_4.status == STARTED:
            # update params
            pass
        
        # if text_4 is stopping this frame...
        if text_4.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 15-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                # update status
                text_4.status = FINISHED
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in c1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "c1" ---
    for thisComponent in c1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('c1.stopped', globalClock.getTime())
    thisExp.addData('slider_1.response', slider_1.getRating())
    thisExp.addData('slider_1.rt', slider_1.getRT())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-15.000000)
    
    # --- Prepare to start Routine "trial9" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('trial9.started', globalClock.getTime())
    sound_26.setSound('C:/Users/fatma/OneDrive/Desktop/IITK BOOKS/Decision Making/DM Project/Stimulus/task_sound_stimulus/t9.ogg.opus', hamming=True)
    sound_26.setVolume(1.0, log=False)
    sound_26.seek(0)
    key_resp_50.keys = []
    key_resp_50.rt = []
    _key_resp_50_allKeys = []
    # keep track of which components have finished
    trial9Components = [sound_26, key_resp_50, target_18, target2_18, target3_18, target4_18, target5_18, target6_18, target7_18, target8_18, target9_18, target10_18, target11_18, target12_18, target13_18, target14_18, target15_18, target16_18, target17_18, target18_18, target19_18, target20_18]
    for thisComponent in trial9Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial9" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 120-frameTolerance:
            continueRoutine = False
        
        # if sound_26 is starting this frame...
        if sound_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_26.frameNStart = frameN  # exact frame index
            sound_26.tStart = t  # local t and not account for scr refresh
            sound_26.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_26.started', tThisFlipGlobal)
            # update status
            sound_26.status = STARTED
            sound_26.play(when=win)  # sync with win flip
        # update sound_26 status according to whether it's playing
        if sound_26.isPlaying:
            sound_26.status = STARTED
        elif sound_26.isFinished:
            sound_26.status = FINISHED
        
        # *key_resp_50* updates
        waitOnFlip = False
        
        # if key_resp_50 is starting this frame...
        if key_resp_50.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_50.frameNStart = frameN  # exact frame index
            key_resp_50.tStart = t  # local t and not account for scr refresh
            key_resp_50.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_50, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_50.started')
            # update status
            key_resp_50.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_50.clock.reset)  # t=0 on next screen flip
        
        # if key_resp_50 is stopping this frame...
        if key_resp_50.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 120-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_50.tStop = t  # not accounting for scr refresh
                key_resp_50.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_50.stopped')
                # update status
                key_resp_50.status = FINISHED
                key_resp_50.status = FINISHED
        if key_resp_50.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_50.getKeys(keyList=['left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_50_allKeys.extend(theseKeys)
            if len(_key_resp_50_allKeys):
                key_resp_50.keys = [key.name for key in _key_resp_50_allKeys]  # storing all keys
                key_resp_50.rt = [key.rt for key in _key_resp_50_allKeys]
                key_resp_50.duration = [key.duration for key in _key_resp_50_allKeys]
        
        # *target_18* updates
        
        # if target_18 is starting this frame...
        if target_18.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            target_18.frameNStart = frameN  # exact frame index
            target_18.tStart = t  # local t and not account for scr refresh
            target_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_18, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target_18.started')
            # update status
            target_18.status = STARTED
            target_18.setAutoDraw(True)
        
        # if target_18 is active this frame...
        if target_18.status == STARTED:
            # update params
            pass
        
        # if target_18 is stopping this frame...
        if target_18.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4-frameTolerance:
                # keep track of stop time/frame for later
                target_18.tStop = t  # not accounting for scr refresh
                target_18.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target_18.stopped')
                # update status
                target_18.status = FINISHED
                target_18.setAutoDraw(False)
        
        # *target2_18* updates
        
        # if target2_18 is starting this frame...
        if target2_18.status == NOT_STARTED and tThisFlip >= 8-frameTolerance:
            # keep track of start time/frame for later
            target2_18.frameNStart = frameN  # exact frame index
            target2_18.tStart = t  # local t and not account for scr refresh
            target2_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target2_18, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target2_18.started')
            # update status
            target2_18.status = STARTED
            target2_18.setAutoDraw(True)
        
        # if target2_18 is active this frame...
        if target2_18.status == STARTED:
            # update params
            pass
        
        # if target2_18 is stopping this frame...
        if target2_18.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 10-frameTolerance:
                # keep track of stop time/frame for later
                target2_18.tStop = t  # not accounting for scr refresh
                target2_18.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target2_18.stopped')
                # update status
                target2_18.status = FINISHED
                target2_18.setAutoDraw(False)
        
        # *target3_18* updates
        
        # if target3_18 is starting this frame...
        if target3_18.status == NOT_STARTED and tThisFlip >= 14-frameTolerance:
            # keep track of start time/frame for later
            target3_18.frameNStart = frameN  # exact frame index
            target3_18.tStart = t  # local t and not account for scr refresh
            target3_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target3_18, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target3_18.started')
            # update status
            target3_18.status = STARTED
            target3_18.setAutoDraw(True)
        
        # if target3_18 is active this frame...
        if target3_18.status == STARTED:
            # update params
            pass
        
        # if target3_18 is stopping this frame...
        if target3_18.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 16-frameTolerance:
                # keep track of stop time/frame for later
                target3_18.tStop = t  # not accounting for scr refresh
                target3_18.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target3_18.stopped')
                # update status
                target3_18.status = FINISHED
                target3_18.setAutoDraw(False)
        
        # *target4_18* updates
        
        # if target4_18 is starting this frame...
        if target4_18.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
            # keep track of start time/frame for later
            target4_18.frameNStart = frameN  # exact frame index
            target4_18.tStart = t  # local t and not account for scr refresh
            target4_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target4_18, 'tStartRefresh')  # time at next scr refresh
            # update status
            target4_18.status = STARTED
            target4_18.setAutoDraw(True)
        
        # if target4_18 is active this frame...
        if target4_18.status == STARTED:
            # update params
            pass
        
        # if target4_18 is stopping this frame...
        if target4_18.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 22-frameTolerance:
                # keep track of stop time/frame for later
                target4_18.tStop = t  # not accounting for scr refresh
                target4_18.frameNStop = frameN  # exact frame index
                # update status
                target4_18.status = FINISHED
                target4_18.setAutoDraw(False)
        
        # *target5_18* updates
        
        # if target5_18 is starting this frame...
        if target5_18.status == NOT_STARTED and tThisFlip >= 26-frameTolerance:
            # keep track of start time/frame for later
            target5_18.frameNStart = frameN  # exact frame index
            target5_18.tStart = t  # local t and not account for scr refresh
            target5_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target5_18, 'tStartRefresh')  # time at next scr refresh
            # update status
            target5_18.status = STARTED
            target5_18.setAutoDraw(True)
        
        # if target5_18 is active this frame...
        if target5_18.status == STARTED:
            # update params
            pass
        
        # if target5_18 is stopping this frame...
        if target5_18.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 28-frameTolerance:
                # keep track of stop time/frame for later
                target5_18.tStop = t  # not accounting for scr refresh
                target5_18.frameNStop = frameN  # exact frame index
                # update status
                target5_18.status = FINISHED
                target5_18.setAutoDraw(False)
        
        # *target6_18* updates
        
        # if target6_18 is starting this frame...
        if target6_18.status == NOT_STARTED and tThisFlip >= 32-frameTolerance:
            # keep track of start time/frame for later
            target6_18.frameNStart = frameN  # exact frame index
            target6_18.tStart = t  # local t and not account for scr refresh
            target6_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target6_18, 'tStartRefresh')  # time at next scr refresh
            # update status
            target6_18.status = STARTED
            target6_18.setAutoDraw(True)
        
        # if target6_18 is active this frame...
        if target6_18.status == STARTED:
            # update params
            pass
        
        # if target6_18 is stopping this frame...
        if target6_18.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 34-frameTolerance:
                # keep track of stop time/frame for later
                target6_18.tStop = t  # not accounting for scr refresh
                target6_18.frameNStop = frameN  # exact frame index
                # update status
                target6_18.status = FINISHED
                target6_18.setAutoDraw(False)
        
        # *target7_18* updates
        
        # if target7_18 is starting this frame...
        if target7_18.status == NOT_STARTED and tThisFlip >= 38-frameTolerance:
            # keep track of start time/frame for later
            target7_18.frameNStart = frameN  # exact frame index
            target7_18.tStart = t  # local t and not account for scr refresh
            target7_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target7_18, 'tStartRefresh')  # time at next scr refresh
            # update status
            target7_18.status = STARTED
            target7_18.setAutoDraw(True)
        
        # if target7_18 is active this frame...
        if target7_18.status == STARTED:
            # update params
            pass
        
        # if target7_18 is stopping this frame...
        if target7_18.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 40-frameTolerance:
                # keep track of stop time/frame for later
                target7_18.tStop = t  # not accounting for scr refresh
                target7_18.frameNStop = frameN  # exact frame index
                # update status
                target7_18.status = FINISHED
                target7_18.setAutoDraw(False)
        
        # *target8_18* updates
        
        # if target8_18 is starting this frame...
        if target8_18.status == NOT_STARTED and tThisFlip >= 44-frameTolerance:
            # keep track of start time/frame for later
            target8_18.frameNStart = frameN  # exact frame index
            target8_18.tStart = t  # local t and not account for scr refresh
            target8_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target8_18, 'tStartRefresh')  # time at next scr refresh
            # update status
            target8_18.status = STARTED
            target8_18.setAutoDraw(True)
        
        # if target8_18 is active this frame...
        if target8_18.status == STARTED:
            # update params
            pass
        
        # if target8_18 is stopping this frame...
        if target8_18.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 46-frameTolerance:
                # keep track of stop time/frame for later
                target8_18.tStop = t  # not accounting for scr refresh
                target8_18.frameNStop = frameN  # exact frame index
                # update status
                target8_18.status = FINISHED
                target8_18.setAutoDraw(False)
        
        # *target9_18* updates
        
        # if target9_18 is starting this frame...
        if target9_18.status == NOT_STARTED and tThisFlip >= 50-frameTolerance:
            # keep track of start time/frame for later
            target9_18.frameNStart = frameN  # exact frame index
            target9_18.tStart = t  # local t and not account for scr refresh
            target9_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target9_18, 'tStartRefresh')  # time at next scr refresh
            # update status
            target9_18.status = STARTED
            target9_18.setAutoDraw(True)
        
        # if target9_18 is active this frame...
        if target9_18.status == STARTED:
            # update params
            pass
        
        # if target9_18 is stopping this frame...
        if target9_18.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 52-frameTolerance:
                # keep track of stop time/frame for later
                target9_18.tStop = t  # not accounting for scr refresh
                target9_18.frameNStop = frameN  # exact frame index
                # update status
                target9_18.status = FINISHED
                target9_18.setAutoDraw(False)
        
        # *target10_18* updates
        
        # if target10_18 is starting this frame...
        if target10_18.status == NOT_STARTED and tThisFlip >= 56-frameTolerance:
            # keep track of start time/frame for later
            target10_18.frameNStart = frameN  # exact frame index
            target10_18.tStart = t  # local t and not account for scr refresh
            target10_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target10_18, 'tStartRefresh')  # time at next scr refresh
            # update status
            target10_18.status = STARTED
            target10_18.setAutoDraw(True)
        
        # if target10_18 is active this frame...
        if target10_18.status == STARTED:
            # update params
            pass
        
        # if target10_18 is stopping this frame...
        if target10_18.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 58-frameTolerance:
                # keep track of stop time/frame for later
                target10_18.tStop = t  # not accounting for scr refresh
                target10_18.frameNStop = frameN  # exact frame index
                # update status
                target10_18.status = FINISHED
                target10_18.setAutoDraw(False)
        
        # *target11_18* updates
        
        # if target11_18 is starting this frame...
        if target11_18.status == NOT_STARTED and tThisFlip >= 62-frameTolerance:
            # keep track of start time/frame for later
            target11_18.frameNStart = frameN  # exact frame index
            target11_18.tStart = t  # local t and not account for scr refresh
            target11_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target11_18, 'tStartRefresh')  # time at next scr refresh
            # update status
            target11_18.status = STARTED
            target11_18.setAutoDraw(True)
        
        # if target11_18 is active this frame...
        if target11_18.status == STARTED:
            # update params
            pass
        
        # if target11_18 is stopping this frame...
        if target11_18.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 64-frameTolerance:
                # keep track of stop time/frame for later
                target11_18.tStop = t  # not accounting for scr refresh
                target11_18.frameNStop = frameN  # exact frame index
                # update status
                target11_18.status = FINISHED
                target11_18.setAutoDraw(False)
        
        # *target12_18* updates
        
        # if target12_18 is starting this frame...
        if target12_18.status == NOT_STARTED and tThisFlip >= 68-frameTolerance:
            # keep track of start time/frame for later
            target12_18.frameNStart = frameN  # exact frame index
            target12_18.tStart = t  # local t and not account for scr refresh
            target12_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target12_18, 'tStartRefresh')  # time at next scr refresh
            # update status
            target12_18.status = STARTED
            target12_18.setAutoDraw(True)
        
        # if target12_18 is active this frame...
        if target12_18.status == STARTED:
            # update params
            pass
        
        # if target12_18 is stopping this frame...
        if target12_18.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 70-frameTolerance:
                # keep track of stop time/frame for later
                target12_18.tStop = t  # not accounting for scr refresh
                target12_18.frameNStop = frameN  # exact frame index
                # update status
                target12_18.status = FINISHED
                target12_18.setAutoDraw(False)
        
        # *target13_18* updates
        
        # if target13_18 is starting this frame...
        if target13_18.status == NOT_STARTED and tThisFlip >= 74-frameTolerance:
            # keep track of start time/frame for later
            target13_18.frameNStart = frameN  # exact frame index
            target13_18.tStart = t  # local t and not account for scr refresh
            target13_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target13_18, 'tStartRefresh')  # time at next scr refresh
            # update status
            target13_18.status = STARTED
            target13_18.setAutoDraw(True)
        
        # if target13_18 is active this frame...
        if target13_18.status == STARTED:
            # update params
            pass
        
        # if target13_18 is stopping this frame...
        if target13_18.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 76-frameTolerance:
                # keep track of stop time/frame for later
                target13_18.tStop = t  # not accounting for scr refresh
                target13_18.frameNStop = frameN  # exact frame index
                # update status
                target13_18.status = FINISHED
                target13_18.setAutoDraw(False)
        
        # *target14_18* updates
        
        # if target14_18 is starting this frame...
        if target14_18.status == NOT_STARTED and tThisFlip >= 80-frameTolerance:
            # keep track of start time/frame for later
            target14_18.frameNStart = frameN  # exact frame index
            target14_18.tStart = t  # local t and not account for scr refresh
            target14_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target14_18, 'tStartRefresh')  # time at next scr refresh
            # update status
            target14_18.status = STARTED
            target14_18.setAutoDraw(True)
        
        # if target14_18 is active this frame...
        if target14_18.status == STARTED:
            # update params
            pass
        
        # if target14_18 is stopping this frame...
        if target14_18.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 82-frameTolerance:
                # keep track of stop time/frame for later
                target14_18.tStop = t  # not accounting for scr refresh
                target14_18.frameNStop = frameN  # exact frame index
                # update status
                target14_18.status = FINISHED
                target14_18.setAutoDraw(False)
        
        # *target15_18* updates
        
        # if target15_18 is starting this frame...
        if target15_18.status == NOT_STARTED and tThisFlip >= 86-frameTolerance:
            # keep track of start time/frame for later
            target15_18.frameNStart = frameN  # exact frame index
            target15_18.tStart = t  # local t and not account for scr refresh
            target15_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target15_18, 'tStartRefresh')  # time at next scr refresh
            # update status
            target15_18.status = STARTED
            target15_18.setAutoDraw(True)
        
        # if target15_18 is active this frame...
        if target15_18.status == STARTED:
            # update params
            pass
        
        # if target15_18 is stopping this frame...
        if target15_18.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 88-frameTolerance:
                # keep track of stop time/frame for later
                target15_18.tStop = t  # not accounting for scr refresh
                target15_18.frameNStop = frameN  # exact frame index
                # update status
                target15_18.status = FINISHED
                target15_18.setAutoDraw(False)
        
        # *target16_18* updates
        
        # if target16_18 is starting this frame...
        if target16_18.status == NOT_STARTED and tThisFlip >= 92-frameTolerance:
            # keep track of start time/frame for later
            target16_18.frameNStart = frameN  # exact frame index
            target16_18.tStart = t  # local t and not account for scr refresh
            target16_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target16_18, 'tStartRefresh')  # time at next scr refresh
            # update status
            target16_18.status = STARTED
            target16_18.setAutoDraw(True)
        
        # if target16_18 is active this frame...
        if target16_18.status == STARTED:
            # update params
            pass
        
        # if target16_18 is stopping this frame...
        if target16_18.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 94-frameTolerance:
                # keep track of stop time/frame for later
                target16_18.tStop = t  # not accounting for scr refresh
                target16_18.frameNStop = frameN  # exact frame index
                # update status
                target16_18.status = FINISHED
                target16_18.setAutoDraw(False)
        
        # *target17_18* updates
        
        # if target17_18 is starting this frame...
        if target17_18.status == NOT_STARTED and tThisFlip >= 98-frameTolerance:
            # keep track of start time/frame for later
            target17_18.frameNStart = frameN  # exact frame index
            target17_18.tStart = t  # local t and not account for scr refresh
            target17_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target17_18, 'tStartRefresh')  # time at next scr refresh
            # update status
            target17_18.status = STARTED
            target17_18.setAutoDraw(True)
        
        # if target17_18 is active this frame...
        if target17_18.status == STARTED:
            # update params
            pass
        
        # if target17_18 is stopping this frame...
        if target17_18.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 100-frameTolerance:
                # keep track of stop time/frame for later
                target17_18.tStop = t  # not accounting for scr refresh
                target17_18.frameNStop = frameN  # exact frame index
                # update status
                target17_18.status = FINISHED
                target17_18.setAutoDraw(False)
        
        # *target18_18* updates
        
        # if target18_18 is starting this frame...
        if target18_18.status == NOT_STARTED and tThisFlip >= 104-frameTolerance:
            # keep track of start time/frame for later
            target18_18.frameNStart = frameN  # exact frame index
            target18_18.tStart = t  # local t and not account for scr refresh
            target18_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target18_18, 'tStartRefresh')  # time at next scr refresh
            # update status
            target18_18.status = STARTED
            target18_18.setAutoDraw(True)
        
        # if target18_18 is active this frame...
        if target18_18.status == STARTED:
            # update params
            pass
        
        # if target18_18 is stopping this frame...
        if target18_18.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 106-frameTolerance:
                # keep track of stop time/frame for later
                target18_18.tStop = t  # not accounting for scr refresh
                target18_18.frameNStop = frameN  # exact frame index
                # update status
                target18_18.status = FINISHED
                target18_18.setAutoDraw(False)
        
        # *target19_18* updates
        
        # if target19_18 is starting this frame...
        if target19_18.status == NOT_STARTED and tThisFlip >= 110-frameTolerance:
            # keep track of start time/frame for later
            target19_18.frameNStart = frameN  # exact frame index
            target19_18.tStart = t  # local t and not account for scr refresh
            target19_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target19_18, 'tStartRefresh')  # time at next scr refresh
            # update status
            target19_18.status = STARTED
            target19_18.setAutoDraw(True)
        
        # if target19_18 is active this frame...
        if target19_18.status == STARTED:
            # update params
            pass
        
        # if target19_18 is stopping this frame...
        if target19_18.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 112-frameTolerance:
                # keep track of stop time/frame for later
                target19_18.tStop = t  # not accounting for scr refresh
                target19_18.frameNStop = frameN  # exact frame index
                # update status
                target19_18.status = FINISHED
                target19_18.setAutoDraw(False)
        
        # *target20_18* updates
        
        # if target20_18 is starting this frame...
        if target20_18.status == NOT_STARTED and tThisFlip >= 116-frameTolerance:
            # keep track of start time/frame for later
            target20_18.frameNStart = frameN  # exact frame index
            target20_18.tStart = t  # local t and not account for scr refresh
            target20_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target20_18, 'tStartRefresh')  # time at next scr refresh
            # update status
            target20_18.status = STARTED
            target20_18.setAutoDraw(True)
        
        # if target20_18 is active this frame...
        if target20_18.status == STARTED:
            # update params
            pass
        
        # if target20_18 is stopping this frame...
        if target20_18.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 118-frameTolerance:
                # keep track of stop time/frame for later
                target20_18.tStop = t  # not accounting for scr refresh
                target20_18.frameNStop = frameN  # exact frame index
                # update status
                target20_18.status = FINISHED
                target20_18.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial9Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial9" ---
    for thisComponent in trial9Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('trial9.stopped', globalClock.getTime())
    sound_26.pause()  # ensure sound has stopped at end of Routine
    # check responses
    if key_resp_50.keys in ['', [], None]:  # No response was made
        key_resp_50.keys = None
    thisExp.addData('key_resp_50.keys',key_resp_50.keys)
    if key_resp_50.keys != None:  # we had a response
        thisExp.addData('key_resp_50.rt', key_resp_50.rt)
        thisExp.addData('key_resp_50.duration', key_resp_50.duration)
    thisExp.nextEntry()
    # the Routine "trial9" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "c1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('c1.started', globalClock.getTime())
    slider_1.reset()
    # keep track of which components have finished
    c1Components = [slider_1, text_4]
    for thisComponent in c1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "c1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 15.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 15-frameTolerance:
            continueRoutine = False
        
        # *slider_1* updates
        
        # if slider_1 is starting this frame...
        if slider_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_1.frameNStart = frameN  # exact frame index
            slider_1.tStart = t  # local t and not account for scr refresh
            slider_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider_1.started')
            # update status
            slider_1.status = STARTED
            slider_1.setAutoDraw(True)
        
        # if slider_1 is active this frame...
        if slider_1.status == STARTED:
            # update params
            pass
        
        # if slider_1 is stopping this frame...
        if slider_1.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 15-frameTolerance:
                # keep track of stop time/frame for later
                slider_1.tStop = t  # not accounting for scr refresh
                slider_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_1.stopped')
                # update status
                slider_1.status = FINISHED
                slider_1.setAutoDraw(False)
        
        # *text_4* updates
        
        # if text_4 is starting this frame...
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_4.status = STARTED
            text_4.setAutoDraw(True)
        
        # if text_4 is active this frame...
        if text_4.status == STARTED:
            # update params
            pass
        
        # if text_4 is stopping this frame...
        if text_4.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 15-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                # update status
                text_4.status = FINISHED
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in c1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "c1" ---
    for thisComponent in c1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('c1.stopped', globalClock.getTime())
    thisExp.addData('slider_1.response', slider_1.getRating())
    thisExp.addData('slider_1.rt', slider_1.getRT())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-15.000000)
    
    # --- Prepare to start Routine "trial10" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('trial10.started', globalClock.getTime())
    sound_27.setSound('C:/Users/fatma/OneDrive/Desktop/IITK BOOKS/Decision Making/DM Project/Stimulus/task_sound_stimulus/t10.ogg.opus', hamming=True)
    sound_27.setVolume(1.0, log=False)
    sound_27.seek(0)
    key_resp_51.keys = []
    key_resp_51.rt = []
    _key_resp_51_allKeys = []
    # keep track of which components have finished
    trial10Components = [sound_27, key_resp_51, target_19, target2_19, target3_19, target4_19, target5_19, target6_19, target7_19, target8_19, target9_19, target10_19, target11_19, target12_19, target13_19, target14_19, target15_19, target16_19, target17_19, target18_19, target19_19, target20_19]
    for thisComponent in trial10Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "trial10" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 120-frameTolerance:
            continueRoutine = False
        
        # if sound_27 is starting this frame...
        if sound_27.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            sound_27.frameNStart = frameN  # exact frame index
            sound_27.tStart = t  # local t and not account for scr refresh
            sound_27.tStartRefresh = tThisFlipGlobal  # on global time
            # add timestamp to datafile
            thisExp.addData('sound_27.started', tThisFlipGlobal)
            # update status
            sound_27.status = STARTED
            sound_27.play(when=win)  # sync with win flip
        # update sound_27 status according to whether it's playing
        if sound_27.isPlaying:
            sound_27.status = STARTED
        elif sound_27.isFinished:
            sound_27.status = FINISHED
        
        # *key_resp_51* updates
        waitOnFlip = False
        
        # if key_resp_51 is starting this frame...
        if key_resp_51.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_51.frameNStart = frameN  # exact frame index
            key_resp_51.tStart = t  # local t and not account for scr refresh
            key_resp_51.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_51, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_51.started')
            # update status
            key_resp_51.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_51.clock.reset)  # t=0 on next screen flip
        
        # if key_resp_51 is stopping this frame...
        if key_resp_51.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 120-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_51.tStop = t  # not accounting for scr refresh
                key_resp_51.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp_51.stopped')
                # update status
                key_resp_51.status = FINISHED
                key_resp_51.status = FINISHED
        if key_resp_51.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_51.getKeys(keyList=['left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_51_allKeys.extend(theseKeys)
            if len(_key_resp_51_allKeys):
                key_resp_51.keys = [key.name for key in _key_resp_51_allKeys]  # storing all keys
                key_resp_51.rt = [key.rt for key in _key_resp_51_allKeys]
                key_resp_51.duration = [key.duration for key in _key_resp_51_allKeys]
        
        # *target_19* updates
        
        # if target_19 is starting this frame...
        if target_19.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
            # keep track of start time/frame for later
            target_19.frameNStart = frameN  # exact frame index
            target_19.tStart = t  # local t and not account for scr refresh
            target_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target_19, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target_19.started')
            # update status
            target_19.status = STARTED
            target_19.setAutoDraw(True)
        
        # if target_19 is active this frame...
        if target_19.status == STARTED:
            # update params
            pass
        
        # if target_19 is stopping this frame...
        if target_19.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 4-frameTolerance:
                # keep track of stop time/frame for later
                target_19.tStop = t  # not accounting for scr refresh
                target_19.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target_19.stopped')
                # update status
                target_19.status = FINISHED
                target_19.setAutoDraw(False)
        
        # *target2_19* updates
        
        # if target2_19 is starting this frame...
        if target2_19.status == NOT_STARTED and tThisFlip >= 8-frameTolerance:
            # keep track of start time/frame for later
            target2_19.frameNStart = frameN  # exact frame index
            target2_19.tStart = t  # local t and not account for scr refresh
            target2_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target2_19, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target2_19.started')
            # update status
            target2_19.status = STARTED
            target2_19.setAutoDraw(True)
        
        # if target2_19 is active this frame...
        if target2_19.status == STARTED:
            # update params
            pass
        
        # if target2_19 is stopping this frame...
        if target2_19.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 10-frameTolerance:
                # keep track of stop time/frame for later
                target2_19.tStop = t  # not accounting for scr refresh
                target2_19.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target2_19.stopped')
                # update status
                target2_19.status = FINISHED
                target2_19.setAutoDraw(False)
        
        # *target3_19* updates
        
        # if target3_19 is starting this frame...
        if target3_19.status == NOT_STARTED and tThisFlip >= 14-frameTolerance:
            # keep track of start time/frame for later
            target3_19.frameNStart = frameN  # exact frame index
            target3_19.tStart = t  # local t and not account for scr refresh
            target3_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target3_19, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'target3_19.started')
            # update status
            target3_19.status = STARTED
            target3_19.setAutoDraw(True)
        
        # if target3_19 is active this frame...
        if target3_19.status == STARTED:
            # update params
            pass
        
        # if target3_19 is stopping this frame...
        if target3_19.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 16-frameTolerance:
                # keep track of stop time/frame for later
                target3_19.tStop = t  # not accounting for scr refresh
                target3_19.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'target3_19.stopped')
                # update status
                target3_19.status = FINISHED
                target3_19.setAutoDraw(False)
        
        # *target4_19* updates
        
        # if target4_19 is starting this frame...
        if target4_19.status == NOT_STARTED and tThisFlip >= 20-frameTolerance:
            # keep track of start time/frame for later
            target4_19.frameNStart = frameN  # exact frame index
            target4_19.tStart = t  # local t and not account for scr refresh
            target4_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target4_19, 'tStartRefresh')  # time at next scr refresh
            # update status
            target4_19.status = STARTED
            target4_19.setAutoDraw(True)
        
        # if target4_19 is active this frame...
        if target4_19.status == STARTED:
            # update params
            pass
        
        # if target4_19 is stopping this frame...
        if target4_19.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 22-frameTolerance:
                # keep track of stop time/frame for later
                target4_19.tStop = t  # not accounting for scr refresh
                target4_19.frameNStop = frameN  # exact frame index
                # update status
                target4_19.status = FINISHED
                target4_19.setAutoDraw(False)
        
        # *target5_19* updates
        
        # if target5_19 is starting this frame...
        if target5_19.status == NOT_STARTED and tThisFlip >= 26-frameTolerance:
            # keep track of start time/frame for later
            target5_19.frameNStart = frameN  # exact frame index
            target5_19.tStart = t  # local t and not account for scr refresh
            target5_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target5_19, 'tStartRefresh')  # time at next scr refresh
            # update status
            target5_19.status = STARTED
            target5_19.setAutoDraw(True)
        
        # if target5_19 is active this frame...
        if target5_19.status == STARTED:
            # update params
            pass
        
        # if target5_19 is stopping this frame...
        if target5_19.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 28-frameTolerance:
                # keep track of stop time/frame for later
                target5_19.tStop = t  # not accounting for scr refresh
                target5_19.frameNStop = frameN  # exact frame index
                # update status
                target5_19.status = FINISHED
                target5_19.setAutoDraw(False)
        
        # *target6_19* updates
        
        # if target6_19 is starting this frame...
        if target6_19.status == NOT_STARTED and tThisFlip >= 32-frameTolerance:
            # keep track of start time/frame for later
            target6_19.frameNStart = frameN  # exact frame index
            target6_19.tStart = t  # local t and not account for scr refresh
            target6_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target6_19, 'tStartRefresh')  # time at next scr refresh
            # update status
            target6_19.status = STARTED
            target6_19.setAutoDraw(True)
        
        # if target6_19 is active this frame...
        if target6_19.status == STARTED:
            # update params
            pass
        
        # if target6_19 is stopping this frame...
        if target6_19.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 34-frameTolerance:
                # keep track of stop time/frame for later
                target6_19.tStop = t  # not accounting for scr refresh
                target6_19.frameNStop = frameN  # exact frame index
                # update status
                target6_19.status = FINISHED
                target6_19.setAutoDraw(False)
        
        # *target7_19* updates
        
        # if target7_19 is starting this frame...
        if target7_19.status == NOT_STARTED and tThisFlip >= 38-frameTolerance:
            # keep track of start time/frame for later
            target7_19.frameNStart = frameN  # exact frame index
            target7_19.tStart = t  # local t and not account for scr refresh
            target7_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target7_19, 'tStartRefresh')  # time at next scr refresh
            # update status
            target7_19.status = STARTED
            target7_19.setAutoDraw(True)
        
        # if target7_19 is active this frame...
        if target7_19.status == STARTED:
            # update params
            pass
        
        # if target7_19 is stopping this frame...
        if target7_19.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 40-frameTolerance:
                # keep track of stop time/frame for later
                target7_19.tStop = t  # not accounting for scr refresh
                target7_19.frameNStop = frameN  # exact frame index
                # update status
                target7_19.status = FINISHED
                target7_19.setAutoDraw(False)
        
        # *target8_19* updates
        
        # if target8_19 is starting this frame...
        if target8_19.status == NOT_STARTED and tThisFlip >= 44-frameTolerance:
            # keep track of start time/frame for later
            target8_19.frameNStart = frameN  # exact frame index
            target8_19.tStart = t  # local t and not account for scr refresh
            target8_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target8_19, 'tStartRefresh')  # time at next scr refresh
            # update status
            target8_19.status = STARTED
            target8_19.setAutoDraw(True)
        
        # if target8_19 is active this frame...
        if target8_19.status == STARTED:
            # update params
            pass
        
        # if target8_19 is stopping this frame...
        if target8_19.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 46-frameTolerance:
                # keep track of stop time/frame for later
                target8_19.tStop = t  # not accounting for scr refresh
                target8_19.frameNStop = frameN  # exact frame index
                # update status
                target8_19.status = FINISHED
                target8_19.setAutoDraw(False)
        
        # *target9_19* updates
        
        # if target9_19 is starting this frame...
        if target9_19.status == NOT_STARTED and tThisFlip >= 50-frameTolerance:
            # keep track of start time/frame for later
            target9_19.frameNStart = frameN  # exact frame index
            target9_19.tStart = t  # local t and not account for scr refresh
            target9_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target9_19, 'tStartRefresh')  # time at next scr refresh
            # update status
            target9_19.status = STARTED
            target9_19.setAutoDraw(True)
        
        # if target9_19 is active this frame...
        if target9_19.status == STARTED:
            # update params
            pass
        
        # if target9_19 is stopping this frame...
        if target9_19.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 52-frameTolerance:
                # keep track of stop time/frame for later
                target9_19.tStop = t  # not accounting for scr refresh
                target9_19.frameNStop = frameN  # exact frame index
                # update status
                target9_19.status = FINISHED
                target9_19.setAutoDraw(False)
        
        # *target10_19* updates
        
        # if target10_19 is starting this frame...
        if target10_19.status == NOT_STARTED and tThisFlip >= 56-frameTolerance:
            # keep track of start time/frame for later
            target10_19.frameNStart = frameN  # exact frame index
            target10_19.tStart = t  # local t and not account for scr refresh
            target10_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target10_19, 'tStartRefresh')  # time at next scr refresh
            # update status
            target10_19.status = STARTED
            target10_19.setAutoDraw(True)
        
        # if target10_19 is active this frame...
        if target10_19.status == STARTED:
            # update params
            pass
        
        # if target10_19 is stopping this frame...
        if target10_19.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 58-frameTolerance:
                # keep track of stop time/frame for later
                target10_19.tStop = t  # not accounting for scr refresh
                target10_19.frameNStop = frameN  # exact frame index
                # update status
                target10_19.status = FINISHED
                target10_19.setAutoDraw(False)
        
        # *target11_19* updates
        
        # if target11_19 is starting this frame...
        if target11_19.status == NOT_STARTED and tThisFlip >= 62-frameTolerance:
            # keep track of start time/frame for later
            target11_19.frameNStart = frameN  # exact frame index
            target11_19.tStart = t  # local t and not account for scr refresh
            target11_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target11_19, 'tStartRefresh')  # time at next scr refresh
            # update status
            target11_19.status = STARTED
            target11_19.setAutoDraw(True)
        
        # if target11_19 is active this frame...
        if target11_19.status == STARTED:
            # update params
            pass
        
        # if target11_19 is stopping this frame...
        if target11_19.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 64-frameTolerance:
                # keep track of stop time/frame for later
                target11_19.tStop = t  # not accounting for scr refresh
                target11_19.frameNStop = frameN  # exact frame index
                # update status
                target11_19.status = FINISHED
                target11_19.setAutoDraw(False)
        
        # *target12_19* updates
        
        # if target12_19 is starting this frame...
        if target12_19.status == NOT_STARTED and tThisFlip >= 68-frameTolerance:
            # keep track of start time/frame for later
            target12_19.frameNStart = frameN  # exact frame index
            target12_19.tStart = t  # local t and not account for scr refresh
            target12_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target12_19, 'tStartRefresh')  # time at next scr refresh
            # update status
            target12_19.status = STARTED
            target12_19.setAutoDraw(True)
        
        # if target12_19 is active this frame...
        if target12_19.status == STARTED:
            # update params
            pass
        
        # if target12_19 is stopping this frame...
        if target12_19.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 70-frameTolerance:
                # keep track of stop time/frame for later
                target12_19.tStop = t  # not accounting for scr refresh
                target12_19.frameNStop = frameN  # exact frame index
                # update status
                target12_19.status = FINISHED
                target12_19.setAutoDraw(False)
        
        # *target13_19* updates
        
        # if target13_19 is starting this frame...
        if target13_19.status == NOT_STARTED and tThisFlip >= 74-frameTolerance:
            # keep track of start time/frame for later
            target13_19.frameNStart = frameN  # exact frame index
            target13_19.tStart = t  # local t and not account for scr refresh
            target13_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target13_19, 'tStartRefresh')  # time at next scr refresh
            # update status
            target13_19.status = STARTED
            target13_19.setAutoDraw(True)
        
        # if target13_19 is active this frame...
        if target13_19.status == STARTED:
            # update params
            pass
        
        # if target13_19 is stopping this frame...
        if target13_19.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 76-frameTolerance:
                # keep track of stop time/frame for later
                target13_19.tStop = t  # not accounting for scr refresh
                target13_19.frameNStop = frameN  # exact frame index
                # update status
                target13_19.status = FINISHED
                target13_19.setAutoDraw(False)
        
        # *target14_19* updates
        
        # if target14_19 is starting this frame...
        if target14_19.status == NOT_STARTED and tThisFlip >= 80-frameTolerance:
            # keep track of start time/frame for later
            target14_19.frameNStart = frameN  # exact frame index
            target14_19.tStart = t  # local t and not account for scr refresh
            target14_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target14_19, 'tStartRefresh')  # time at next scr refresh
            # update status
            target14_19.status = STARTED
            target14_19.setAutoDraw(True)
        
        # if target14_19 is active this frame...
        if target14_19.status == STARTED:
            # update params
            pass
        
        # if target14_19 is stopping this frame...
        if target14_19.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 82-frameTolerance:
                # keep track of stop time/frame for later
                target14_19.tStop = t  # not accounting for scr refresh
                target14_19.frameNStop = frameN  # exact frame index
                # update status
                target14_19.status = FINISHED
                target14_19.setAutoDraw(False)
        
        # *target15_19* updates
        
        # if target15_19 is starting this frame...
        if target15_19.status == NOT_STARTED and tThisFlip >= 86-frameTolerance:
            # keep track of start time/frame for later
            target15_19.frameNStart = frameN  # exact frame index
            target15_19.tStart = t  # local t and not account for scr refresh
            target15_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target15_19, 'tStartRefresh')  # time at next scr refresh
            # update status
            target15_19.status = STARTED
            target15_19.setAutoDraw(True)
        
        # if target15_19 is active this frame...
        if target15_19.status == STARTED:
            # update params
            pass
        
        # if target15_19 is stopping this frame...
        if target15_19.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 88-frameTolerance:
                # keep track of stop time/frame for later
                target15_19.tStop = t  # not accounting for scr refresh
                target15_19.frameNStop = frameN  # exact frame index
                # update status
                target15_19.status = FINISHED
                target15_19.setAutoDraw(False)
        
        # *target16_19* updates
        
        # if target16_19 is starting this frame...
        if target16_19.status == NOT_STARTED and tThisFlip >= 92-frameTolerance:
            # keep track of start time/frame for later
            target16_19.frameNStart = frameN  # exact frame index
            target16_19.tStart = t  # local t and not account for scr refresh
            target16_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target16_19, 'tStartRefresh')  # time at next scr refresh
            # update status
            target16_19.status = STARTED
            target16_19.setAutoDraw(True)
        
        # if target16_19 is active this frame...
        if target16_19.status == STARTED:
            # update params
            pass
        
        # if target16_19 is stopping this frame...
        if target16_19.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 94-frameTolerance:
                # keep track of stop time/frame for later
                target16_19.tStop = t  # not accounting for scr refresh
                target16_19.frameNStop = frameN  # exact frame index
                # update status
                target16_19.status = FINISHED
                target16_19.setAutoDraw(False)
        
        # *target17_19* updates
        
        # if target17_19 is starting this frame...
        if target17_19.status == NOT_STARTED and tThisFlip >= 98-frameTolerance:
            # keep track of start time/frame for later
            target17_19.frameNStart = frameN  # exact frame index
            target17_19.tStart = t  # local t and not account for scr refresh
            target17_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target17_19, 'tStartRefresh')  # time at next scr refresh
            # update status
            target17_19.status = STARTED
            target17_19.setAutoDraw(True)
        
        # if target17_19 is active this frame...
        if target17_19.status == STARTED:
            # update params
            pass
        
        # if target17_19 is stopping this frame...
        if target17_19.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 100-frameTolerance:
                # keep track of stop time/frame for later
                target17_19.tStop = t  # not accounting for scr refresh
                target17_19.frameNStop = frameN  # exact frame index
                # update status
                target17_19.status = FINISHED
                target17_19.setAutoDraw(False)
        
        # *target18_19* updates
        
        # if target18_19 is starting this frame...
        if target18_19.status == NOT_STARTED and tThisFlip >= 104-frameTolerance:
            # keep track of start time/frame for later
            target18_19.frameNStart = frameN  # exact frame index
            target18_19.tStart = t  # local t and not account for scr refresh
            target18_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target18_19, 'tStartRefresh')  # time at next scr refresh
            # update status
            target18_19.status = STARTED
            target18_19.setAutoDraw(True)
        
        # if target18_19 is active this frame...
        if target18_19.status == STARTED:
            # update params
            pass
        
        # if target18_19 is stopping this frame...
        if target18_19.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 106-frameTolerance:
                # keep track of stop time/frame for later
                target18_19.tStop = t  # not accounting for scr refresh
                target18_19.frameNStop = frameN  # exact frame index
                # update status
                target18_19.status = FINISHED
                target18_19.setAutoDraw(False)
        
        # *target19_19* updates
        
        # if target19_19 is starting this frame...
        if target19_19.status == NOT_STARTED and tThisFlip >= 110-frameTolerance:
            # keep track of start time/frame for later
            target19_19.frameNStart = frameN  # exact frame index
            target19_19.tStart = t  # local t and not account for scr refresh
            target19_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target19_19, 'tStartRefresh')  # time at next scr refresh
            # update status
            target19_19.status = STARTED
            target19_19.setAutoDraw(True)
        
        # if target19_19 is active this frame...
        if target19_19.status == STARTED:
            # update params
            pass
        
        # if target19_19 is stopping this frame...
        if target19_19.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 112-frameTolerance:
                # keep track of stop time/frame for later
                target19_19.tStop = t  # not accounting for scr refresh
                target19_19.frameNStop = frameN  # exact frame index
                # update status
                target19_19.status = FINISHED
                target19_19.setAutoDraw(False)
        
        # *target20_19* updates
        
        # if target20_19 is starting this frame...
        if target20_19.status == NOT_STARTED and tThisFlip >= 116-frameTolerance:
            # keep track of start time/frame for later
            target20_19.frameNStart = frameN  # exact frame index
            target20_19.tStart = t  # local t and not account for scr refresh
            target20_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(target20_19, 'tStartRefresh')  # time at next scr refresh
            # update status
            target20_19.status = STARTED
            target20_19.setAutoDraw(True)
        
        # if target20_19 is active this frame...
        if target20_19.status == STARTED:
            # update params
            pass
        
        # if target20_19 is stopping this frame...
        if target20_19.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 118-frameTolerance:
                # keep track of stop time/frame for later
                target20_19.tStop = t  # not accounting for scr refresh
                target20_19.frameNStop = frameN  # exact frame index
                # update status
                target20_19.status = FINISHED
                target20_19.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trial10Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "trial10" ---
    for thisComponent in trial10Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('trial10.stopped', globalClock.getTime())
    sound_27.pause()  # ensure sound has stopped at end of Routine
    # check responses
    if key_resp_51.keys in ['', [], None]:  # No response was made
        key_resp_51.keys = None
    thisExp.addData('key_resp_51.keys',key_resp_51.keys)
    if key_resp_51.keys != None:  # we had a response
        thisExp.addData('key_resp_51.rt', key_resp_51.rt)
        thisExp.addData('key_resp_51.duration', key_resp_51.duration)
    thisExp.nextEntry()
    # the Routine "trial10" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "c1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('c1.started', globalClock.getTime())
    slider_1.reset()
    # keep track of which components have finished
    c1Components = [slider_1, text_4]
    for thisComponent in c1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "c1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine and routineTimer.getTime() < 15.0:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # is it time to end the Routine? (based on local clock)
        if tThisFlip > 15-frameTolerance:
            continueRoutine = False
        
        # *slider_1* updates
        
        # if slider_1 is starting this frame...
        if slider_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            slider_1.frameNStart = frameN  # exact frame index
            slider_1.tStart = t  # local t and not account for scr refresh
            slider_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(slider_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'slider_1.started')
            # update status
            slider_1.status = STARTED
            slider_1.setAutoDraw(True)
        
        # if slider_1 is active this frame...
        if slider_1.status == STARTED:
            # update params
            pass
        
        # if slider_1 is stopping this frame...
        if slider_1.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 15-frameTolerance:
                # keep track of stop time/frame for later
                slider_1.tStop = t  # not accounting for scr refresh
                slider_1.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'slider_1.stopped')
                # update status
                slider_1.status = FINISHED
                slider_1.setAutoDraw(False)
        
        # *text_4* updates
        
        # if text_4 is starting this frame...
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            # update status
            text_4.status = STARTED
            text_4.setAutoDraw(True)
        
        # if text_4 is active this frame...
        if text_4.status == STARTED:
            # update params
            pass
        
        # if text_4 is stopping this frame...
        if text_4.status == STARTED:
            # is it time to stop? (based on local clock)
            if tThisFlip > 15-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                # update status
                text_4.status = FINISHED
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in c1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "c1" ---
    for thisComponent in c1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('c1.stopped', globalClock.getTime())
    thisExp.addData('slider_1.response', slider_1.getRating())
    thisExp.addData('slider_1.rt', slider_1.getRT())
    # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
    if routineForceEnded:
        routineTimer.reset()
    else:
        routineTimer.addTime(-15.000000)
    
    # --- Prepare to start Routine "end" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('end.started', globalClock.getTime())
    key_resp_23.keys = []
    key_resp_23.rt = []
    _key_resp_23_allKeys = []
    # keep track of which components have finished
    endComponents = [text_3, key_resp_23]
    for thisComponent in endComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "end" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        
        # if text_3 is starting this frame...
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_3.started')
            # update status
            text_3.status = STARTED
            text_3.setAutoDraw(True)
        
        # if text_3 is active this frame...
        if text_3.status == STARTED:
            # update params
            pass
        
        # *key_resp_23* updates
        waitOnFlip = False
        
        # if key_resp_23 is starting this frame...
        if key_resp_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_23.frameNStart = frameN  # exact frame index
            key_resp_23.tStart = t  # local t and not account for scr refresh
            key_resp_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_23, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_23.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_23.clock.reset)  # t=0 on next screen flip
        if key_resp_23.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_23.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _key_resp_23_allKeys.extend(theseKeys)
            if len(_key_resp_23_allKeys):
                key_resp_23.keys = [key.name for key in _key_resp_23_allKeys]  # storing all keys
                key_resp_23.rt = [key.rt for key in _key_resp_23_allKeys]
                key_resp_23.duration = [key.duration for key in _key_resp_23_allKeys]
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, inputs=inputs, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in endComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end" ---
    for thisComponent in endComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('end.stopped', globalClock.getTime())
    # check responses
    if key_resp_23.keys in ['', [], None]:  # No response was made
        key_resp_23.keys = None
    thisExp.addData('key_resp_23.keys',key_resp_23.keys)
    if key_resp_23.keys != None:  # we had a response
        thisExp.addData('key_resp_23.rt', key_resp_23.rt)
        thisExp.addData('key_resp_23.duration', key_resp_23.duration)
    thisExp.nextEntry()
    # the Routine "end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win, inputs=inputs)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, inputs=None, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    inputs : dict
        Dictionary of input devices by name.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()


def quit(thisExp, win=None, inputs=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    inputs : dict
        Dictionary of input devices by name.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    if inputs is not None:
        if 'eyetracker' in inputs and inputs['eyetracker'] is not None:
            inputs['eyetracker'].setConnectionState(False)
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    inputs = setupInputs(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win, 
        inputs=inputs
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win, inputs=inputs)
