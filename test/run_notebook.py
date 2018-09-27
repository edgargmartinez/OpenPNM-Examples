# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 13:57:34 2018
Testing wrapper for ipython notebooks
https://blog.thedataincubator.com/2016/06/testing-jupyter-notebooks/
@author: Tom Tranter
"""
import os
import subprocess
import tempfile


def _notebook_run(path):
    """Execute a notebook via nbconvert and collect output.
       :returns (parsed nb object, execution errors)
    """
    dirname, __ = os.path.split(path)
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
        args = ["jupyter", "nbconvert", "--to", "notebook", "--execute",
                "--ExecutePreprocessor.timeout=360",
                "--output", fout.name, path]
        proc = subprocess.run(args)
        rc = proc.returncode
    return rc


def test_ipynb():
    rootdir = os.path.split(os.getcwd())[0]
    for path, subdirs, files in os.walk(rootdir):
        for name in files:
            if (name.endswith('.ipynb') and 'checkpoint' not in name):
                nbook = os.path.join(path, name)
                rc = _notebook_run(nbook)
                print(nbook, rc)
                assert rc == 0

if __name__ == '__main__':
    test_ipynb()
