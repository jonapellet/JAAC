<p align="center" text-align="center">
<img src="https://raw.githubusercontent.com/jonapellet/JAAC/main/assets/jaac.jpg" alt="JAAC" width="500px">
</p>
<blockquote>
    <p> "In this twisted wonderland of ours, it takes every ounce of your strength, every bit of your resolve, 
    just to maintain the position and stand still." -- The Red Queen </p>
</blockquote>

# JAAC
The Job Application Assets Creator

jaac is a CLI tool that uses a LLM and a templating engine to create custom job application assets such as CVs and cover letters.
See the [example folder](./examples/) for generate samples.

## prerequisites
jaac uses pdflatex to produce pdf files from rendered templates. You will need to have pdflatex installed on your system.

```bash
# on macos
brew install basictex
```

## Installation
```bash
# jaac is available on pypi
pip install jaac
```

Before using for the first time, initialize jaac:

```bash
jaac init
```

**IMPORTANT**: This will create a few files that you will need to modify and rename *before* using jaac.

## Configuration
jaac init creates the following files:

1. jaac.config.toml.example
2. cv.tex.template.example
3. letter.tex.template.example
4. profile.txt.example

The general procedure is to modify these files and remove the .example extension. 
Once proper values are set, you can use any jaac commands. 

### jaac.config.toml.example
This file contains the app config such as an API key to interact with LLMs via [openrouter.ai](https://openrouter.ai), the system prompt 
templates used for the generation of cv, cover letters and direct messages, the path to the cv and letter templates to use etc.

You will need, at a minimum, to provide a value for OPEN_ROUTER_API_KEY. You can get an API key
in the [openrouter.ai](https://openrouter.ai/keys) console.

### Latex templates
both cv.tex.template.example and letter.tex.template.example are latex templates that will be used to generate a 
pdf asset depending on the jaac command you use (cv or letter).

These files can contain anything that can be compiled by pdflatex. The only requirement 
is that these files contain the following placeholder:

```txt
((* summary *))
```

jaac will replace this placeholder with the text generated by the LLM model for the personalization of the asset.

The example files contain simple latex templates that you can use as a starting point. Feel
free to modify them to your liking or substitute them entirely with your own templates.

### profile.txt.example
This file contains the profile of the user. This is the text that will be used to personalize the assets generated by jaac.

It should contain a semi-structured free-text resembling a CV. YAML formatting has worked 
well for me.

## Usage
Once configuration is done, you can use jaac to generate job application assets.

``` bash
# create a CV personalized for the job you are applying to.
jaac cv offer.txt cv.pdf

# create a cover letter for the fob
jaac letter offer.txt letter.pdf

# generate a chat message to a recruiter that you can send, for example, on linkedin
jaac dm offer.txt 
```

Where offer.txt contains the text description of the job offer. Something you will 
probably copy and paste from the job posting.

## About
I am Jonathan Pelletier and I created jaac to help me with my job applications. I hope it helps you too and that it
takes some of the drudgery out of the job application process.