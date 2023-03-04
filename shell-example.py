import requests
import sys
import getopt
import sys
import getopt
import re
from rich import print
from rich.padding import Padding
from rich.panel import Panel
from rich import print
from rich.layout import Layout
from rich.align import Align
from rich.console import Console
from rich.text import Text

def escape_ansi(line):
    ansi_escape =re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
    return ansi_escape.sub('', line)

def command_name():
    command_name = None

    argv = sys.argv[1:]

    try:
        opts, args = getopt.getopt(argv, "c:", "command_name =")

    except:
        print("Error")

    for opt, arg in opts:
      opt = opt.strip()
      if opt in ['-c', '--command_name']:
          url = f"http://cheat.sh/{arg}"
          payload = "ls"
          headers = {
          'Content-Type': 'text/plain'
          }
          console = Console()
          layout = Layout()

          response = requests.request("GET", url, headers=headers, data=payload)
          tldr_text = escape_ansi(response.text).split("tldr:")[1]
          command_title = tldr_text.split("\n")[0]
          command_title_text = Text(command_title)
          command_title_text.stylize("bold blue")
          command_title = Align.center(command_title_text, vertical="middle")
          layout.split_column(
            Layout(name="upper"),
            Layout(name="lower")
          )
          layout["upper"].size = 11
          layout["upper"].update(Panel(command_title))
          layout["lower"].update(Panel(tldr_text))
#          layout["upper"].size=25
#          layout["lower"].size=15
#          layout["upper"].update(tldr_text)
          layout = Padding(layout, (4,0,0,0))
          print(layout)

command_name()

