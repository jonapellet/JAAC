<p align="center" text-align="center">
<img src="./assets/jaac.jpg" alt="JAAC" width="500px">
</p>
<blockquote>
    <p> "In this twisted wonderland of ours, it takes every ounce of your strength, every bit of your resolve, 
    just to maintain the position and stand still."</p>
</blockquote>

# JAAC
The Job Application Assets Creator

JAAC is a CLI tools that uses LLM and a templating engine to create custom job application assets such as CVs and cover letters.

For JAAC to work for you, you will need to provide it with:

1. an openrouter.ai API key.
2. a user context, which is all the information that one would normally find in a C.V. 

The 

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

For more information see the documentation

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
