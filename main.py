import rich
import pyfiglet
from rich.console import Console


title = pyfiglet.figlet_format('Ciphera', 'big')

def main_menu():
    console = Console()
    console.print(f'[red]{title}[/red]', style='bold')
    
    console.print('[red]Choose what to do:[/red]')
    console.print('[red]1.   Generate Password[/red]')
    console.print('[red]2.   Add Password[/red]')
    console.print('[red]3.   Password List[/red]')
    option = console.input('[red][1,2,3]> [/red]')


if __name__=='__main__':
    main_menu()