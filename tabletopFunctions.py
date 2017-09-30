# this section holds tabletop functions such as rolling or stat generation
import discord # allows use of discord functions here
import random


async def stat_gen(message, client):
    strstat = random.randint(1, 6) + random.randint(1, 6) + 6
    constat = random.randint(1, 6) + random.randint(1, 6) + 6
    dexstat = random.randint(1, 6) + random.randint(1, 6) + 6
    intstat = random.randint(1, 6) + random.randint(1, 6) + 6
    wisstat = random.randint(1, 6) + random.randint(1, 6) + 6
    chastat = random.randint(1, 6) + random.randint(1, 6) + 6
    
    await client.send_message(message.channel, "Generating stats using a 2d6 + 6 method...")
    await client.send_message(message.channel, "**STR:** %s \n**CON:** %s \n**DEX:** %s \n**INT:** %s \n**WIS:** %s \n**CHA:** %s" % (strstat, constat, dexstat, intstat, wisstat, chastat))
    

async def rolling_dice(message, client):
	try:
		processString = message.content
		print(processString)
		processString = processString.replace("!roll", "")
		processString = processString.replace(" ", "")
		print(processString)
		processString = processString.strip()
		print(processString)
		syntaxDChcker = processString.index('d') # verfies a d is in the string
		diceModExist = False
		modType = 0
		monIndex = -1
		# check if there is a mod
		for a in processString:
			if a == "+":
				modIndex = processString.index("+")
				modType = 1
				diceModExist = True
				break
			elif a == "-":
				modIndex = processString.index("-")
				modType = -1
				diceModExist = True
				break

		if diceModExist == True:
			print("Dice mod exists.")
		else:
			print("No dice modifier.")

       
		totalRoll = 0 # so it can be used later

		if diceModExist == False:
        	# there is no dice mod, easy
			print(syntaxDChcker)
			numberOfDice = processString[0:syntaxDChcker]
			numberOfDice = int(numberOfDice)
			print(numberOfDice)
			diceNumber = processString[syntaxDChcker+1:]
			diceNumber = int(diceNumber)
			print(diceNumber)
			numRollsSoFar = 0
			totalRoll = 0
    
			while numRollsSoFar < numberOfDice:
				totalRoll = totalRoll + random.randint(1, diceNumber)
				numRollsSoFar = numRollsSoFar + 1
		else:
	    	# there is a dice mod
			numberOfDice = processString[0:syntaxDChcker]
			numberOfDice = int(numberOfDice)
			diceNumber = processString[syntaxDChcker+1:modIndex]
			diceNumber = int(diceNumber)
			modNumber = processString[modIndex+1:]
			modNumber = int(modNumber)

			numRollsSoFar = 0
			totalRoll = 0
    
			while numRollsSoFar < numberOfDice:
				totalRoll = totalRoll + random.randint(1, diceNumber)
				numRollsSoFar = numRollsSoFar + 1
	        # apply modifier
			if modType == 1:
				totalRoll = totalRoll + modNumber
			elif modType == -1:
				totalRoll = totalRoll - modNumber

		print("completed rolling")
	    # now we print it out
		await client.send_message(message.channel, "Rolling... your result is %s" % totalRoll)

	except ValueError:
		await client.send_message(message.channel, "Please use the proper syntax; you are lacking the d:\n[number of dice to roll]d[faces of the die]\nExample: 12d6\nAdditional Variants:\n[number of dice to roll]d[faces of the die] (+/-) [dice modifier]\nExample: 12d6 + 13\nExample: 2d16 - 7")
		
	
	except Exception:
		await client.send_message(message.channel, "Something went wrong, please ensure you are using the proper syntax:\n[number of dice to roll]d[faces of the die]\nExample: 12d6\nAdditional Variants:\n[number of dice to roll]d[faces of the die] (+/-) [dice modifier]\nExample: 12d6 + 13\nExample: 2d16 - 7")
		await client.send_message(message.channel, "If this is not the source of your error, please screenshot your error and PM it to the bot. The developer will look at it later.")