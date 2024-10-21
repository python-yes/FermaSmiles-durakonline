import time
import random
import threading
from durakonline import durakonline
from datetime import datetime

Token_List = ["токен1",
"токен2",
"токен3",
"токен4",
"токен5",
"токен6",
"токен7",
"токен8",
"токен9",
"токен10"]

shuffled_tokens = random.sample(Token_List, len(Token_List))

BOT1_TOKEN = shuffled_tokens[0]
BOT2_TOKEN = shuffled_tokens[1]
BOT3_TOKEN = shuffled_tokens[2]
BOT4_TOKEN = shuffled_tokens[3]
BOT5_TOKEN = shuffled_tokens[4]
BOT6_TOKEN = shuffled_tokens[5]
BOT7_TOKEN = shuffled_tokens[6]
BOT8_TOKEN = shuffled_tokens[7]
BOT9_TOKEN = shuffled_tokens[8]
BOT10_TOKEN = shuffled_tokens[9]

DEBUG_MODE: bool = False

class ClassA:
    def __init__(self):
        print("class A initialized")

    games: int = 0
    accounts: [] = []
    SERVERS: [] = [
    "u1"
]

    def __init__(self):
        self.pages = [
            self.acc,
            self.acc,
        ]
        print("START")

    def start_game(self, main, bot, server_id: str, count: int = 1000):
        self.games += 1
        self.log("Create 1 thread", f"{server_id}")
        game = bot.game.create(100, "1", 2, 52)
        main.game.join("1", game.id)
        main._get_data("game")
        for i in range(count):
            self.log(f"{i+1} game", f"{server_id}")
            main.game.ready()
            bot.game.ready()

            for i in range(4):
                try:
                    main_cards = main._get_data("hand")["cards"]

                except:
                    pass
                try:
                    bot_cards = bot._get_data("hand")["cards"]

                except:
                    pass
                mode = bot._get_data("mode")
                if mode["0"] == 1:
                    bot.game.turn(bot_cards[0])
                    time.sleep(.1)
                    main.game.take()
                    time.sleep(.1)
                    bot.game._pass()
                else:
                    main.game.turn(main_cards[0])
                    time.sleep(.1)
                    bot.game.take()
                    time.sleep(.1)
                    main.game._pass()
            bot.game.surrender()
            bot._get_data("game_over")
        main.game.leave(game.id)
        self.log("Leave", "MAIN")
        bot.game.leave(game.id)
        self.log("Leave", "BOT")
        self.games -= 1
        if not self.games:
            data = main._get_data("uu")
            while data["k"] != "points":
                data = main._get_data("uu")
            user = main.get_user_info(main.uid)
            self.log(f"ник: {user.name}",f" Bal: {data.get('v')}")
            data = bot._get_data("uu")
            while data["k"] != "points":
                data = bot._get_data("uu")
            user = bot.get_user_info(bot.uid)
            self.log(f"ник: {user.name}",f" Bal: {data.get('v')}")

    def start(self):
        page_type = 1
        self.pages[page_type-1]("$u")

    def acc(self, token: str):
        for server_id in self.SERVERS:
            main = durakonline.Client(shuffled_tokens[0], server_id=server_id, tag="[MAIN]", debug=DEBUG_MODE)
            bot = durakonline.Client(shuffled_tokens[1], server_id=server_id, tag="[BOT]", debug=DEBUG_MODE)
            threading.Thread(target=self.start_game, args=(main, bot, server_id, 1 )).start()

    def log(self, message: str, tag: str = "MAIN") -> None:
        print(f">> [{tag}] [{datetime.now().strftime('%H:%M:%S')}] {message}")

class ClassB(ClassA):
    SERVERS: [] = [
    "u2"
]
    def start(self):
        page_type = 1
        self.pages[page_type-1]("$u")

    def acc(self, token: str):
        for server_id in self.SERVERS:
            main = durakonline.Client(shuffled_tokens[1], server_id=server_id, tag="[MAIN]", debug=DEBUG_MODE)
            bot = durakonline.Client(shuffled_tokens[2], server_id=server_id, tag="[BOT]", debug=DEBUG_MODE)
            threading.Thread(target=self.start_game, args=(main, bot, server_id, 1)).start()

class ClassC(ClassA):
    SERVERS: [] = [
    "u3"
]
    def start(self):
        page_type = 1
        self.pages[page_type-1]("$u")

    def acc(self, token: str):
        for server_id in self.SERVERS:
            main = durakonline.Client(shuffled_tokens[2], server_id=server_id, tag="[MAIN]", debug=DEBUG_MODE)
            bot = durakonline.Client(shuffled_tokens[3], server_id=server_id, tag="[BOT]", debug=DEBUG_MODE)
            threading.Thread(target=self.start_game, args=(main, bot, server_id, 1)).start()

class ClassD(ClassA):
    SERVERS: [] = [
    "u4"
]
    def start(self):
        page_type = 1
        self.pages[page_type-1]("$u")

    def acc(self, token: str):
        for server_id in self.SERVERS:
            main = durakonline.Client(shuffled_tokens[3], server_id=server_id, tag="[MAIN]", debug=DEBUG_MODE)
            bot = durakonline.Client(shuffled_tokens[4], server_id=server_id, tag="[BOT]", debug=DEBUG_MODE)
            threading.Thread(target=self.start_game, args=(main, bot, server_id, 1)).start()

class ClassE(ClassA):
    SERVERS: [] = [
    "u5"
]
    def start(self):
        page_type = 1
        self.pages[page_type-1]("$u")

    def acc(self, token: str):
        for server_id in self.SERVERS:
            main = durakonline.Client(shuffled_tokens[4], server_id=server_id, tag="[MAIN]", debug=DEBUG_MODE)
            bot = durakonline.Client(shuffled_tokens[5], server_id=server_id, tag="[BOT]", debug=DEBUG_MODE)
            threading.Thread(target=self.start_game, args=(main, bot, server_id, 1)).start()

class ClassF(ClassA):
    SERVERS: [] = [
    "u6"
]
    def start(self):
        page_type = 1
        self.pages[page_type-1]("$u")

    def acc(self, token: str):
        for server_id in self.SERVERS:
            main = durakonline.Client(shuffled_tokens[5], server_id=server_id, tag="[MAIN]", debug=DEBUG_MODE)
            bot = durakonline.Client(shuffled_tokens[6], server_id=server_id, tag="[BOT]", debug=DEBUG_MODE)
            threading.Thread(target=self.start_game, args=(main, bot, server_id, 1)).start()

class ClassG(ClassA):
    SERVERS: [] = [
    "u7"
]
    def start(self):
        page_type = 1
        self.pages[page_type-1]("$u")

    def acc(self, token: str):
        for server_id in self.SERVERS:
            main = durakonline.Client(shuffled_tokens[6], server_id=server_id, tag="[MAIN]", debug=DEBUG_MODE)
            bot = durakonline.Client(shuffled_tokens[7], server_id=server_id, tag="[BOT]", debug=DEBUG_MODE)
            threading.Thread(target=self.start_game, args=(main, bot, server_id, 1)).start()

class ClassH(ClassA):
    SERVERS: [] = [
    "u8"
]
    def start(self):
        page_type = 1
        self.pages[page_type-1]("$u")

    def acc(self, token: str):
        for server_id in self.SERVERS:
            main = durakonline.Client(shuffled_tokens[7], server_id=server_id, tag="[MAIN]", debug=DEBUG_MODE)
            bot = durakonline.Client(shuffled_tokens[8], server_id=server_id, tag="[BOT]", debug=DEBUG_MODE)
            threading.Thread(target=self.start_game, args=(main, bot, server_id, 1)).start()

class ClassK(ClassA):
    SERVERS: [] = [
    "u9"
]
    def start(self):
        page_type = 1
        self.pages[page_type-1]("$u")

    def acc(self, token: str):
        for server_id in self.SERVERS:
            main = durakonline.Client(shuffled_tokens[8], server_id=server_id, tag="[MAIN]", debug=DEBUG_MODE)
            bot = durakonline.Client(shuffled_tokens[9], server_id=server_id, tag="[BOT]", debug=DEBUG_MODE)
            threading.Thread(target=self.start_game, args=(main, bot, server_id, 1)).start()

class ClassM(ClassA):
    SERVERS: [] = [
    "uA"
]
    def start(self):
        page_type = 1
        self.pages[page_type-1]("$u")

    def acc(self, token: str):
        for server_id in self.SERVERS:
            main = durakonline.Client(shuffled_tokens[9], server_id=server_id, tag="[MAIN]", debug=DEBUG_MODE)
            bot = durakonline.Client(shuffled_tokens[0], server_id=server_id, tag="[BOT]", debug=DEBUG_MODE)
            threading.Thread(target=self.start_game, args=(main, bot, server_id, 1)).start()

# Instantiate the classes
classA = ClassA()
classB = ClassB()
classC = ClassC()
classD = ClassD()
classE = ClassE()
classF = ClassF()
classG = ClassG()
classH = ClassH()
classK = ClassK()
classM = ClassM()

for i in range(100000):
    shuffled_tokens = random.sample(Token_List, len(Token_List))
    BOT1_TOKEN = shuffled_tokens[0]
    BOT2_TOKEN = shuffled_tokens[1]
    BOT3_TOKEN = shuffled_tokens[2]
    BOT4_TOKEN = shuffled_tokens[3]
    BOT5_TOKEN = shuffled_tokens[4]
    BOT6_TOKEN = shuffled_tokens[5]
    BOT7_TOKEN = shuffled_tokens[6]
    BOT8_TOKEN = shuffled_tokens[7]
    BOT9_TOKEN = shuffled_tokens[8]
    BOT10_TOKEN = shuffled_tokens[9]
    print("Cycle:", i+1)
    classA.start()
    time.sleep(15)
    classB.start()
    time.sleep(15)
    classC.start()
    time.sleep(15)
    classD.start()
    time.sleep(15)
    classE.start()
    time.sleep(15)
    classF.start()
    time.sleep(15)
    classG.start()
    time.sleep(15)
    classH.start()
    time.sleep(15)
    classK.start()
    time.sleep(15)
    classM.start()
    time.sleep(15)