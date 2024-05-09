<p align="center" text-align="center">
<img src="./assets/jaac.jpg" alt="JAAC" width="500px">
</p>
<blockquote>
    <p> "In this twisted wonderland of ours, it takes every ounce of your strength, every bit of your resolve, 
    just to maintain the position and stand still." -- The Red Queen </p>
</blockquote>

# JAAC
The Job Application Assets Creator

JAAC is a CLI tools that uses LLM and a templating engine to create custom job application assets such as CVs and cover letters.

## Installation
```bash
# jaac is available on pypi
pip install jaac
```

Before using for the first time, initialize JAAC:

```bash
jaac init
```

**IMPORTANT**: This will create a few files that you will need to modify and rename *before* using.

## Configuration
jaac init creates the following files:

1. jaac.config.toml.example
2. cv.tex.template.example
3. letter.tex.template.example
4. profile.txt.example

The general procedure is to modify these files and remove the .example extension. 
Once proper values are set, you can use any jaac commands. 

### jaac.config.toml.example
This file contains the app config such as an API key to interact with LLM, 
the system templates used for the generation of cv, cover letters and direct messages, the path to 
the cv and letter templates to use etc.


## Usage
``` bash
# create a CV personalized for the job you are applying to.
jaac cv offer.txt cv.pdf

# create a cover letter for the fob
jaac letter offer.txt letter.pdf

# generate a chat message to a recruiter that you can send, for example, on linkedin
jaac msg offer.txt 
```

offer.txt contains the text description of the job offer. Something you will probably copy and 


## Author
Jonathan Pelletier (jonathan.pelletier-aafz@thecloudco.ca)
