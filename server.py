#!/usr/bin/env python

from flask import Flask, jsonify
import os
import re

app = Flask(__name__, 
            static_url_path='/s',
            static_folder='static/')

@app.route('/history')
def history():
  cmds = []
  def make_cmd((ts, cmd)):
    ts = re.sub(":( |0)",'', ts)
    cmds.append((ts, cmd.strip('\n')))

  path = os.path.expanduser("~/.zsh_history")
  for line in open(path):
    line = line.split(';')
    if len(line) == 2:
      make_cmd(line)
  return jsonify(cmds or [])


if __name__ == '__main__':
  app.run(debug=True)

