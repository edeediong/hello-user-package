#!/usr/bin/env python
"""A CLI tool built with Click """

import click

@click.command()
@click.option("--greeting", default='Hello',help="How do you want to greet?")
@click.option("--name", default="World", help="Who do you want to greet?")
def greet(greeting, name):
    print(f"{greeting} {name}")

if __name__ == '__main__':
    greet()
