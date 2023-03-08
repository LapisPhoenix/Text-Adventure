class Item:
    def __init__(self, name: str, description: str, weight: float, value: int) -> None:
        self.name = name
        self.description = description
        self.weight = weight
        self.value = value

    def __repr__(self) -> str:
        return f"Item({self.name}, {self.description}, {self.weight}, {self.value})"

    def __str__(self) -> str:
        return f"{self.name}: {self.description}\nWeight: {self.weight}\nValue: {self.value}"
    
    def getName(self) -> str:
        return self.name
    
    def getDescription(self) -> str:
        return self.description
    
    def getWeight(self) -> float:
        return self.weight
    
    def getValue(self) -> int:
        return self.value
    
    def setName(self, name: str) -> str:
        self.name = name

        return f"Name set to {name}"
    
    def setDescription(self, description: str) -> str:
        self.description = description

        return f"Description set to {description}"
    
    def setWeight(self, weight: float) -> str:
        self.weight = weight

        return f"Weight set to {weight}"
    
    def setValue(self, value: int) -> str:
        self.value = value

        return f"Value set to {value}"


class Weapon(Item):
    def __init__(self, name: str, description: str, weight: float, value: int, damage: int) -> None:
        super().__init__(name, description, weight, value)
        self.damage = damage

    def __repr__(self) -> str:
        return f"Weapon({self.name}, {self.description}, {self.weight}, {self.value}, {self.damage})"

    def __str__(self) -> str:
        return f"{self.name}: {self.description}\nWeight: {self.weight}\nValue: {self.value}\nDamage: {self.damage}"
    
    def getDamage(self) -> int:
        return self.damage
    
    def setDamage(self, damage: int) -> str:
        self.damage = damage

        return f"Damage set to {damage}"


class Armor(Item):
    def __init__(self, name: str, description: str, weight: float, value: int, armor: int) -> None:
        super().__init__(name, description, weight, value)
        self.armor = armor

    def __repr__(self) -> str:
        return f"Armor({self.name}, {self.description}, {self.weight}, {self.value}, {self.armor})"

    def __str__(self) -> str:
        return f"{self.name}: {self.description}\nWeight: {self.weight}\nValue: {self.value}\nArmor: {self.armor}"
    
    def getArmor(self) -> int:
        return self.armor
    
    def setArmor(self, armor: int) -> str:
        self.armor = armor

        return f"Armor set to {armor}"


class Entity:
    def __init__(self, name: str, description: str, health: int, damage: int, armor: int, color: str = "white") -> None:
        self.name = name
        self.description = description
        self.health = health
        self.damage = damage
        self.armor = armor
        self.color = color

    def __useable_dict__(self) -> dict:
        return {key : value for key, value in self.__dict__.items()}

    def __repr__(self) -> str:
        return f"Entity({self.name}, {self.description}, {self.health}, {self.damage}, {self.armor})"

    def __str__(self) -> str:
        return f"{self.name}: {self.description}\nHealth: {self.health}\nDamage: {self.damage}\nArmor: {self.armor}"
    
    def attack(self, target) -> str:
        if not isinstance(target, Entity):
            raise ValueError("Target must be an Entity")
        
        target.health -= (self.damage - target.armor)

        if target.health <= 0:
            return f"{self.name} killed {target.name}!"
        else:
            return f"{self.name} attacked {target.name} for {self.damage - target.armor} damage!"

    def heal(self, amount: int) -> str:
        self.health += amount

        return f"{self.name} healed for {amount} health!"
    
    def hurt(self, amount: int) -> str:
        self.health -= amount - self.armor

        return f"{self.name} took {amount} damage!"
    
    def getHealth(self) -> int:
        return self.health
    
    def getDamage(self) -> int:
        return self.damage
    
    def getArmor(self) -> int:
        return self.armor
    
    def setHealth(self, amount: int) -> str:
        self.health = amount

        return "Health set"
    
    def setDamage(self, amount: int) -> str:
        self.damage = amount

        return "Damage set"
    
    def setArmor(self, amount: int) -> str:
        self.armor = amount

        return "Armor set"
    
    def getName(self) -> str:
        return self.name
    
    def getDescription(self) -> str:
        return self.description
    
    def setName(self, name: str) -> str:
        self.name = name

        return "Name set"
    
    def setDescription(self, description: str) -> str:
        self.description = description

        return "Description set"


class Player(Entity):
    def __init__(self, name: str = "You", description: str = "The Player.", health: int = 100, damage: int = 1,
                 armor: int = 0, inventory: list = [], max_inventory: int = 10, gold: int = 0, max_weight: int = 50, color: str = "red") -> None:
        super().__init__(name, description, health, damage, armor, color)
        self.inventory = inventory
        self.max_inventory = max_inventory
        self.gold = gold
        self.max_weight = max_weight

    def __repr__(self) -> str:
        return f"Player({self.name}, {self.description}, {self.health}, {self.damage}, {self.armor}, {self.inventory}, {self.max_inventory}, {self.gold})"
    
    def __str__(self) -> str:
        return f"{self.name}: {self.description}\nHealth: {self.health}\nDamage: {self.damage}\nArmor: {self.armor}\nInventory: {self.inventory}\nGold: {self.gold}"
    
    def addItem(self, item: Item) -> str:
        if len(self.inventory) >= self.max_inventory:
            return "Inventory is full"
        
        self.inventory.append(item)

        return "Item added"
        
    def removeItem(self, item: Item) -> str:
        if item not in self.inventory:
            return "Item not in inventory"
        
        self.inventory.remove(item)

        return "Item removed"
    
    def getInventory(self) -> list:
        return self.inventory
    
    def getGold(self) -> int:
        return self.gold
    
    def addGold(self, amount: int) -> str:
        self.gold += amount

        return "Gold added"
    
    def removeGold(self, amount: int) -> str:
        self.gold -= amount

        return "Gold removed"


class Trader(Entity):
    def __init__(self, name: str, description: str, health: int = 100, damage: int = 0, armor: int = 0, trades: dict = {}) -> None:
        super().__init__(name, description, health, damage, armor)
        self.trades = trades

    def __repr__(self) -> str:
        return f"Trader({self.name}, {self.description}, {self.health}, {self.damage}, {self.armor}, {self.trades})"
    
    def __str__(self) -> str:
        return f"{self.name}: {self.description}\nHealth: {self.health}\nDamage: {self.damage}\nArmor: {self.armor}\nTrades: {self.trades}"
        
    def getTrades(self) -> dict:
        return self.trades
    
    def addTrade(self, item: Item, price: int) -> str:
        self.trades += {item.name: {"price": price, "description": item.description, "bought": False}}

        return "Trade added"
    
    def removeTrade(self, item: Item) -> str:
        if item.name not in self.trades.keys():
            return "Item not in trades"

        del self.trades[item]
        return "Trade removed"
    
    def buyItem(self, item: Item, player: Player) -> str:
        if item.name not in self.trades.keys():
            return "Item not in trades"
        
        if self.trades[item.name]["bought"]:
            return "Item already bought"
        
        if player.getGold() < self.trades[item.name]["price"]:
            return "Not enough gold"
        
        player.removeGold(self.trades[item.name]["price"])
        player.addItem(item)
        self.trades[item.name]["bought"] = True

        return f"{item.name} bought"
    
    def sellItem(self, item: Item, player: Player) -> str:
        if item.name not in self.trades.keys():
            return "Item not in inventory"
        
        player.removeItem(item)
        player.addGold(item.value)
        self.addTrade(item, item.value)


        return f"{item.name} sold for {item.value} gold"
    
    def getTradesByName(self, name: str) -> str:
        if name not in self.trades.keys():
            return "Item not in trades"
        
        return self.trades[name].__str__()
    
    def getTradePrice(self, item: Item) -> int:
        if item.name not in self.trades.keys():
            return "Item not in trades"
        
        return self.trades[item.name]["price"]
    
    def getTradeDescription(self, item: Item) -> str:
        if item.name not in self.trades.keys():
            return "Item not in trades"
        
        return self.trades[item.name]["description"]
    
    def getTradeBought(self, item: Item) -> bool:
        if item.name not in self.trades.keys():
            return "Item not in trades"
        
        return self.trades[item.name]["bought"]
    
    def setTradePrice(self, item: Item, price: int) -> str:
        if item.name not in self.trades.keys():
            return "Item not in trades"
        
        self.trades[item.name]["price"] = price

        return "Price set"
    
    def setTradeDescription(self, item: Item, description: str) -> str:
        if item.name not in self.trades.keys():
            return "Item not in trades"
        
        self.trades[item.name]["description"] = description

        return "Description set"
    
    def setTradeBought(self, item: Item, bought: bool) -> str:
        if item.name not in self.trades.keys():
            return "Item not in trades"
        
        self.trades[item.name]["bought"] = bought

        return "Bought set"
    
    def resetTrades(self) -> str:
        for item in self.trades.keys():
            self.trades[item]["bought"] = False

        return "Trades reset"
    
    def resetTrade(self, item: Item) -> str:
        if item.name not in self.trades.keys():
            return "Item not in trades"
        
        self.trades[item.name]["bought"] = False

        return "Trade reset"
    
    def resetTradePrice(self, item: Item) -> str:
        if item.name not in self.trades.keys():
            return "Item not in trades"
        
        self.trades[item.name]["price"] = item.value

        return "Price reset"
    
    def resetTradeDescription(self, item: Item) -> str:
        if item.name not in self.trades.keys():
            return "Item not in trades"
        
        self.trades[item.name]["description"] = item.description

        return "Description reset"
    
    def resetTradeBought(self, item: Item) -> str:
        if item.name not in self.trades.keys():
            return "Item not in trades"
        
        self.trades[item.name]["bought"] = False

        return "Bought reset"
    
    def resetTradeAll(self, item: Item) -> str:
        if item.name not in self.trades.keys():
            return "Item not in trades"
        
        self.trades[item.name]["price"] = item.value
        self.trades[item.name]["description"] = item.description
        self.trades[item.name]["bought"] = False

        return "Trade reset"