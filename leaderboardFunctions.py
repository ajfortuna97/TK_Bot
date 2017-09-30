import discord 
import MySQLdb
import _mysql

async def view_leader(message, client, db):
	#db.query("""SELECT * FROM leaderboard ORDER BY plusones LIMIT 1""")
	cursor = db.cursor()
	cursor.execute("SELECT * FROM leaderboard ORDER BY plusones LIMIT 1")
	topLeader = cursor.fetchone()
	topLeaderName = str(topLeader[0])
	topLeaderScore = str(topLeader[1])
	print("Retrieved top 1...")
	print(topLeaderName)
	print(topLeaderScore)
	await client.send_message(message.channel, ":crown: The Current Leader Is :crown:: \n**%s**, with %s +1s" % (topLeaderName, topLeaderScore))
