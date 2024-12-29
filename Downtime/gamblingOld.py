embed <drac2>
footer = ' ' + get_svar('footer', default='')
DC = '2d10+5'
actions = ["Insight","Deception","Intimidation","Game Set"]
rolls = ["1d20","1d20","1d20","1d20"]
inds = [20,20,20,20]
flags = [0,0,0,0]
name = str("&1&")
weeks = int("&2&") if "&2&".strip("+-").isdigit() else 1
bet = int("&3&") if "&3&".strip('+-').isdigit() else 10
output = f'-title "Gambling"'
win = int(0)
if &ARGS&:
 args = [f'{"-" if x in ["ins","dec","int","game","reliable"] else ""}{x.lower() if x in ["ins","dec","int","game","reliable"] else x}' for x in &ARGS&]
 parsed = argparse(args)
 for x in &ARGS&:
  if x.lower() == "lucky":
   for y in range(4):
    rolls[y] += "ro1"
  rolls[1] += 'mi10' if x.lower() == 'silvered' else ''
 if parsed.get('reliable'):
  reliableskills = parsed.get('reliable')[0].split(',')
  rolls[0] += "mi10" if 'ins' in reliableskills else ''
  rolls[1] += "mi10" if 'dec' in reliableskills and 'mi10' not in rolls[1] else ''
  rolls[2] += "mi10" if 'int' in reliableskills else ''
  rolls[3] += "mi10" if 'game' in reliableskills else ''
 extraskills = 0
 extraskills += 1 if parsed.get('int') else 0
 extraskills += 1 if parsed.get('ins') else 0
 extraskills += 1 if parsed.get('dec') else 0
 extraskills += 1 if parsed.get('game') else 0
 if extraskills >3:
  output += ' -desc "choose only three insight, intimidation, deception, or gaming set."' + footer
  return output
 if extraskills <3:
  output += ' -desc "must choose 3 skills: insight, intimidation, deception, or gaming set."' + footer
  return output
 if parsed.get('ins'):
  flags[0] = 1
  rolls[0] += '+' + str(parsed.get('ins')[0])
 if parsed.get('dec'):
  flags[1] = 1
  rolls[1] += '+' + str(parsed.get('dec')[0])
 if parsed.get('int'):
  flags[2] = 1
  rolls[2] += '+' + str(parsed.get('int')[0])
 if parsed.get('game'):
  flags[3] = 1
  rolls[3] += '+' + str(parsed.get('game')[0])
 finalrolls = []
 finalactions = []
 ii = 0
 for x in flags:
  if x:
   finalrolls.append(rolls[ii])
   finalactions.append(actions[ii])
  ii += 1
 for x in range(weeks):
  output += f' -f "**Week {x+1}:**'
  suc = 0
  for y in range(3):
   form = finalrolls[y]
   dc = vroll(DC)
   roll_it = vroll(form)
   if roll_it.total >= dc.total:
    suc += 1
   output += f'\nRolling {finalactions[y]} {roll_it} versus {dc}'
  win += int(bet) if suc == 3 else floor(int(bet)/2) if suc == 2 else -floor(int(bet)/2) if suc == 1 else -2*int(bet)
  output += f'\n{suc} success{"es" if suc == 0 or suc > 1 else ""}: {name} {f"loses the bet they made of {bet} gp and accrue debt of {bet} gp." if suc == 0 else f"has a partial failure, losing {floor(int(bet))/2} gp. " if suc == 1 else f"has a partial success, getting {floor(int(bet))/2} gp. " if suc == 2 else f"succeeds and gets {bet} gp."}"'
 output += f' -f "{name} spends {weeks} weeks gambling {f"winning a total of {win} gp." if win>0 else f"loosing a total of {0-win}"}"'
else:
 output = f' -desc "`!gambling [char-name] [# of weeks] [Bet] [ins/dec/int/game] [modifier]`\nPair up the roll indicator ins/dec/int/game with the appropriate modifier. For example:\n`!gambling \'Doc Pseudopolis\' 3 500 ins 6 dec 10 int 10 reliable dec,int`\nAppend silvered to apply silver tongued to deception.\nAppend reliable followed by ins,dec,int no spaces including only the skills you are proficient in\nAppend lucky, if you are a Halfling."'
output += footer
return output
</drac2>