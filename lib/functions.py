#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")


def greet(name):
    print(f"Hello, {name}!")


greet("Ivan")


def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
print(greet_with_default())


def add(num1, num2):
    return num1 + num2



def halve(number):
    return number / 2
