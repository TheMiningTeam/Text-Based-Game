from lib.Tqdm.tqdm import tqdm
from time import sleep

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

whatToLoad = tqdm(['Files', 'Code', 'Variabels', 'NPCs', 'Items', 'Locations', 'Text', 'Pant', 'Weeb Sh*t', 'GUI'])
def loading():
    # Initial "Loading bar" 
    with tqdm(total=100) as pbar:
        for loading in whatToLoad:
            if loading == 'GUI':
                for i in range(9):
                    sleep(0.1)
                    if i == 8: # Making the bar red at 99%
                        pbar.update(1)
                        pbar.set_description(f'{bcolors.FAIL}Loading %s' % loading)    
                        break
                    pbar.update(1)
                    pbar.set_description(f'{bcolors.WARNING}Loading %s' % loading)    
                break
            for i in range(10):
                sleep(0.1)
                pbar.update(1)
                pbar.set_description(f'{bcolors.WARNING}Loading %s' % loading)

    sleep(0.1)
    print(f"\n{bcolors.FAIL}'GUI' failed to load.")
    sleep(1.2)
    print(f'\n{bcolors.FAIL}Reverting to latest usable state.{bcolors.WARNING}\n')
    for i in tqdm(range(int(2e6))):
        pass
    sleep(0.1)
    print(f'\n{bcolors.OKGREEN}Usable state found.')
    sleep(1.2)
    print(f'\nLoading from state.{bcolors.WARNING}\n')
    sleep(1.2)
    for i in tqdm(range(int(2e6))):
        pass
    sleep(1.2)
    print()