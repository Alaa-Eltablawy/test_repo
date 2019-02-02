import ipywidgets as widgets
from IPython.core.display import HTML
import threading
from IPython.display import display, Image
import ipywidgets as widgets
import time
import queue
import subprocess
import datetime
import matplotlib
import matplotlib.pyplot as plt
import os 

def checkUpdate():
    

def dispalyPage():
    '''
	progress indicator reads first line in the file "path" 
	path: path to the progress file
        file_name: file with data to track
	title: description of the bar
	min_: min_ value for the progress bar
	max_: max value in the progress bar

    '''
    style = {'description_width': 'initial'}

    remain_time = widgets.html(
    value='0',
    placeholder='0',
    description='remaining:',
    style=style
)
    est_time = widgets.html(
    value='0',
    placeholder='0',
    description='total estimated:',
    style=style
)

    update_button = widgets.Button(
    description='Updated demos',
    disabled=CheckUpdate,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Click me',
    icon='check'
)
    restore_button = widgets.Button(
    description='Updated demos',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Click me',
    icon='check'
)

    text_box = widgets.HTML(
    value="Hello <b>World</b>",
    placeholder='Some HTML',
    description='Some HTML',
)
    CheckUpdate = checkUpdate()
     
    def _work(update_button, restore_button):
        box_layout = widgets.layout(display='flex', flex_flow='column', align_items='stretch', border='ridge', width='70%', height='')
        box = widgets.hbox([button, est_time, remain_time], layout=box_layout)
        display(box)
        # progress
        last_status = 0.0
        remain_val = '0'
        est_val = '0'
        output_file = path
        while last_status < 100:
            if os.path.isfile(output_file):
                with open(output_file, "r") as fh:
                    line1 = fh.readline() 	#progress 
                    line2 = fh.readline()  	#remaining time
                    line3 = fh.readline()  	#estimated total time
                    if line1 and line2 and line3:
                        last_status = float(line1)
                        remain_val = line2
                        est_val = line3
                    progress_bar.value = last_status
                    remain_time.value = remain_val+' seconds' 
                    est_time.value = est_val+' seconds' 
            else:
                cmd = ['ls']
                p = subprocess.popen(cmd, stdout=subprocess.pipe)
                output,_ = p.communicate()
        remain_time.value = '0'+' seconds' 
        time.sleep(1)
        os.remove(output_file)


    thread = threading.thread(target=_work, args=(button, est_time, remain_time))
    thread.start()
    time.sleep(0.1)


