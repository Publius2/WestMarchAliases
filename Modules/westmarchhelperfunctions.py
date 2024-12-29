# helper
# collection of functions I use in aliases associated with my westmarch server they are often re inventing the wheel for things 
# that would be easy with the character functionality but I don't want to use that so I can be sure all users on my westmarch can use them
# 
# parser(args, tags)
#   takes the arguments in a function and prepende - if they are on the list of tags does args parse and returnse the parsed data
# 
# skillgenerator(name, modifier, advantage='normal')
#   returns a dict with values for a skills name, modifier, advantage/disadvantage status and roll string
#   my kingdom for the ability to use classes in draconic

def parser(args, tags):
    tagged_args = list(map(lambda x: f"{'-' if x in tags else ''}{x}", args))
    return argsparse(tagged_args)
    
def skillgenerator(name, modifier, advantage="normal"):
    roll = f"1d20+{modifier}"