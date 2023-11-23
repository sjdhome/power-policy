#!/usr/bin/env python3
import sys, os

def set_governor(governor: str) -> bool:
	return os.system(f"cpupower frequency-set -g {governor}") == 0

def set_intel_epb(value: int) -> bool:
	return os.system(f"cpupower set -b {value}") == 0

def powersave() -> bool:
	print(f"{set_governor('powersave')=}")
	print(f"{set_intel_epb(15)=}")

def performance():
	print(f"{set_governor('performance')=}")
	print(f"{set_intel_epb(0)=}")

def show_help(program_path: str):
	print(f"usage: {program_path} performance/powersave")

def main(args: list[str]):
	if len(args) > 1:
		if args[1] == "powersave":
			powersave()
		elif args[1] == "performance":
			performance()	
	else:
		show_help(args[0])

if __name__ == "__main__":
	main(sys.argv)
