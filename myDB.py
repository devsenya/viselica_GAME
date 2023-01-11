import json
import os
class FoobarDB(object):

	def __init__(self , location):
		self.location = os.path.expanduser(location)
		self.load(self.location)   

	def load(self , location):
		if os.path.exists(location):
			self._load()
		else:
			self.db = {}
		return True   

	def _load(self):
		self.db = json.load(open(self.location , "r"))   

	def dumpdb(self):
		try:
			json.dump(self.db , open(self.location, "w+"))
			return True
		except:
			return False

	def set(self, key, value):
		try:
			self.db[str(key)] = value
			self.dumpdb()
			return True
		except Exception as e:
			print("[X] Error Saving Values to Database : " + str(e))
			return False   

	def get(self, key):
		try:
			return self.db[key]
		except KeyError:
			print("No Value Can Be Found for " + str(key))  
			return False   

	def delete(self , key):
		if not key in self.db:
			return False
		del self.db[key]
		self.dumpdb()
		return True

	def resetdb(self):
		self.db={}
		self.dumpdb()
		return True

	def top10(self):
		print(type(self.db))
		print(self.db)
		num = 0
		players = []
		for x in self.db:
			players.append([x,self.db[x]["Games"],self.db[x]["Total Scores"]])
		players.sort(key = lambda x: x[2], reverse = True)
		
		if len(players) > 10:
			players = players[0:10]
		print(*players)	
		return players
# mydb = FoobarDB("./mydb.db")

# mydb.load("./mydb.db")

# playerInfo = {
# 	"Games": 12,
# 	"Total Scores": 1000
# }

# mydb.set("Senya" , playerInfo) #Sets Name  (Games, TotalScores)


# playerInfo = {
# 	"Games": 1,
# 	"Total Scores": 100
# }

# mydb.set("Dima" , playerInfo) #Sets Name  (Games, TotalScores)