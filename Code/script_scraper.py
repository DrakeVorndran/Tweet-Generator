
scriptname = 'deadpool_complete_script.txt'
character = 'DEADPOOL:'
script = open(scriptname)
output = open(character+'_lines', 'w+')
for line in script:
  if line[:len(character)] == character:
    output.write(line[len(character):])