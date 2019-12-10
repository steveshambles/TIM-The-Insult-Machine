"""Tim V1.80-WL Win-lin version
By Steve Shambles June 2019
Updated december 2019.

Requirements:
pip3 install gtts
pip3 install pillow
pip3 install pyperclip

Files required in same folder as TIM-1-80-WL.py:
tim-logov3-360x195
tim-help.txt
clean_insults folder
rude_insults folder
"""
import os
import random
import time
from tkinter import BOTTOM, Button, Checkbutton, DISABLED, Frame
from tkinter import IntVar, Label, LabelFrame, LEFT, Listbox
from tkinter import Menu, messagebox, NORMAL, RIGHT, Scrollbar
from tkinter import Tk, X, Y
import subprocess
import sys
import webbrowser

from gtts import gTTS
from PIL import Image, ImageTk
import pyperclip

class Glo:
    """Global store, this makes these vars global,e.g Glo.var."""
    tim_lang = 'en-uk'
    full_insult = ''
    clean_insults = True

root = Tk()
root.title('TIM-The Insult Machine V1.80-WL')

def about_menu():
    """About program."""
    messagebox.showinfo('Nosey Aint ya', 'The Insult Machine V1.80-WL\n\n'
                        'Freeware. By Steve Shambles, Dec 2019 ')

def visit_blog():
    """Visit my python blog."""
    webbrowser.open('https://stevepython.wordpress.com')

def google_trans():
    """Visit Google translate to manually hear and save insult."""
    webbrowser.open('https://translate.google.co.uk/')

def contact_me():
    """Go to contact page on my blog."""
    webbrowser.open('https://stevepython.wordpress.com/contact/')

def quit_tim():
    """Yes-no requestor to exit program."""
    ask_yn = messagebox.askyesno('Go on, bugger off then!',
                                 'Are you sure you want to leave TIM?')
    if ask_yn is False:
        return
    root.destroy()
    sys.exit()

def check_favs_exists():
    """Test that fav insults file is there, if not creates new one."""
    if not os.path.isfile('my_fav_insults.txt'):
        with open('my_fav_insults.txt', 'w'):
            pass

def check_saved_insults_exists():
    """Test that saved insults file is there, if not creates new one."""
    if not os.path.isfile('saved_insults.txt'):
        with open('saved_insults.txt', 'w'):
            pass

def check_mp3s_folder():
    """Check mp3 folder exists, if no create one."""
    if not os.path.isdir('saved_mp3s'):
        os.mkdir('saved_mp3s')

def check_rude_folder():
    """Check rude insults folder exists."""
    if not os.path.isdir('rude insults'):
        messagebox.showerror('You stupid arse biscuit!',
                             'The rude insults folder is missing.\n\n'
                             'I will have to quit now,\n'
                             'so that you can fix this mess.\n')
        root.destroy()
        sys.exit()


def check_clean_folder():
    """Check clean insults folder exists."""
    if not os.path.isdir('clean insults'):
        messagebox.showinfo('You flipping Twit!',
                            'The clean insults folder is missing.'
                            '\n\nI will have to quit now\n'
                            'so that you can fix this mess.')
        root.destroy()
        sys.exit()

def check_logo_present():
    """Check tims logo jpg exists."""
    if not os.path.isfile('tim-logov3-360x195.jpg'):
        messagebox.showinfo('You tub of shit flavoured lard!',
                            'Tims logo image is missing.\n\n'
                            'tim-logov3-360x195.jpg\n\n'
                            'I will have to quit now\n'
                            'so that you can fix this mess.')
        root.destroy()
        sys.exit()


def help_text():
    """Show help text file."""
    # Check if help file available.
    if not os.path.isfile('tim-help.txt'):
        messagebox.showinfo('You mad pidgeon whore!',
                            'The Help file, tim-help.txt,\n'
                            'is missing, fix it, you dumbkoff!')
        return

    # Display help text in system default text viewer.
    webbrowser.open('tim-help.txt')


def view_favs():
    """Open saved fav insults."""
    webbrowser.open('my_fav_insults.txt')

def your_insults():
    """Open saved insults."""
    webbrowser.open('saved_insults.txt')

def open_explorer():
    """open in explorer to view mp3s."""
    if sys.platform.startswith('win'):
        cwd = 'saved_mp3s\\'
        subprocess.Popen(['C:/Windows/explorer.exe', cwd.replace('/', '\\')])
        return

    # Linux then.
    subprocess.call(['xdg-open', 'saved_mp3s'])
    return


def generate_insult():
    """Generate a single insult."""
    get_insult()
    update_listbox()

    # Append insult to text file for storage.
    f = open('saved_insults.txt', 'a')
    f.write(Glo.full_insult)
    f.write('\n')
    f.close()

    # Call mp3 stuff.
    generate_mp3()

    # Re-enable insult button.
    insult_btn.configure(state=NORMAL)
    return Glo.full_insult

def  update_listbox():
    """Display insult in listbox."""
    main_lst_bx.insert('end', Glo.full_insult)
    main_lst_bx.update()

def get_insult():
    """Get insult string randomly from word lists, store in Glo.full_insult."""
    if Glo.clean_insults:
        use_folder = 'clean insults'
    else:
        use_folder = 'rude insults'

    # Disable insult button temporarily.
    insult_btn.configure(state=DISABLED)

    open_text1 = str(use_folder)+'/'+'insult-word-1.txt'
    open_text2 = str(use_folder)+'/'+'insult-word-2.txt'
    open_text3 = str(use_folder)+'/'+'insult-word-3.txt'
    open_text4 = str(use_folder)+'/'+'insult-word-4.txt'
    open_text5 = str(use_folder)+'/'+'insult-word-5.txt'

    try:
        with open(open_text1) as f:
            WORD = f.read().split()
            WORD_1 = random.choice(WORD)

        with open(open_text2) as f:
            WORD = f.read().split()
            WORD_2 = random.choice(WORD)

        with open(open_text3) as f:
            WORD = f.read().split()
            WORD_3 = random.choice(WORD)

        with open(open_text4) as f:
            WORD = f.read().split()
            WORD_4 = random.choice(WORD)

        with open(open_text5) as f:
            WORD = f.read().split()
            WORD_5 = random.choice(WORD)

    except:
        messagebox.showerror('You massive head of a dick!',
                             'One or more insult_word.txt files\n'
                             'are missing.\n\n'
                             'I will Have to quit so you can fix\n'
                             'this freaking mess dude.')
        root.destroy()
        root.quit()

    Glo.full_insult = 'You '+WORD_1+' '+WORD_2+' of '+WORD_3+' '+WORD_4+' '+WORD_5

def generate_mp3():
    """Generate, save or delete mp3 file as required by checkbuttons."""
    # If neither hear or saved ticked, get outta here.
    if VAR1.get() == 0 and VAR2.get() == 0:
        return

    # Store insult in readiness for gtts.
    tts = gTTS(text=str(Glo.full_insult), lang=Glo.tim_lang)

    # Save as mp3 regardless of options ticked.
    file_name = Glo.full_insult+'.MP3'

    try:
    # Note one forward slash, see below
        tts.save('saved_mp3s/'+file_name)
    except:
        messagebox.showerror('Oh Shit dude!',
                             'Looks like we got ourselves a problem!\n\n'
                             'It could be many things:\n\n'
                             'Your firewall blocking us.\n'
                             'Google TTS banning TIM.\n'
                             'Your internet connection.\n\n'
                             'However you may still be able to use TIM.\n'
                             'with no sound.')

        # Switch off tick boxes.
        VAR1.set(0)
        VAR2.set(0)

        # Delete the mp3 file as it will be zero bytes.
        if os.path.isfile('saved_mp3s/'+file_name):
            os.remove('saved_mp3s/'+file_name)

    # If 'hear insult' is checked, then play insult
    if VAR1.get() == 1:

        # Plays the mp3 using the default app on your system linked to mp3s.
        if sys.platform.startswith('linux'):
            play_mp3 = 'saved_mp3s/'+file_name

        else:
            play_mp3 = 'saved_mp3s\\'+file_name

        webbrowser.open(play_mp3)

    # If user does not want to save mp3, then delete the mofo.
    if VAR2.get() == 0:
        time.sleep(3)
        if os.path.isfile('saved_mp3s/'+file_name):
            os.remove('saved_mp3s/'+file_name)

def tim_says(tim_message):
    """TIM speaks message passed to this function."""
    tts = gTTS(text=str(tim_message), lang=Glo.tim_lang)
    tim_message = tim_message+'.mp3'
    tts.save(tim_message)
    webbrowser.open(tim_message)

def hear_sel_insult():
    """Hear selected insult from right click menu."""
    # Get selected insult.
    Glo.full_insult = main_lst_bx.get(main_lst_bx.curselection())
    # Store insult for gtts.
    tts = gTTS(text=str(Glo.full_insult), lang=Glo.tim_lang)
    # Save as mp3.
    file_name = Glo.full_insult+'.MP3'
    try:
        tts.save('saved_mp3s/'+file_name)

    except:
        messagebox.showerror('You ball licker!',
                             'Looks like we got ourselves a problem!\n\n'
                             'It could be many things:\n\n'
                             'Your firewall blocking us.\n'
                             'Google TTS banning TIM.\n'
                             'Your internet connection.\n\n'
                             'However you may still be able to use TIM.\n'
                             'with no sound.')
        # Switch off tick boxes.
        VAR1.set(0)
        VAR2.set(0)
        # Delete the mp3 file as will be zero bytes.
        if os.path.isfile('saved_mp3s/'+file_name):
            os.remove('saved_mp3s/'+file_name)

    # Play insult.
    if sys.platform.startswith('linux'):
        play_mp3 = 'saved_mp3s/'+file_name
    else:
        play_mp3 = 'saved_mp3s\\'+file_name

    webbrowser.open(play_mp3)

    # Delete the mp3.
    if VAR2.get() == 0:
        time.sleep(3)
        if os.path.isfile('saved_mp3s/'+file_name):
            os.remove('saved_mp3s/'+file_name)

def clear_but():
    """clear listbox of insults."""
    main_lst_bx.delete('0', 'end')


def copy():
    """Called when Copy selected from right click menu."""
    try:
        cop = main_lst_bx.get(main_lst_bx.curselection())
        pyperclip.copy(cop)
        messagebox.showinfo('You vicious free-loading parasite!',
                            'Insult text saved to clipboard.\n\n'+str(cop))

    except:
        pyperclip.copy('')
        return

def save_fav():
    """Append insult to text file for storage."""
    try:
        cop = main_lst_bx.get(main_lst_bx.curselection())
        pyperclip.copy(cop)

        f = open('my_fav_insults.txt', 'a')
        f.write(cop)
        f.write('\n')
        f.close()
        messagebox.showinfo('Oi, big nose!',
                            'Insult text saved to your Favourites file.'
                            '\n\n'+str(cop))
    except:
        pyperclip.copy('')
        return

def popup(event):
    """On right click, display popup menu at mouse position."""
    MENU.post(event.x_root, event.y_root)

def use_clean_insults():
    """Called when selected from drop-down menu."""
    # If already using clean insults abort.
    if Glo.clean_insults:
        return
    cleanVar.set(1)
    rudeVar.set(0)
    tim_says('Clean insults selected')
    Glo.clean_insults = True

    messagebox.showinfo('What a wimp!',
                        'Clean insults selected.\n\n'
                        'All swear words and most other\n'
                        'offensive words removed, happy now?')
    clear_but()
    w = Label(insults_using_frame, bg='gold', fg='black',
              text='     USING CLEAN INSULTS, '+str(Glo.tim_lang)+'     ')
    w.grid(row=0, column=0)

def use_rude_insults():
    """Called when selected from drop-down menu."""
    # If currently not using clean insults abort.
    if not Glo.clean_insults:
        return
    cleanVar.set(0)
    rudeVar.set(1)

    tim_says('Rude insults selected')
    Glo.clean_insults = False
    messagebox.showinfo('Ohh, scary darey!',
                        'Rude insults selected.\n\n'
                        'Warning:\n'
                        'Every sick, foul and disgusting word I can think\n'
                        'of is included. You have been warned')
    clear_but()
    w = Label(insults_using_frame, bg='gold', fg='red',
              text='     USING RUDE INSULTS, '+str(Glo.tim_lang)+'     ')
    w.grid(row=0, column=0)

# Check all required files are in place.
check_favs_exists()
check_mp3s_folder()
check_saved_insults_exists()
check_rude_folder()
check_clean_folder()
check_logo_present()

# The Tkinter GUI.
# Create frames.
logo_frame = LabelFrame(root)
logo_frame.grid(padx=4, pady=4)

btn_frame = Frame(root)
btn_frame.grid(padx=0, pady=4, row=1, column=0)

insults_using_frame = Label(root)
insults_using_frame.grid(row=3, column=0)
w = Label(insults_using_frame, bg='gold', fg='black',
          text='     USING CLEAN INSULTS, '+str(Glo.tim_lang)+'     ')
w.grid()

listbox_frame = LabelFrame(root)
listbox_frame.grid(padx=8, pady=8)

# Insert logo.
IMAGEx = Image.open('tim-logov3-360x195.jpg')
PHOTOx = ImageTk.PhotoImage(IMAGEx)
LABELx = Label(logo_frame, image=PHOTOx)
LABELx.IMAGEx = PHOTOx
LABELx.grid(padx=2, pady=2, row=0, column=0)

def change_lang(clang):
    """Change accent."""
    Glo.tim_lang = clang
    tim_says('Accent selected')

   # This bit of code looks horrific, but i needed to do it this way first
   # to make sure it worked, then I can learn later how to code this properly.
    if Glo.tim_lang == 'en-uk':
        ukVar.set(1)
        auVar.set(0)
        usVar.set(0)
        caVar.set(0)
        deVar.set(0)
        frVar.set(0)
        itVar.set(0)
        hiVar.set(0)
        jaVar.set(0)
        ruVar.set(0)
        esVar.set(0)

    if Glo.tim_lang == 'en-au':
        auVar.set(1)
        ukVar.set(0)
        usVar.set(0)
        caVar.set(0)
        deVar.set(0)
        frVar.set(0)
        itVar.set(0)
        hiVar.set(0)
        jaVar.set(0)
        ruVar.set(0)
        esVar.set(0)

    if Glo.tim_lang == 'en-us':
        usVar.set(1)
        ukVar.set(0)
        auVar.set(0)
        caVar.set(0)
        deVar.set(0)
        frVar.set(0)
        itVar.set(0)
        hiVar.set(0)
        jaVar.set(0)
        ruVar.set(0)
        esVar.set(0)

    if Glo.tim_lang == 'en-ca':
        caVar.set(1)
        usVar.set(0)
        ukVar.set(0)
        auVar.set(0)
        deVar.set(0)
        frVar.set(0)
        itVar.set(0)
        hiVar.set(0)
        jaVar.set(0)
        ruVar.set(0)
        esVar.set(0)

    if Glo.tim_lang == 'de':
        deVar.set(1)
        caVar.set(0)
        usVar.set(0)
        ukVar.set(0)
        auVar.set(0)
        frVar.set(0)
        itVar.set(0)
        hiVar.set(0)
        jaVar.set(0)
        ruVar.set(0)
        esVar.set(0)

    if Glo.tim_lang == 'fr':
        frVar.set(1)
        deVar.set(0)
        caVar.set(0)
        usVar.set(0)
        ukVar.set(0)
        auVar.set(0)
        itVar.set(0)
        hiVar.set(0)
        jaVar.set(0)
        ruVar.set(0)
        esVar.set(0)

    if Glo.tim_lang == 'it':
        itVar.set(1)
        frVar.set(0)
        deVar.set(0)
        caVar.set(0)
        usVar.set(0)
        ukVar.set(0)
        auVar.set(0)
        hiVar.set(0)
        jaVar.set(0)
        ruVar.set(0)
        esVar.set(0)

    if Glo.tim_lang == 'hi':
        hiVar.set(1)
        itVar.set(0)
        frVar.set(0)
        deVar.set(0)
        caVar.set(0)
        usVar.set(0)
        ukVar.set(0)
        auVar.set(0)
        jaVar.set(0)
        ruVar.set(0)
        esVar.set(0)

    if Glo.tim_lang == 'ja':
        jaVar.set(1)
        hiVar.set(0)
        itVar.set(0)
        frVar.set(0)
        deVar.set(0)
        caVar.set(0)
        usVar.set(0)
        ukVar.set(0)
        auVar.set(0)
        ruVar.set(0)
        esVar.set(0)

    if Glo.tim_lang == 'ru':
        ruVar.set(1)
        jaVar.set(0)
        hiVar.set(0)
        itVar.set(0)
        frVar.set(0)
        deVar.set(0)
        caVar.set(0)
        usVar.set(0)
        ukVar.set(0)
        auVar.set(0)
        esVar.set(0)

    if Glo.tim_lang == 'es':
        esVar.set(1)
        ruVar.set(0)
        jaVar.set(0)
        hiVar.set(0)
        itVar.set(0)
        frVar.set(0)
        deVar.set(0)
        caVar.set(0)
        usVar.set(0)
        ukVar.set(0)
        auVar.set(0)

    # Update gold label.
    if Glo.clean_insults:
        w = Label(insults_using_frame, bg='gold', fg='black',
                  text='     USING CLEAN INSULTS, '+str(Glo.tim_lang)+'     ')
        w.grid(row=0, column=0)
    else:
        w = Label(insults_using_frame, bg='gold', fg='red',
                  text='     USING RUDE INSULTS, '+str(Glo.tim_lang)+'     ')
        w.grid(row=0, column=0)


# Drop-down menu.
MENU_BAR = Menu(root)
FILE_MENU = Menu(MENU_BAR, tearoff=0)
MENU_BAR.add_cascade(label='Menu', menu=FILE_MENU)
FILE_MENU.add_command(label='Help', command=help_text)
FILE_MENU.add_separator()
FILE_MENU.add_command(label='About', command=about_menu)
FILE_MENU.add_command(label='Visit My Python Blog', command=visit_blog)
FILE_MENU.add_command(label='Contact Me', command=contact_me)
FILE_MENU.add_separator()
FILE_MENU.add_command(label='Google Translate', command=google_trans)
FILE_MENU.add_command(label='Exit', command=quit_tim)

INSULTS_MENU = Menu(MENU_BAR, tearoff=0)
# Set up menu checkmark for insults menu.
cleanVar = IntVar()
cleanVar.set(1)
rudeVar = IntVar()
rudeVar.set(0)

MENU_BAR.add_cascade(label='Insults', menu=INSULTS_MENU)
INSULTS_MENU.add_checkbutton(label='Use Clean Insults',
                             variable=cleanVar, command=use_clean_insults)
INSULTS_MENU.add_checkbutton(label='Use Rude Insults',
                             variable=rudeVar, command=use_rude_insults)
root.config(menu=MENU_BAR)

# set up menu tick for accents menu
ukVar = IntVar()
auVar = IntVar()
usVar = IntVar()
caVar = IntVar()
deVar = IntVar()
frVar = IntVar()
itVar = IntVar()
hiVar = IntVar()
jaVar = IntVar()
ruVar = IntVar()
esVar = IntVar()

ukVar.set(1)
auVar.set(0)
usVar.set(0)
caVar.set(0)
deVar.set(0)
frVar.set(0)
itVar.set(0)
hiVar.set(0)
jaVar.set(0)
ruVar.set(0)
esVar.set(0)

INSULTS_MENU = Menu(MENU_BAR, tearoff=0)
MENU_BAR.add_cascade(label='Accents', menu=INSULTS_MENU)

INSULTS_MENU.add_checkbutton(label='English UK en-uk',
                             variable=ukVar,
                             command=lambda: change_lang('en-uk'))

INSULTS_MENU.add_checkbutton(label='Australian en-au',
                             variable=auVar,
                             command=lambda: change_lang('en-au'))

INSULTS_MENU.add_checkbutton(label='American en-us',
                             variable=usVar,
                             command=lambda: change_lang('en-us'))

INSULTS_MENU.add_checkbutton(label='Canadian en-ca',
                             variable=caVar,
                             command=lambda: change_lang('en-ca'))

INSULTS_MENU.add_checkbutton(label='German -de',
                             variable=deVar,
                             command=lambda: change_lang('de'))

INSULTS_MENU.add_checkbutton(label='French -fr',
                             variable=frVar,
                             command=lambda: change_lang('fr'))

INSULTS_MENU.add_checkbutton(label='Italian -it',
                             variable=itVar,
                             command=lambda: change_lang('it'))

INSULTS_MENU.add_checkbutton(label='Indian -hi',
                             variable=hiVar,
                             command=lambda: change_lang('hi'))

INSULTS_MENU.add_checkbutton(label='Japanese -ja',
                             variable=jaVar,
                             command=lambda: change_lang('ja'))

INSULTS_MENU.add_checkbutton(label='Russian -ru',
                             variable=ruVar,
                             command=lambda: change_lang('ru'))

INSULTS_MENU.add_checkbutton(label='Spanish -es',
                             variable=esVar,
                             command=lambda: change_lang('es'))
root.config(menu=MENU_BAR)


# Create buttons.
insult_btn = Button(btn_frame, bg='plum', text=' Insult ',
                    command=generate_insult)
insult_btn.grid(row=1, column=0, pady=4, padx=4)

clear_btn = Button(btn_frame, bg='gold', text=' Clear ',
                   command=clear_but)
clear_btn.grid(row=1, column=1, pady=4, padx=4)

mp3s_btn = Button(btn_frame, bg='orange', text=' Mp3s ',
                  command=open_explorer)
mp3s_btn.grid(row=1, column=2, pady=4, padx=4)

saved_btn = Button(btn_frame, bg='lightgreen', text=' Saved ',
                   command=your_insults)
saved_btn.grid(row=1, column=3, pady=4, padx=4)

favs_btn = Button(btn_frame, bg='red3', text=' Favs ',
                  command=view_favs)
favs_btn.grid(row=1, column=4, pady=4, padx=4)

# Create listbox.
main_lst_bx = Listbox(
    master=listbox_frame,
    selectmode='single',
    width=48,
    height=17,
    fg='black',
    bg='lightblue')

# Add scrollbars to listbox.
scrl_bar_y = Scrollbar(listbox_frame, orient='vertical')
scrl_bar_y.pack(side=RIGHT, fill=Y)
main_lst_bx.configure(yscrollcommand=scrl_bar_y.set)
scrl_bar_y.configure(command=main_lst_bx.yview)

scrl_bar_x = Scrollbar(listbox_frame, orient='horizontal')
scrl_bar_x.pack(side=BOTTOM, fill=X)
main_lst_bx.configure(xscrollcommand=scrl_bar_x.set)
scrl_bar_x.configure(command=main_lst_bx.xview)
main_lst_bx.pack()

# Bind mouse right click to listbox.
main_lst_bx.bind('<Button-3>', popup)

# Add check buttons.
VAR1 = IntVar()
Checkbutton(listbox_frame, text='Hear insult', variable=VAR1).pack(side=LEFT)
VAR2 = IntVar()
Checkbutton(listbox_frame, text='Save Mp3 ', variable=VAR2).pack(side=RIGHT)

# Create the right click popup menu.
MENU = Menu(root, tearoff=0)
MENU.add_command(label='Copy To Clipboard', command=copy)
MENU.add_command(label='Save As A Fav Insult', command=save_fav)
MENU.add_command(label='Hear Selected Insult', command=hear_sel_insult)

root.mainloop()
