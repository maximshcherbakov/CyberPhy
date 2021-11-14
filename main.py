# This is a the main script for testing CyberPhy package.
# Maxim Shcherbakov
# 13/11/21

import cyberphyChangeDetector.cyberphyChangeDetectorUnit
from cyberphyChangeDetector.cyberphyChangeDetectorUnit import changeDetection

def print_hi(name):
    print(f'Hereby the message, {name}')


if __name__ == '__main__':
    print_hi('Welcome to CyberPhy main file')
    changeDetection()

