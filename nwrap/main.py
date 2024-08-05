import os

import typer

cli = typer.Typer()

@cli.command()
def ipscan(ipaddress: str):
    os.system("nmap -sn %s", ipaddress)

@cli.command()
def ipport(port: int, ipaddress: str):
    os.system("nmap -p %d %s", port, ipaddress)

@cli.command()
def scaniprange(iprange: str):
    os.system("nmap -sn %s", iprange)

@cli.command()
def scaniprangeport(port: int, iprange: str):
    os.system("nmap -p %d %s", port, iprange)

if __name__ == '__main__':
    cli()