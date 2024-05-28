#!/usr/bin/env python3
from collections import deque
import argparse

def parse_input(filename):
    mazes = []
    with open(filename, "r") as file:
        while True:
            header = file.readline().strip()
            if header == '0':
                break
            m, n, start_x, start_y, end_x, end_y = map(int, header.split())
            grid = []
            for _ in range(m):
                grid.append(list(map(int, file.readline().strip().split())))
            mazes.append((m, n, start_x, start_y, end_x, end_y, grid))
    return mazes

def main():
    # Setup del parser de argumentos
    parser = argparse.ArgumentParser(description="Parse and solve jumping mazes.")
    parser.add_argument("filename", type=str, help="The filename of the maze input.")
    
    # Parsear los argumentos
    args = parser.parse_args()

    # Procesar el archivo de entrada
    try:
        mazes = parse_input(args.filename)
        for maze in mazes:
            print(maze)
    except FileNotFoundError:
        print(f"Error: El archivo '{args.filename}' no se encuentra.")

if __name__ == "__main__":
    main()