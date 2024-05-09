<p align="center" text-align="center">
  <img src="https://raw.githubusercontent.com/La-Compagnie-Infonuagique/selfdiffusion/aca5dc131f3162c2a0817a38a7d95b836a7faefc/assets/selfdiffusion.jpg" alt="self diffusion">
</p>

<div align="center">
  <h1>JAAC</h1>
</div>

# JAAC
The Job Application Assets Creator

## Summary
JAAC is a CLI tools that uses LLM and a templating engine to create custom job application assets such as CV and cover letter.

For JAAC to work for you, you will need to provide it with:

1. an openrouter.ai API key.
2. a user context, which is all the information that one would normally find in a C.V. 

The 

## Installation
```bash
# install jaac from pypi.
pip install jaac
```

After installation and before using for the first time, initialize JAAC with the following:

```bash
# fill in the values of the example config file afterwards.
jaac init
```

This will generate a jaac config file (jaac.conf.example). Provide the required values and rename it jaac.conf and
you'll be good to go.

For more information, see the online doc.

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
