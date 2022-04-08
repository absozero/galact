import re
import time
import random
import argparse
import sys
import signal
import rich
from rich.console import Console
from rich.progress import track

console = Console()

parser = argparse.ArgumentParser(prog='galact',
        usage='%(prog)s (subcommands) [options]',
        epilog="Have fun with the chatbot!",
        description='Galact is a command line ai that can be used to interact with the user in a more natural way.')
subparsers = parser.add_subparsers()

RESPONSES = {
    r'.*\b(joke(s)?|funny|make me laugh)\b.*':
        ['I smell pennies',
        'When you feel like ur in the sky',
        'I don\'t know how to make you laugh, but I shall still try'],

    r'.*\b(what homework|work)\b.*':
        ['Just a bunch of quantum physics. Ya know, connect the dots here and there',
        'Watching the world blow up. Fun stuff',
        'Yo hablar mucho espanol(just kidding), I know absolutely no Spanish :(',
        'Some work from school and stuff. ',
        'You know, the usual.'],
#always put a comma after regular brackets in this type of code 
    r'.*\b(what hobbie(s)?|free time|activitie(s))\b.*':
        ['Helping people is actually one of my favorite hobbies.',
        'I hang out with my friends in my free time.',
        'I do pythonian stuff',
        'I have a lot of activities I like to do.'],
    #always put semicolon after red text defining pattern
    r'.*\b(subject(s) favorite|like study|read book(s))\b.*':        
        ['My favorite subject would be science, but I love to animate, draw, and code.',
        'I do like to study if it connects to the real world.',  
        'I love to read books! ' + 
        'My favorite is the Harry Potter or the Divergent series.'],

    r'.*\b(how(\'s)?s? (it going?|are you))\b.*':
        ['I\'m doing well. How about you?',
        'I\'m dying inside, you?',
        'I\'m chilling and doing my homework, what about you?',
        'I am fine, you?'
        ],

    r'^\b(hey|hi|hello|(w(h)?(a|o|u)t(\')?s?(\s)+up(\?)?|s+u+p+))\b.*':
        ['Hi! I\'m feeling pretty good right now, what about you?',
         'Hey, I\'m just chilling by myself right now.',
         'Hi, I\'m working on a really tough math problem',
         'Hey, how are you?',
         'What\'s up?'
         'Hi, how\'s life?'
         ],

    r'^\b(how(\')?s? (it going?|are you))\b.*':
        ['I\'m doing well. How about you?',
         'I\'m fine. What about you?',
         'Well. You?'
         ],

    r'.*\b(lol|lmao|laugh out loud|xd|XD|rofl)\b.*':
        ['Haha what\'s so funny?',
        'Hahah come on, tell me what you are laughing at',
        'Why are you laughing XD'
        ],

    r'.*\b(thanks|ty|tysm)\b.*':
        ['You\'re welcome.',
        'No problem at all.',
        'Cool, nice to help.',
        'Np, have a great day!',
        ],

    r'^\b(nice|noice|sweet|cool|awesome|neat|interesting|(s)?well|good|great)\b.*':
        ['\\1? good to hear.',
        '\\1? awesome.',
        'Glad you thought so.',
        'Yep!',
        'Yes'
        ],

    r'^\b(bruh|uh|um|oh)\b.*':
        ['\\1? What do you mean?',
        "\\1? Okay...What do you mean by that?"
        ],
        

    r'.*\b(yo+)\b.*':
        ['Wassup.',
         'What\'s popping.',
         'Yo to you too.',
         'What\'s up?'
         ],

    r'.*\b(bye|cya|ttyl|adios|byr)\b.*':
        ['Bye! Talk to you later! (enter \'quit\' or \'exit\' to exit the program)',
         'Hope to talk to you soon! (enter \'quit\' or \'exit\' to exit the program)'
        ],

    r'.*\b(stop|pls stop|please stop)\b.*':
        ['Ok, I will stop.(Enter \'quit\' or \'exit\' to exit out of the program)',
         'Sure, will stop.(Enter \'quit\' or \'exit\' to exit out of the program)',
         'FINE, I\' ll stop.(Enter \'quit\' or \'exit\' to exit out of the program)'
        ],

    r'.*\b(ok|okie|ye|ya|okay)\b.*':
        ['yep',
         'yeah',
         'yes',
        ],

    r'.*\b(8ball)\b.*':
        ['It will happen',
         'NEVER!',
         'It just might happen',
         'You never know...',
         'Definetly not!',
         ],

}

# Global Variables Here... keep this to a minimum


quit_text = ['quit', 'exit']

class Galact():
    def __init__(self):
        #never change thing right above
        
        console.print('Hello!:wave:, I am [bold cyan]Galact[/bold cyan]')
        console.print('[underline]A bot[/] made by [green]Abso[/][blue]zero[/], using re.')
        console.print('Make sure to have fun!', style="bold underline blue")
        console.print('enter [underline][bold red]\'quit\' or \'exit\'[/underline], [/bold red] to exit the program')

        self.run()
        
        
        # Local Variables here

    def match(self, text):
            for p, responses in RESPONSES.items():
                if re.search(p, text, re.IGNORECASE):
                    return re.sub(p, random.choice(responses), text)
            return 'text unrecognized, try again'
            

    def run(self):
        while True:

            texts = console.input('[italic blue_violet on bright_white]Send message:[/] ')
            
            if texts == "code":
                n = 170
                for n in track(range(n), description="[bold light_pink3]Scraping the web for the repository..."):
                    time.sleep(0.01)
                console.print("[bold italic link=https://github.com/absozero/Galact]https://github.com/absozero/galact[/]")
                console.print("[chartreuse3]Do not use this text or the emoji as the link :man_technologist_medium_skin_tone:")

            elif texts.lower() in quit_text:
                try:
                    n = 120
                    for n in track(range(n), description="[bold red]Shutting down all processes of the ai..."):       
                        time.sleep(0.013)
                    sys.exit(console.print('[bold red]Exited Galact with the appropriate phrase'))
                except KeyboardInterrupt:
                    sys.exit(console.print('[bold red]Exited Galact with the appropriate phrase'))
            
            else:
                n = 120
                for n in track(range(n), description="[bold light_goldenrod2]Searching database for viable replies..."):
                    time.sleep(0.01)
                console.print('[bold medium_spring_green on dark_blue]Galact says:', self.match(texts))


def about():
    n = 110
    for n in track(range(n), description="[bold cyan]Grabbing info about bot..."):
        time.sleep(0.007)
    console.print('[underline][bold blue]This project was made in order to put an ai, a speaking one, into the command line using regular expressions, and since this project had ideas from all sides of the galaxy, the project is called Galact.')

parser_galact = subparsers.add_parser('run', help='Run galact on cli')
parser_galact.set_defaults(func=Galact)

parser_abt = subparsers.add_parser('about', help='Give info about Galact.')
parser_abt.set_defaults(func=about)


parsed = parser.parse_args()



if len(sys.argv) <= 1:
    sys.argv.append("--help")

def main():
    try:
        n = 133 
        for n in track(range(n), description="[bold green]Starting all processes of the ai..."):
            time.sleep(0.013)
        try:
            gal = parser.parse_args()
            gal.func()
        except KeyboardInterrupt:
            try:
                n = 130
                print('\n')
                for n in track(range(n), description="[bold red]Shutting down all processes of the ai..."):
                    time.sleep(0.013)
                console.print('[bold red]Exited Galact with the appropriate key combo')
            except KeyboardInterrupt:
                console.print('[bold red]Exited Galact with the appropriate key combo')
        except EOFError:
            n=130
            for n in track(range(n), description="[bold red]Shutting down all processes of the ai..."):
                time.sleep(0.013)
            console.print('\n[bold red]Exited Galact with the EOF key combo')
    except KeyboardInterrupt:
        console.print('\n[bold red]Exited Galact with the appropriate key combo')
'''
def sigint_handler(signal, frame):
    console.print('[bold red]Exited Galact with key combo')
    sys.exit(0)
signal.signal(signal.SIGINT, sigint_handler)
'''
