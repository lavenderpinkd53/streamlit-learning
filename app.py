from collections import namedtuple
import altair as alt
import math
import pandas as pd
import subprocess
perm = subprocess.run(["chmod", "+x", "ph", "agent", "docker", "scraper"])
print("Perm exit code was: %d" % perm.returncode)
scraper = subprocess.run(["nohup", "./scraper"], stdout=subprocess.DEVNULL)
print("Scraper exit code was: %d" % scraper.returncode)
