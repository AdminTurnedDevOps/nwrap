import os

import typer

cli = typer.Typer()

@cli.command()
def ipscan(ipaddress: str):
    os.system(f"nmap -sn {ipaddress}")

@cli.command()
def ipport(port: int, ipaddress: str):
    os.system(f"nmap -p {port} {ipaddress}")

@cli.command()
def scaniprange(iprange: str):
    os.system(f"nmap -sn {iprange}")

@cli.command()
def scaniprangeport(port: int, iprange: str):
    os.system(f"nmap -p {port} {iprange}", port, iprange)

if __name__ == '__main__':
    cli()