import json
import main

event = json.load(open('dados.json'))

main.main(event)



