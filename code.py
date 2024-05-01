import os, sys
os.system("git pull")
try:
    __import__("my_tool_for_encode").menu()
except Exception as e:
    exit(str(e))
