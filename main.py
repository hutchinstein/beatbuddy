import time
import rtmidi

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()
print(type(available_ports))
print(available_ports)
if available_ports:
    print("Trying ports...")
    #midiout.open_port(available_ports.index("USB MIDI Interface MIDI 1 28:0"))
    #midiout.open_port(available_ports.index("Midi Through:Midi Through Port-0 14:0"))
    midiout.open_port(available_ports.index("USB MIDI Interface:USB MIDI Interface MIDI 1 20:0"))
    print("Success!")
else:
    midiout.open_virtual_port("My vitual output")



with midiout:
    print("Now controlling BeatBuddy...")
    #a = c0
    #song = [0xc0, 0, 112]
    #tempo = [0xfa, 0, 112]
    ## 0xc0 song selection
    ## 0xfa start song
    #fortybpm = [176, 107, 0]
    #midiout.send_message(song)
    #time.sleep(.1)
    #midiout.send_message(tempo)
    
    # TEMPOS might be 

    #for i in range(176,177):
        #for j in range(80,88):
            #for l in range(0,5):
                #print("working on it...")
                #test = [i, j, l]
                #try:
                    #midiout.send_message(test)
                    #print(i, j, l)
                    #time.sleep(1)
                #except rtmidi._rtmidi.SystemError:
                    #continue
    

    ### What I thought was forty bpm is really increasing BPM by 15 [176,80,15]
    ### It appears the last number is the amount to increase the current BPM in
    ### Increase BPM = [176, 80, # of BPM to increase]
    ### Decrease BPM = [176, 81, # of BPM to decrease]
    ### Set song to first song in first folder = [192, 0, 0]
    ### To change the song, change the third number, i.e. [192, 0, 1] 

    song = [192, 20, 20]
    midiout.send_message(song)
    increase = [176,80,20]
    #time.sleep(.1)
    ##tempo = [0xfa, 0, 112]
    input("Press enter to increase tempo 20 BPM...")
    midiout.send_message(increase) #CCR Down on the... normal tempo is 108
    decrease = [176, 81, 20]
    input("Press enter to decrease tempo 20 BPM...")
    midiout.send_message(decrease) #CCR Down on the... normal tempo is 108
    input("Press enter to advance to the next song...")
    song = [192, 0, 3] 
    midiout.send_message(song)
    #time.sleep(.1)
    #decrease = [176, 81, 10]
    #midiout.send_message(decrease)
del midiout
print("Exiting BeatBuddy...")
