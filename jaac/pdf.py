import os
import subprocess
from jinja2 import Environment, FileSystemLoader
import tempfile

def render_template(context, template_loc):

    template_dir = os.path.dirname(template_loc)
    template_name = os.path.basename(template_loc)

    # create jinja2 templat env
    env = Environment(
        loader=FileSystemLoader(template_dir),
        block_start_string='(%%',
        block_end_string='%%)',
        variable_start_string='((*',
        variable_end_string='*))',
        comment_start_string='(#',
        comment_end_string='#)'
    )

    # load the template
    template = env.get_template(template_name)

    # render the template using the context
    rendered = template.render(context)
    return rendered

def compile_latex(tex: str, output_loc: str):

    # create a temporary directory
    with tempfile.TemporaryDirectory() as temp_dir:
        # save content to file in the temporary directory
        temp_path = os.path.join(temp_dir, 'artifact.tex')
        with open(temp_path, 'w') as f:
            f.write(tex)

        # pdf latex command
        command = ["pdflatex", "-interaction=nonstopmode", "-output-directory", temp_dir, temp_path]

        # Execute the command with subprocess, with stdin, stdout, and stderr appropriately piped
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if result.returncode != 0:
            raise Exception(f"Error compiling latex: {result.stderr}")

        # move the artifact.pdf to the desired location
        artifact_path = os.path.join(temp_dir, 'artifact.pdf')
        os.rename(artifact_path, output_loc)

    return

def to_pdf(summary, template_loc, destination):
    # render the summary using the template
    rendered = render_template({'summary':summary}, template_loc)
    # compile the rendered template to pdf
    compile_latex(rendered, destination)

    return