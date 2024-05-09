import click
import os
import shutil
import tomllib

from .llm import simple_completion
from .pdf import to_pdf

@click.group()
def cli():
    pass

@cli.command(help="Initialize the jaac configuration.")
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


def asset_content(conf, asset_name, offer):
    ASSET_NAME = asset_name.upper()

    # load required options from config file
    api_key = conf['ai']['OPEN_ROUTER_API_KEY']
    model = conf['ai']['MODEL']
    system_prompt = conf['ai']['prompts'][ASSET_NAME]
    profile_loc = conf['profile']['LOCATION']

    # read the offer
    with open(offer, 'r') as f:
        offer_txt = f.read()

    # read the user profile
    with open(profile_loc, 'r') as f:
        profile_txt = f.read()

    user_prompt = f"{offer_txt}\n{profile_txt}"

    # generate the cv summary
    summary = simple_completion(
        api_key, 
        model, 
        system_prompt, 
        user_prompt
    )
    return summary

def asset(conf_loc, asset_name, print_raw ,offer, destination):

    conf = load_config(conf_loc)
    summary = asset_content(conf, asset_name, offer)
    asset_template_loc = conf['templates'][asset_name]['LOCATION']

    if print_raw:
        print(summary)
    
    to_pdf(summary, asset_template_loc, destination)


@cli.command(help="Generate a CV from an offer file.")
@click.argument('offer')
@click.argument('destination')
@click.option('--print-raw', is_flag=True, help="Print the raw output of the AI model.", default=False)
def cv(offer, destination, print_raw) :
    asset('jaac.config.toml', 'cv', print_raw , offer, destination)
    return

@cli.command(help="Generate a cover letter from an offer file.")
@click.argument('offer')
@click.argument('destination')
@click.option('--print-raw', is_flag=True, help="Print the raw output of the AI model.", default=False)
def letter(offer, destination, print_raw):
    asset('jaac.config.toml', 'letter', print_raw, offer, destination)
    return


@cli.command(help="Generate a direct message to send recruiter from an offer file.")
@click.argument('offer')
def dm(offer):
    conf = load_config('jaac.config.toml')
    dm = asset_content(conf, 'dm', offer)
    click.echo(dm)
    return