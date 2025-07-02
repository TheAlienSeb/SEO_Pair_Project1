import json, pathlib
from pathlib import Path
import sys
project_root = Path(__file__).resolve().parent.parent        # …/SEO_Pair_Project1
DB_dir  = project_root / "DB_Conn"                      # …/SEO_Pair_Project1/DB_Conn
Scripts_dir = project_root / "Scripts"

sys.path.append(str(project_root))    # you already had this
sys.path.append(str(DB_dir))     # ← **add this line**
sys.path.append(str(Scripts_dir)) 

from DB import Grab_Titles
from Gemini import Call_Gemini
def Main():
    Grab_Titles()
    Call_Gemini()



if __name__ == "__main__":
    Main()









