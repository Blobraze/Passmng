import rich
from rich.console import Console

title = '''
  _____ _       _                    
 / ____(_)     | |                   
| |     _ _ __ | |__   ___ _ __ __ _ 
| |    | | '_ \| '_ \ / _ \ '__/ _` |
| |____| | |_) | | | |  __/ | | (_| |
 \_____|_| .__/|_| |_|\___|_|  \__,_|
         | |                         
         |_|                         
'''

def main_menu():
    console = Console()
    console.print(f'[red]{title}[/red]', style='bold')
    
    console.print(f'[red]Choose what to do:[/red]')
    console.print(f'[red]1.   Generate Password[/red]')
    console.print(f'[red]2.   Add Password[/red]')
    console.print(f'[red]3.   Password List[/red]')
    option = console.input(f'[red][1,2,3]> [/red]')


if __name__=='__main__':
    main_menu()
