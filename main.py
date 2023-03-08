import objects as obj
import os
import functions as fn
import animations
import time

weapons = {
    "wooden_sword": obj.Weapon(name="Wooden Sword", description="A wooden sword, rather rustic.", damage=5, value=1, weight=5),
    "iron_sword": obj.Weapon(name="Iron Sword", description="A sword made of iron. Strong and reliable.", damage=10, value=10, weight=10),
    "steel_sword": obj.Weapon(name="Steel Sword", description="A sword made of steel, it's quite heavy but packs a punch.", damage=15, value=20, weight=15),
    "bow": obj.Weapon(name="Bow", description="A bow made of wood, it's quite light but packs a punch.", damage=10, value=10, weight=5),
    "axe": obj.Weapon(name="Axe", description="A axe made of steel, it's quite heavy but packs a punch.", damage=15, value=20, weight=15),
}

armors = {
    "wooden_armor": obj.Armor(name="Wooden Armor", description="A wooden armor, rather rustic.", armor=5, value=1, weight=5),
    "iron_armor": obj.Armor(name="Iron Armor", description="An armor made of iron. Strong and reliable.", armor=10, value=10, weight=10),
    "steel_armor": obj.Armor(name="Steel Armor", description="An armor made of steel, it's quite heavy but packs a punch.", armor=15, value=20, weight=15),
}

items = {
    "potion": obj.Item(name="Potion", description="A potion that heals you.", value=5, weight=1),
    "apple": obj.Item(name="Apple", description="An apple that heals you.", value=2, weight=1),
    "gold": obj.Item(name="Gold", description="Gold, it's shiny.", value=1, weight=1),
    "garbage": obj.Item(name="Garbage", description="Garbage, it's smelly.", value=1, weight=1),
}

enemies = {
    "goblin": obj.Entity(name="Goblin", description="A goblin, it's green and ugly.", health=30, damage=10, armor=2),
    "fairy": obj.Entity(name="Fairy", description="A fairy, it's small and cute. It loves collecting teeth... weird.", health=5, damage=2, armor=1),
    "dragon": obj.Entity(name="Dragon", description="A dragon, it's big and scary. It breathes fire.", health=100, damage=10, armor=5),
    "skeleton": obj.Entity(name="Skeleton", description="A skeleton, it's a very rattly.", health=20, damage=5, armor=1),
    "zombie": obj.Entity(name="Zombie", description="A zombie, it's a very smelly.", health=20, damage=5, armor=1),
}

narrator = obj.Entity(name="Narrator", description="The narrator of the story", health=999999, damage=0, armor=9999999, color="green")
player = obj.Player(name="Player", description="You, the player")

print("""
████████╗██╗░░██╗███████╗  ░██████╗░░█████╗░███╗░░░███╗███████╗
╚══██╔══╝██║░░██║██╔════╝  ██╔════╝░██╔══██╗████╗░████║██╔════╝
░░░██║░░░███████║█████╗░░  ██║░░██╗░███████║██╔████╔██║█████╗░░
░░░██║░░░██╔══██║██╔══╝░░  ██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░
░░░██║░░░██║░░██║███████╗  ╚██████╔╝██║░░██║██║░╚═╝░██║███████╗
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝""")

fn.say(narrator.__useable_dict__(), """Welcome to the game, this is a text based game where you can explore the world and fight monsters.
Would you like to see the lore? (y/n)""", 250)

if input("> ").lower() == "y":
    fn.say(narrator.__useable_dict__(), """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Enim praesent elementum facilisis leo. Posuere ac ut consequat semper viverra nam libero justo laoreet. Purus ut faucibus pulvinar elementum integer enim. Sapien et ligula ullamcorper malesuada proin libero. Volutpat lacus laoreet non curabitur gravida. Penatibus et magnis dis parturient. Diam volutpat commodo sed egestas egestas fringilla phasellus faucibus scelerisque. Interdum consectetur libero id faucibus nisl tincidunt eget nullam non. Risus in hendrerit gravida rutrum quisque. Nibh tellus molestie nunc non blandit massa enim. Pretium fusce id velit ut tortor pretium viverra suspendisse potenti. In iaculis nunc sed augue lacus viverra vitae congue eu. Est ante in nibh mauris cursus. Leo a diam sollicitudin tempor id. Nibh venenatis cras sed felis eget velit aliquet sagittis. Urna cursus eget nunc scelerisque viverra mauris in aliquam sem. Aliquam sem et tortor consequat id porta nibh venenatis. Cursus in hac habitasse platea dictumst.
""", 300) # TODO: Add real lore

fn.say(narrator.__useable_dict__(), "What is your name?")
player.name = input("> ")

fn.say(narrator.__useable_dict__(), f"Hello {player.name}! Let's start the game!")
fn.wait(1)
fn.clear()
fn.wait(0.9)
fn.human_say("* You wake up on a dirt road, you don't know why or how you got here, all you know is you have 3 paths ahead of you. *")
fn.human_say("Which path do you take? (left, middle, right)")
path = input("> ").lower()

if path not in ["left", "middle", "right"]:
    fn.say(narrator.__useable_dict__(), "You can't go that way!")
    fn.wait(1)
    fn.clear()
    fn.wait(0.9)
    fn.human_say("* You wake up on a dirt road, you don't know why or how you got here, all you know is you have 3 paths ahead of you. *")
    path = input("Which path do you take? (left, middle, right) > ").lower()

if path == "left":
    pass
elif path == "middle":
    pass
elif path == "right":
    pass



fn.end()
