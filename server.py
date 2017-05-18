import PodSixNet.Channel
import PodSixNet.Server
from time import sleep

class ClientChannel(PodSixNet.Channel.Channel):
    def Network(self, data):
        print data

    def Network_move(self, data):
        self.gameid = data["gameid"]

        self._server.do_stuff(data)

    def Network_put_wall(self, data):
        self.gameid = data["gameid"]
        self._server.do_stuff(data)

class QuoridorServer(PodSixNet.Server.Server):

    channelClass = ClientChannel

    def __init__(self, *args, **kwargs):
        PodSixNet.Server.Server.__init__(self, *args, **kwargs)
        self.games = []
        self.queue = None
        self.currentIndex = 0

    def Connected(self, channel, addr):
        print 'new connection:', channel
        if self.queue == None:
            self.currentIndex+=1
            channel.gameid=self.currentIndex
            self.queue=Game(channel, self.currentIndex)
        else:
            channel.gameid=self.currentIndex
            self.queue.player1=channel
            self.queue.player0.Send({"action":"startgame","player":0, "gameid": self.queue.gameid})
            self.queue.player1.Send({"action":"startgame","player":1, "gameid": self.queue.gameid})
            self.games.append(self.queue)
            self.queue=None

    def do_stuff(self, data):
        game = [a for a in self.games if a.gameid == data["gameid"]]
        if len(game)==1:
            game[0].do_stuff(data)

class Game:
    def __init__(self, player0, currentIndex):
        # whose turn it is
        self.turn = 0

        self.player0=player0
        self.player1=None

        self.gameid=currentIndex

    def do_stuff(self, data):
        if data["num"]==0:
            self.player1.Send(data)
        else:
            self.player0.Send(data)

        
print "STARTING SERVER ON LOCALHOST"
quoridorServe = QuoridorServer()
while True:
    quoridorServe.Pump()
    sleep(0.01)
