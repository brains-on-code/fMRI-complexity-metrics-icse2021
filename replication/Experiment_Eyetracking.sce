scenario = "ProgCode4_Eyetracking";
scan_period = 2000;
scenario_type = fMRI;

no_logfile = false;
write_codes = true;

active_buttons = 4;
button_codes = 3,4,7,8;
response_matching = simple_matching;

pulse_width = 30;  
pulses_per_scan = 1;
pulse_code = 30;

default_font_size = 22;
default_font = "arial"; 
default_text_color = 255,255,255;
default_background_color = 0,0,0;
default_text_align = align_left; 

begin;

# todo fix the times (and further down!) for the real experiment to 10000 \ 29900 (30000-100 ms for the camera delay) \ 2000
$D2rTime = 10000; #10000
$RestConditionTime = 30000; #30000
$LastResponseChanceTime = 2000;
$xf = 0;
$yf = 0;

picture {
   background_color = 0,0,0;
} et_calibration;


# images for comprehension and syntax conditions
# presentation will display it in the order of the array
# todo add pseudo-randomization to this (if i do, need to adjust the syntax click amount limit in loop script)
array {
	# Trial 1
   bitmap { filename = "ArrayAverage.png"; description = "ArrayAverage_Number"; preload = false; scale_factor = 1.0; };
   bitmap { filename = "ContainsSubstring.png"; description = "ContainsSubstring_Word"; preload = false; scale_factor = 1.0; };
   bitmap { filename = "RecursiveBinaryToDecimal.png"; description = "RecursiveBinaryToDecimal_Recur"; preload = false; scale_factor = 1.0; };
   bitmap { filename = "Syn_BubbleSort.png"; description = "Syn_BubbleSort"; preload = false; scale_factor = 1.0; };

	# Trial 2
   bitmap { filename = "CountVowels.png"; description = "CountVowels_Word"; preload = false; scale_factor = 1.0; };
   bitmap { filename = "DumbSort.png"; description = "DumbSort_Number"; preload = false; scale_factor = 1.0; };
   bitmap { filename = "RecursiveCrossSum.png"; description = "RecursiveCrossSum_Recur"; preload = false; scale_factor = 1.0; };
   bitmap { filename = "Syn_CountSameCharsAtSamePosition.png"; description = "Syn_CountSameCharsAtSamePosition"; preload = false; scale_factor = 1.0; };

	# Trial 3
   bitmap { filename = "GreatestCommonDivisor.png"; description = "GreatestCommonDivisor_Number"; preload = false; scale_factor = 1.0; };
   bitmap { filename = "isHurricane.png"; description = "isHurricane_Number"; preload = false; scale_factor = 1.0; };
   bitmap { filename = "RecursiveFactorial.png"; description = "RecursiveFactorial_Recur"; preload = false; scale_factor = 1.0; };
   bitmap { filename = "Syn_DecimalToBinary.png"; description = "Syn_DecimalToBinary"; preload = false; scale_factor = 1.0; };

	# Trial 4
   bitmap { filename = "isPalindrome.png"; description = "isPalindrome_word"; preload = false; scale_factor = 1.0; };
   bitmap { filename = "hIndex.png"; description = "hIndex_number"; preload = false; scale_factor = 1.0; };
   bitmap { filename = "RecursiveFibonacciVariant.png"; description = "RecursiveFibonacciVariant_Recur"; preload = false; scale_factor = 1.0; };
   bitmap { filename = "Syn_IntertwineTwoWords.png"; description = "Syn_IntertwineTwoWords"; preload = false; scale_factor = 1.0; };

	# Trial 5
   bitmap { filename = "lengthOfLastWord.png"; description = "lengthOfLastWord_word"; preload = false; scale_factor = 1.0; };
   bitmap { filename = "SquareRoot.png"; description = "SquareRoot_number"; preload = false; scale_factor = 1.0; };
   bitmap { filename = "YesNo.png"; description = "YesNo_word"; preload = false; scale_factor = 1.0; };
   bitmap { filename = "RecursivePower.png"; description = "RecursivePower_Recur"; preload = false; scale_factor = 1.0; };
   bitmap { filename = "Syn_StringPermutation.png"; description = "Syn_StringPermutation"; preload = false; scale_factor = 1.0; };

} code_stimuli_images;

array {
   bitmap { filename = "attention_task_0.png"; description = "D2_0"; preload = false; scale_factor = 1.0; };
   bitmap { filename = "attention_task_1.png"; description = "D2_1"; preload = false; scale_factor = 1.0; };
   bitmap { filename = "attention_task_2.png"; description = "D2_2"; preload = false; scale_factor = 1.0; };
   bitmap { filename = "attention_task_3.png"; description = "D2_3"; preload = false; scale_factor = 1.0; };
   bitmap { filename = "attention_task_4.png"; description = "D2_4"; preload = false; scale_factor = 1.0; };
   bitmap { filename = "attention_task_5.png"; description = "D2_5"; preload = false; scale_factor = 1.0; };
   bitmap { filename = "attention_task_6.png"; description = "D2_6"; preload = false; scale_factor = 1.0; };
   bitmap { filename = "attention_task_7.png"; description = "D2_7"; preload = false; scale_factor = 1.0; };
   bitmap { filename = "attention_task_8.png"; description = "D2_8"; preload = false; scale_factor = 1.0; };
   bitmap { filename = "attention_task_9.png"; description = "D2_9"; preload = false; scale_factor = 1.0; };
   bitmap { filename = "attention_task_10.png"; description = "D2_10"; preload = false; scale_factor = 1.0; };
   bitmap { filename = "attention_task_11.png"; description = "D2_11"; preload = false; scale_factor = 1.0; };
   bitmap { filename = "attention_task_12.png"; description = "D2_12"; preload = false; scale_factor = 1.0; };
   bitmap { filename = "attention_task_13.png"; description = "D2_13"; preload = false; scale_factor = 1.0; };
	bitmap { filename = "attention_task_14.png"; description = "D2_14"; preload = false; scale_factor = 1.0; };
	bitmap { filename = "attention_task_15.png"; description = "D2_15"; preload = false; scale_factor = 1.0; };
	bitmap { filename = "attention_task_16.png"; description = "D2_16"; preload = false; scale_factor = 1.0; };
	bitmap { filename = "attention_task_17.png"; description = "D2_17"; preload = false; scale_factor = 1.0; };
	bitmap { filename = "attention_task_18.png"; description = "D2_18"; preload = false; scale_factor = 1.0; };
	bitmap { filename = "attention_task_19.png"; description = "D2_19"; preload = false; scale_factor = 1.0; };
	bitmap { filename = "attention_task_20.png"; description = "D2_20"; preload = false; scale_factor = 1.0; };
	bitmap { filename = "attention_task_21.png"; description = "D2_21"; preload = false; scale_factor = 1.0; };
	bitmap { filename = "attention_task_22.png"; description = "D2_22"; preload = false; scale_factor = 1.0; };
	bitmap { filename = "attention_task_23.png"; description = "D2_23"; preload = false; scale_factor = 1.0; };
	bitmap { filename = "attention_task_24.png"; description = "D2_24"; preload = false; scale_factor = 1.0; };
	bitmap { filename = "attention_task_25.png"; description = "D2_25"; preload = false; scale_factor = 1.0; };
	bitmap { filename = "attention_task_26.png"; description = "D2_26"; preload = false; scale_factor = 1.0; };
	bitmap { filename = "attention_task_27.png"; description = "D2_27"; preload = false; scale_factor = 1.0; };
	bitmap { filename = "attention_task_28.png"; description = "D2_28"; preload = false; scale_factor = 1.0; };
	bitmap { filename = "attention_task_29.png"; description = "D2_29"; preload = false; scale_factor = 1.0; };
} d2_stimuli_images;

#cursor for left eye
ellipse_graphic { ellipse_height = 50; ellipse_width = 50; color = 0,255,0; } left_cursor;
      
#cursor for right eye
ellipse_graphic { ellipse_height = 50; ellipse_width = 50; color = 0,0,255; } right_cursor;

picture {    
	text{ 
		caption = "+";
	};     
	x = $xf; y = $yf;
} fix;

picture {    
	text{ 
  	   caption = "
Will start soon... As a reminder:

Code comprehension:
  - Left click: you know the output of the function
  - Right click: you do *not* know the output of the function


Bracket search:
  - Left click: you found a bracket ( or {


d2:
  - Left click: it is a "d" with exactly two lines
  - Right click: it is *not* a "d" with exactly two lines
";
	};
	x = $xf; 
	y = $yf;
} INSTRUCT;

picture {    
	text{ 
  	   caption = "
Last chance to click...
	";
	};
	x = $xf; 
	y = $yf;
} LAST_RESPONSE_CHANCE;

picture { 
	text {
		caption = "
Done :)

Please lay still for three more minutes for a post-measurement.

In the meantime, we may test the eye-tracker again.";
	}; 
	x = $xf; 
	y = $yf;
} THE_END;


############################ TRIALS_HELP ############################
trial {
	trial_duration = forever;
	trial_type = first_response;
	picture INSTRUCT; 
	time = 0; 
	code = "Instruct";
} INSTRUCT_T;   

trial {
	trial_duration = '$LastResponseChanceTime';
	picture LAST_RESPONSE_CHANCE;
	code = "LastResponseCondition";
} LastResponseCondition;

trial {
	trial_duration = 100;
	picture  fix;
	code = "WARTEN";
} WARTEN_T;

trial {
	trial_duration = '$RestConditionTime';
	picture  fix;
	code = "RestCondition";
} RestCondition;


#todo change to the correct time: trial_duration = 180000;
trial {
	trial_duration = 20000; # if eyetracking doesnt work 180000
	picture  THE_END ;
	code = "THE END";
} THE_END_T;

trial {
   picture {  
      # this is only a placeholder - the real image gets loaded dynamically in the loop further down
      box { height = 1; width = 1; color = 0,0,0; };
      x = 0; y = 0;  
   } stimulus_image;
	code = "code_placeholder"; 
} code_stimulus;

trial {    
   trial_duration = '$D2rTime';   
   picture {  
      # this is only a placeholder - the real image gets loaded dynamically in the loop further down
      box { height = 1; width = 1; color = 0,0,0; };
      x = 0; y = 0;  
   } d2_stimulus_image;
   duration = '$D2rTime'; 
   time = 0 ;
	code = "d2_placeholder"; 
} d2;

begin_pcl;

# todo change this for the real experiment to 58000 and 28000
int ComprehensionTime = 58000;
int SyntaxTime = 28000;

int x = 0;
int y = 0;

# todo change this for the real experiment to false or true
bool use_eyetracker = false;

# utility function returns the last button press
sub
	int  get_last_button_press_id(string buttonstr )
begin
	if buttonstr.count() >0 then
		array <string> starr[2];
		buttonstr.split(" ",starr);
		return int(starr[1]);	
	end;
		return 0;
end;

#file name cannot be longer than 8 characters
string edf_name = "pc4.edf";
if (logfile.subject().count() >0) then
	edf_name = "pc4_" + logfile.subject() + ".edf";
end;

#initialize PresLink.
eye_tracker tracker = new eye_tracker( "PresLink" );
	
if (use_eyetracker) then
	#connect to Eyelink tracker.
	tracker.start_tracking();

	string tracker_ver = tracker.get_parameter("tracker_version");

	#tracker_ver would be something like EYELINK CL 4.48, but we want to get the 4.48
	array <string> starr[5];
	tracker_ver.split(" ",starr);
	double tr_v = double(starr[3]);

	#open edf file on the tracker
	tracker.set_parameter("open_edf_file",edf_name);

	#set preamble
	tracker.send_command("add_file_preamble_text 'ProgCode4'");

	tracker.set_parameter("file_event_filter","LEFT,RIGHT,FIXATION,SACCADE,BLINK,MESSAGE,BUTTON,INPUT");		   
	tracker.set_parameter("link_event_filter","LEFT,RIGHT,FIXATION,SACCADE,BLINK,BUTTON");

	if (tr_v >=4.0) then
		tracker.set_parameter("link_sample_data","LEFT,RIGHT,GAZE,GAZERES,AREA,STATUS,HTARGET");
		tracker.set_parameter("file_sample_data","LEFT,RIGHT,GAZE,AREA,GAZERES,STATUS,HTARGET,INPUT");
	else
		tracker.set_parameter("link_sample_data","LEFT,RIGHT,GAZE,GAZERES,AREA,STATUS"); 
		tracker.set_parameter("file_sample_data","LEFT,RIGHT,GAZE,AREA,GAZERES,STATUS,INPUT");
	end;

	#program button #5 for use in drift correction
	tracker.send_command("button_function 5 'accept_target_fixation'");

	#tell the tracker to use 9 point calibration.
	#tracker.set_parameter("calibration_type","HV9");
	tracker.set_parameter("calibration_type","HV13");

	#tell PresLink that we need gaze data for both eyes (if available)
	tracker.start_data(et_left, dt_position, false);
	tracker.start_data(et_right, dt_position, false);
end;

if (use_eyetracker) then
	#-----------------------CALIBRATION----------------------	
	#et_calibration.set_background_color(153,153,153);
	et_calibration.set_background_color(0,0,0);
	et_calibration.clear(); 
	et_calibration.present();
	
	#start calibration with camera support
	tracker.calibrate( et_calibrate_default, 1.0, 0.0, 0.0 );

	#drift correct at (0,0) with the options to allow Camera Setup and to draw a target
	#tracker.calibrate( et_calibrate_drift_correct, 7.0, 0.0, 0.0 );
end;

# show the participant the task
INSTRUCT_T.present();

# wait for the fMRI trigger (needs to be scenario_type = fMRI;). Can simulate by pressing "T" on the keyboard
loop until (pulse_manager.main_pulse_count() == 1) begin end;

# start with an initial rest condition (currently there is no eyetracking in this initial rest)
RestCondition.present();

# TODO change this to 1860000
int experiment_time_maximum = 1860000; # 1860000
int experiment_time_end = clock.time() + experiment_time_maximum;
int syntax_counter = 0;

# then start the loop of stimuli
loop
   int i = 1
until
   clock.time() >= experiment_time_end || i > code_stimuli_images.count()
begin
	#load the images for displaying the code and d2 attention task.
	code_stimuli_images[i].load();
	stimulus_image.clear(); #remove all
	stimulus_image.add_part(code_stimuli_images[i],0,0); 
	
	d2_stimuli_images[i].load();
	d2_stimulus_image.clear(); #remove all
	d2_stimulus_image.add_part(d2_stimuli_images[i],0,0);
	
	string msg = "record_status_message 'TRIAL ";
	if (use_eyetracker) then
		#
		#Send viewer integration messages and tracker commands to monitor recording.
		#
		tracker.send_command("clear_screen 0");

		# This supplies the title at the bottom of the eyetracker display
		msg.append(string(i));
		msg.append("/");
		msg.append(string(code_stimuli_images.count()));
		msg.append("'");
		tracker.send_command(msg);

		# Always send a TRIALID message before starting to record.
		# It should contain trial condition data required for analysis.
		msg= "TRIALID TRIAL ";
		msg.append(string(i));
		tracker.send_message(msg);

		# TRIAL_VAR message is recorded for EyeLink Data Viewer analysis
		# It specifies the list of trial variables value for the trial
		# This must be specified within the scope of an individual trial (i.e., after
		# "TRIALID" and before "TRIAL_RESULT")
		msg = "!V TRIAL_VAR TRIAL_IMAGE ";
		msg.append(code_stimuli_images[i].filename());
		tracker.send_message(msg);

		# IMGLOAD command is recorded for EyeLink Data Viewer analysis
		# It displays a default image on the overlay mode of the trial viewer screen.
		# Writes the image filename + path info
		msg = "!V IMGLOAD FILL ";
		msg.append(code_stimuli_images[i].filename());
		tracker.send_message(msg);

		#set the the tracker to idle mode.
		tracker.send_command("set_idle_mode");
		#give some time for the tracker to switch mode.
		wait_interval(50);
		#start recording
		tracker.set_recording(true);
	end;

	# set the stimulus event to the code and then present the stimulus
	code_stimulus.get_stimulus_event(1).set_event_code( code_stimuli_images[i].description() );
	code_stimulus.present();  
	
	int eye_av = 0;
	int left_index = 2;
	int right_index = 3;
		
	if (use_eyetracker) then
		#mark the time we presented the stimulus
		tracker.send_message("SYNCTIME"); 
			
		#get the available eye.
		eye_av = int(tracker.get_parameter("eye_available"));
		left_index = 2;
		right_index = 3;
		if(eye_av == 0) then
			stimulus_image.add_part(left_cursor,0,0);
			left_index = 2;
			right_index = -1;
		elseif(eye_av == 1) then
			stimulus_image.add_part(right_cursor,0,0);
			right_index = 2;
			left_index = -1;
		else
			stimulus_image.add_part(left_cursor,0,0);
			stimulus_image.add_part(right_cursor,0,0);
		end;
	end;
	
	bool button_pressed = false;
	int response_count_start = response_manager.total_response_count();
	int minimum_clicks = 2;
	int maximum_time = ComprehensionTime;
	
	if (code_stimuli_images[i].description().find("Syn_") != 0) then
		if (syntax_counter == 0) then
			minimum_clicks = 16;
		elseif(syntax_counter == 1) then
			minimum_clicks = 26;
		elseif(syntax_counter == 2) then
			minimum_clicks = 14;
		elseif(syntax_counter == 3) then
			minimum_clicks = 22;
		elseif(syntax_counter == 4) then
			minimum_clicks = 24;
		else
			minimum_clicks = 20;
		end;
		
		maximum_time = SyntaxTime;
		syntax_counter = syntax_counter + 1
	end;
	
	loop
		int end_time = clock.time() + maximum_time
	until
		clock.time() >= end_time || button_pressed
	begin
		int response_count_end = response_manager.total_response_count();
		
		# if participant pressed a button -> move on in the experiment
		# for syntax snippets, many presses are necessary to move on
		if (response_count_end >= response_count_start + minimum_clicks) then
			button_pressed = true;
		end;
			
		bool overlay_eyetracking = false;
		if (overlay_eyetracking) then
			int modified = 0;
			#check for new button presses
			button_pressed = get_last_button_press_id(tracker.get_parameter("last_button_press"))!=0;
			
			if ((eye_av == 0 || eye_av == 2)) then
				#we have left data OR both eye data
				if(tracker.new_position_data(et_left) >0) then
					eye_position_data epd = tracker.last_position_data(et_left);
					stimulus_image.set_part_x( left_index, epd.x());
					stimulus_image.set_part_y( left_index, epd.y());
					modified = 1;
				end;
			end;	
			
			if ((eye_av == 1 || eye_av == 2)) then
				#we have right data OR both eye data
				if(tracker.new_position_data(et_right) >0) then
					eye_position_data epd = tracker.last_position_data(et_right);
					stimulus_image.set_part_x( right_index, epd.x());
					stimulus_image.set_part_y( right_index, epd.y());
					modified = 1;
				end;
			end;
			if(modified == 1) then
				code_stimulus.present();   
			end;
			modified = 0;
		end;
	end;
	
	if (!button_pressed) then
		if (use_eyetracker) then
			msg = "Last Response Condition ";
			msg.append(string(i));
			tracker.send_message(msg);
		end;
		
		LastResponseCondition.present();
	end;
	
	if (use_eyetracker) then
		msg = "D2 Task ";
		msg.append(d2_stimuli_images[i].description());
		tracker.send_message(msg);
	end;
		
	d2.get_stimulus_event(1).set_event_code( d2_stimuli_images[i].description() );
	d2.present(); 
	
	if (use_eyetracker) then
		msg = "Rest Condition ";
		msg.append(string(i));
		tracker.send_message(msg);
	end;
	
	#drift correct at (0,0) with the options to allow Camera Setup and to draw a target
	#tracker.calibrate(et_calibrate_drift_correct, 7.0, 0.0, 0.0 );
	RestCondition.present();
	
	stimulus_image.clear();
	stimulus_image.set_background_color(0,0,0);
	stimulus_image.present();
	wait_interval(100);
	#stop recording.
	
	if (use_eyetracker) then
		tracker.set_recording(false);
		
		msg= "TRIAL_RESULT ";
		msg.append(string(0));
		tracker.send_message(msg);
	end;

	d2_stimuli_images[i].unload();	
	code_stimuli_images[i].unload(); 
	i = i + 1
end;

THE_END_T.present();

# do a validation after the end of the experiment
if (use_eyetracker) then
	et_calibration.set_background_color(0,0,0);
	et_calibration.clear(); 
	et_calibration.present();
	
	#start calibration with camera support
	tracker.calibrate( et_calibrate_default, 1.0, 0.0, 0.0 );
end;

# experiment done, now transfer the file to the presentation computer
if (use_eyetracker) then
	#transfer the edf file. Note Presentation places files specified without a path in the user's home directory.
	#in this example pres_1.edf will be placed in your home directory. (eg. in xp C:\documents and settings\<username>
	string edf_fname = logfile_directory + edf_name;
	tracker.set_parameter("get_edf_file",edf_fname);
	tracker.stop_tracking();
end;