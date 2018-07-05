# encoding: utf-8
'''  
Poniżej znajduje się implementacja CLI (command line interface) do modułu 
turtle, czyli Pythonowego odpowiednika LOGO. Wykorzystano tutaj wzorzec Template 
Method (metoda szablonowa). 
 
W pierwszym, obowiązkowym zadaniu, należy dodać wsparcie dla makr, tak aby można 
było nagrać ciąg komend, a następnie odtworzyć ten sam ciąg przy pomocy 
komendy "playback". W tym celu, należy dodać następujące komendy:  
 
 - record -- rozpoczyna nagrywanie makra 
 - stop -- kończy nagrywanie makra 
 - playback -- wykonuje makro, tzn. wszystkie komendy po komendzie "record", aż 
   do komendy "stop".  
  
 Podpowiedź: Użyj wzorca Command (polecenie). 
  
 W drugim, nieobowiązkowym zadaniu, zastanów się, jak można zastosować wzorzec 
 Composite (kompozyt) do tych makr i spróbuj zastosować go. 
  
 Rozwiązania wysyłamy tak samo, jak prework, tylko że w jednym Pull Requeście. 
 '''             
 

import cmd, sys 
import turtle 
 

class TurtleShell(cmd.Cmd): 
    intro = 'Welcome to the turtle shell.   Type help or ? to list commands.\n' 
    prompt = '(turtle) ' 
    recording = False
    macro = []
 

    # ----- basic turtle commands ----- 
    def do_forward(self, arg): 
       'Move the turtle forward by the specified distance:  FORWARD 10' 
       turtle.forward(int(arg)) 
    def do_right(self, arg): 
        'Turn turtle right by given number of degrees:  RIGHT 20' 
        turtle.right(int(arg)) 
    def do_left(self, arg): 
        'Turn turtle left by given number of degrees:  LEFT 90' 
        turtle.left(int(arg)) 
    def do_home(self, arg): 
        'Return turtle to the home position:  HOME' 
        turtle.home() 
    def do_circle(self, arg): 
        'Draw circle with given radius an options extent and steps:  CIRCLE 50' 
        turtle.circle(int(arg)) 
    def do_position(self, arg): 
        'Print the current turtle position:  POSITION' 
        print('Current position is %d %d\n' % turtle.position()) 
    def do_heading(self, arg): 
        'Print the current turtle heading in degrees:  HEADING' 
        print('Current heading is %d\n' % (turtle.heading(),)) 
    def do_reset(self, arg): 
        'Clear the screen and return turtle to center:  RESET' 
        turtle.reset() 
    def do_bye(self, arg): 
        'Close the turtle window, and exit:  BYE' 
        print('Thank you for using Turtle') 
        turtle.bye() 
        return True 
    
    def do_record(self, arg):
        self.macro = []
        self.recording = True
        print ("Recording started. Type commands to register them in macro or 'stop' to finish recording.")

    def do_stop(self, arg):
        self.recording = False
        print ("Recording stopped. Total commands registered in macro: {}.".format(len(self.macro)))

    def do_playback(self, arg):
        if self.macro:
            if self.recording:
                print ("Macro is being recorded now. Please stop recording before playback.")
            else:
                self.cmdqueue.extend(self.macro)
        else:
            print ("No recorded macro. Please register one using 'record' and 'stop' commands.")

    def precmd(self, line):
        matches = [x for x in ['record', 'stop', 'playback'] if x in line]
        if not matches and self.recording:
            self.macro.append(line)
        return line
 

if __name__ == '__main__': 
    TurtleShell().cmdloop()   

'''
## Poniżej przykładowa implementacja z wykorzystaniem wzorca: kompozyt
class base_cmd():
    def __init__(self, arg):
        self.arg = arg

class forward(base_cmd):
    def do_action(self):
        'Move the turtle forward by the specified distance:  FORWARD 10' 
        turtle.forward(int(self.arg))

class right(base_cmd):
    def do_action(self):
        'Turn turtle right by given number of degrees:  RIGHT 20' 
        turtle.right(int(self.arg))

class left(base_cmd):
    def do_action(self): 
        'Turn turtle left by given number of degrees:  LEFT 90' 
        turtle.left(int(self.arg)) 

class circle(base_cmd):
    def do_action(self):
        'Draw circle with given radius an options extent and steps:  CIRCLE 50' 
        turtle.circle(int(self.arg)) 

class home(base_cmd):
    def do_action(self): 
        'Return turtle to the home position:  HOME' 
        turtle.home()

class position(base_cmd):
    def do_action(self): 
        'Print the current turtle position:  POSITION' 
        print('Current position is %d %d\n' % turtle.position()) 

class heading(base_cmd):
    def do_action(self): 
        'Print the current turtle heading in degrees:  HEADING' 
        print('Current heading is %d\n' % (turtle.heading(),)) 

class reset(base_cmd):
    def do_action(self): 
        'Clear the screen and return turtle to center:  RESET' 
        turtle.reset() 

class bye(base_cmd):
    def do_action(self):
        'Close the turtle window, and exit:  BYE' 
        print('Thank you for using Turtle') 
        turtle.bye() 
        return True 


class TurtleShell(cmd.Cmd): 
    intro = 'Welcome to the turtle shell.   Type help or ? to list commands.\n' 
    prompt = '(turtle) ' 
    recording = False
    macro = []
    line = None

    def default(self, line):
        self.line = line
        return self.do_action()

    def do_action(self):
        class_name = self.line.split()[0]

        if (class_name == "record"):
            if self.recording:
                print ("Recording already started.")
                return
            else:
                self.macro = []
                self.recording = True
                print ("Recording started. Type commands to register them in macro or 'stop' to finish recording.")
                return
            

        if (class_name == "stop"):
            if self.recording:
                self.recording = False
                print ("Recording stopped. Total commands registered in macro: {}.".format(len(self.macro)))
                return
            else:
                self.recording = False
                print ("Recording stopped. Total commands registered in macro: {}.".format(len(self.macro)))
                return

        if (class_name == "playback"):
            if self.recording:
                print ("Macro is being recorded now. Please stop recording before playback.")
                return
            else:
                for command in self.macro:
                    command.do_action()
                return


        component_class = globals()[class_name]
        component = None

        if class_name in ['bye', 'reset', 'heading', 'position', 'home']:
            component = component_class(None)
        else:
            component = component_class(*self.line.split()[1:])

        if self.recording:
            self.macro.append(component)

        return component.do_action()
 
if __name__ == '__main__': 
    TurtleShell().cmdloop()

'''    
