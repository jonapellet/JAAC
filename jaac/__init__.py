import click
import os
import shutil
import tomllib

@click.group()
def cli():
    pass

@cli.command()
def init():

    # get the current directory based on the current filename
    source_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), "documents")
    destination_folder = os.getcwd()


    for filename in os.listdir(source_folder):
        source = os.path.join(source_folder, filename)
        destination = os.path.join(destination_folder, filename)
        shutil.copy2(source, destination)

    # Provide instructions to the user
    click.echo("jaac examples files created. Modify accordingly and remove .example before issuing jaac commands.")

    return

# handle commands that need configuration
# first define the config loading logic
def load_config(loc):
    try:
        with open(loc, 'rb') as f:
            config = tomllib.load(f)
        return config
    except FileNotFoundError:
        print(f"Config file '{loc}' not found. Make sure you ran 'jaac init' first and saved your config file as jaac.config.toml.")
        exit(-1)

@cli.command(help="Generate a CV from an offer file.")
@click.argument('offer')
@click.argument('destination')
def cv(offer, destination):
    """
    Generate a CV from an offer file.

    Args:
        offer (str): Path to the offer file.
        destination (str): Path to the destination file.
        output_format (str): Output format of the CV (pdf or txt).

    Returns:
        None
    """
    conf = load_config('jaac.config.toml')
    print(conf)
    return

@cli.command(help="Generate a cover letter from an offer file.")
def letter():
    click.echo("Generating cover letter from offer file.")
    return






