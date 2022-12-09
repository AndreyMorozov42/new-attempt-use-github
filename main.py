import argparse

from calc.calc import Calc

def main(a, b, operation):
    c = Calc(a, b, operation)
    return c.result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calc two number")
    parser.add_argument("a", type=float)
    parser.add_argument("b", type=float)
    parser.add_argument("op", type=str)
    args = parser.parse_args()
    res = main(args.a, args.b, args.op)
    print(res)