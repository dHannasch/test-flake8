import os
import requests  # noqa We are just importing this to prove the dependency installed correctly


def main():
    my_input = os.environ["INPUT_MYINPUT"]

    my_output = f"Hello {my_input}"

    print(f"::set-output name=myOutput::{my_output}")


def E111():
  pass

# Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor

if __name__ == "__main__":
    main()
