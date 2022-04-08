import re
import os
import time
import random
import argparse
import sys
import signal
import rich
from .readmd import readmd
from .responses import RESPONSES
from rich.console import Console
from rich.progress import track
from rich.markdown import Markdown
from rich.traceback import install
install()

console = Console()

parser = argparse.ArgumentParser(prog='galact',
        usage='%(prog)s (subcommands) [options]',
        epilog="Have fun with the chatbot!",
        description='Galact is a command line ai that can be used to interact with the user in a more natural way.')
subparsers = parser.add_subparsers()


# Global Variables Here... keep this to a minimum


quit_text = ['quit', 'exit']

class Galact():
    def __init__(self):
        #never change thing right above
        
        console.print('Hello!:wave:, I am [bold cyan]Galact[/bold cyan]')
        console.print('[underline]A bot[/] made by [green]Abso[/][blue]zero[/], using re.')
        console.print('Make sure to have fun!', style="bold underline blue")
        console.print('enter [underline][bold red]\'quit\' or \'exit\'[/underline], [/bold red] to exit the program')
        print(os.getcwd())
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

def readme(): 
    os.chdir(os.path.join(os.path.dirname(__file__)))
    f = open('README.md', 'r')
    mark = f.read()
    console.print(Markdown(mark))


parser_galact = subparsers.add_parser('run', help='Run galact on cli')
parser_galact.set_defaults(func=Galact)

parser_abt = subparsers.add_parser('about', help='Give info about Galact.')
parser_abt.set_defaults(func=about)

parser_read = subparsers.add_parser('readme', help='Show the readme of galact.')
parser_read.set_defaults(func=readme)

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
