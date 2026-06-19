"""Simple demo CLI for practice/run.py"""

import argparse

# module-level value
a = 10


def get_value():
	"""Return the current module value."""
	return a


def main():
	parser = argparse.ArgumentParser(description="Demo CLI for practice/run.py")
	parser.add_argument("--value", action="store_true", help="print the value of 'a'")
	parser.add_argument("--set", type=int, help="set a new value and print it")
	args = parser.parse_args()

	if args.set is not None:
		print(args.set)
	elif args.value:
		print(get_value())
	else:
		print("Hello from run.py. Use --value to print 'a' or --set N to print N.")


if __name__ == "__main__":
	main()
b = 12
print(b+a)