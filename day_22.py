import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--value", type=float, help="Temperature value")
parser.add_argument("--unit", choices=["c2f", "f2c"], help="Conversion type")

args = parser.parse_args()

if args.unit == "c2f":
    result = (args.value * 9/5) + 32
    print(f"{args.value}°C = {result:.2f}°F")
else:
    result = (args.value - 32) * 5/9
    print(f"{args.value}°F = {result:.2f}°C")
