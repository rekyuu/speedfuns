# Pokémon Emerald (Any%, Glitchless)

## Records
[speedrun.com](http://www.speedrun.com/pkmnemerald#Any%25_Glitchless)

## Route Rules
- Timing is by the in-game timer, as it shows on the back of the trainer card after reloading the file.
- Runs must be single segment (no save+quit), as otherwise the in-game timer is not accurate.
- Runs must be done on English version.
- Using glitches is not allowed.

## These Notes
Copied from the guide [here](http://wiki.pokemonspeedruns.com/index.php/Pok%C3%A9mon_Emerald_Mudkip/Rayquaza_Route) and personally modified.

-----

## Links and Information
[Battle Information Spreadsheet](https://docs.google.com/spreadsheets/d/1YBll3FbJfaIMJ2CtV72kXfYTlF0qRDxuWHHKhUJ76Uo/edit?usp=sharing)

### Spinner Manipulation (Run/Walk Method)
Run from below to the square diagonally below-and-right of the trainer, then walk to the next square directly to the right of the trainer. From here you can run or walk, they can't catch you. Be careful when doing this however, as running a single tile higher will guarantee that the trainer catches you.

Any spinner that you have to pass by the left or right of (so you start below them, and then finish above) can be manipulated in this manner, to guarantee not getting caught. However it does not work on spinners that you need to pass above or below, as running into the squares immediately diagonal to a spinner will make them look either up or down, up for the top-left and top-right squares, down for bottom-left and bottom-right.

### Maps
#### Petalburg Woods
![](http://i.imgur.com/zULmMFn.png)

#### Granite Gave
![](http://i.imgur.com/X0xk3Je.png)

#### Slateport Beach
![](http://i.imgur.com/1SL3NvC.png)

#### Wattson Gym
![](http://i.imgur.com/0XGGNqq.png)

#### Mauville to Meteor Falls
![](http://i.imgur.com/DiA34DH.png)

#### Flannery Gym
![](http://i.imgur.com/XdBGS0F.png)

#### Brawly Gym
![](http://i.imgur.com/J3XEb4D.png)

#### Winona Gym
![](http://i.imgur.com/7t0tLyn.png)

#### Aqua Hideout
![](http://i.imgur.com/8YneFqd.png)

#### Juan Gym
![](http://i.imgur.com/2L0pFac.png)

#### Victory Road
![](http://i.imgur.com/V3UbO03.png)

### VBA-M
The message "The internal battery has died. The game can be played. However clock based events will no longer occur." may appear when you load the game. It is actually advantageous to have this message, as it eliminates random phone calls from registered trainers. Old carts will likely have this warning, and the emulator vba naturally has this warning. However, vba-m does not. To get the internal battery warning with vba-m, go to the folder you have vba-m saved in, and open the vba-over file in notepad. Find the line that reads "# Pokemon - Emerald Version (USA, Europe)", and in the lines below, edit "rtcEnabled=1" to "rtcEnabled=0".

## Notation
- Whenever the route refers to Mudkip's stats, it will be in the form `xx/xx/xx`, where the "`x`"s represent numbers. In order, these refer to the stats `Attack`, `Special Attack` and `Speed`.
- If the route says to avoid a trainer, and the trainer's name is **bold**, that trainer is a spinner. "Timed" spinners/Rotatos (i.e. trainers that spin in a predictable fashion, non-randomly) will not be in bold.
- If "@[Item Name]" follows after a pokemon, it means it is holding an item that you should be aware of. Not all of the items that each pokemon are holding are written here, just the ones that are significant to the route.
- Unless stated otherwise (normally by "use this move until it faints"), battles are detailed turn by turn.

-----

## New Game
Before starting a new game, set your options as:

  - Text Speed - Fast
  - Battle Scene - Off
  - Battle Style - Set

Other options can be set as you please.

Start a new game, and choose Girl (the Brendan 2 fight is much safer as the girl), and name your character a single character name.

## Littleroot Town
Leave the clock at default.

Collect the Potion from your PC.

Once the conversations with Mom are done, head towards Brendan's house. Enter, talk to Brendan's mom, and head upstairs. As soon as you enter the room, leave again and go to walk out the house. Brendan will appear and talk to you.

Head out and north to Route 101 to meet Prof. Birch.

## Route 101
Choose Mudkip after looking in the bag, and then the Zigzagoon fight will begin.

In the battle, check Mudkip's nature and stats. The minimum stats that are runnable are `13/10/9`.

> It is recommended to only accept `13/11/9`, however `10 Sp.Atk` can be run with, but with some time loss (mostly to the 3 double battles in the Magma and Aqua hideouts). `14/10/9+` is also acceptable, as the time gained from `14 Attack` negates the time lost from `10 Sp.Attack`.

Note: Defenses and Hp don't matter in terms of resetting, however higher is better. The best possible Mudkip for a run is Naughty natured, 14/11/10. The possible stat values at Lvl.5 are:

Stat | HP | Attack | Defense | Sp.Atk | Sp.Def | Speed
:----|:--:|:------:|:-------:|:------:|:------:|:----:
Min (-nature) | -- | 10 |  9 |  9 |  9 |  8
Min           | 20 | 12 | 10 | **10** | 10 |  **9**
Max           | 21 | **13** | 11 | **11** | 11 | **10**
Max (+nature) | -- | **14** | 12 | **12** | 12 | **11**

> Note: -nature and +nature mean a decreasing and increasing nature in that stat, respectively.

### Wild Encounter
Pokemon | Actions
:--|:--
Zigzagoon | Tackle until it faints.

## Littleroot Town
In the conversation with Prof. Birch, nickname your Mudkip a one character name.

Say "Yes" to seeing Brendan, and exit the lab.

From here, head north, through Route 101 and Oldale Town into Route 103. Run from any encounters.

## Route 103
Speak to Brendan to start the first Rival fight.

### Rival Brendan
Pokemon | Actions
:--|:--
Treecko | Tackle until it faints.

Beating Treecko will level Mudkip to lvl.6.

  - Check its Attack here, if it goes to `15` continue on, if not reset.
  - Take note of Mudkip's health at the end of the fight, you will need to Potion before the next battle if your health is below `7 HP`, below `9 HP` with bad defense, below `10 HP` with `14 Atk`, or below `13 HP` with `14 Atk` and bad defense.

After the Brendan fight return south to Prof. Birch's lab.

## Littleroot Town
After receiving the Pokedex and Pokeballs, exit the lab and talk to Mom (who is standing outside the house). Don't walk past her, as she will then walk to you, which wastes time. From here on run wherever you can.

From here, head north to Oldale Town, then west at Oldale to Route 102, again running from any encounters.

> Note: If you encounter a Poochyena or Zigzagoon before Petalburg City, you can catch it as a Rock Smash slave, however this is slower than catching a Poochyena in Route 116, as you have to deposit it at Petalburg City to avoid a double battle. Poochyena's encounter rate in Route 116 is 28%, so this is down to personal preference whether you catch one here or not.

## Route 102
Head west and battle the first Youngster.

### Youngster Calvin
Pokemon | Actions
:--|:--
Poochyena | Tackle until it faints.

Avoid all the other trainers by running through the grass, running from encounters when necessary.

Grab the Oran berries to the right of the second youngster.

## Petalburg City
Enter the PokeCentre to set a Teleport point for later.

  - Deposit Poochyena/Zigzagoon if you caught one along the way.
  - Go into "Move pokemon", and move Mudkip into the box first, then take him back out and put Poochyena/Zigzagoon in. This fully heals Mudkip.

Next, head to the Mart.

### Petalburg Mart
Purchase | #
:--|:--
Potion | 1
Repel | 4
X Speed | 1
X Attack | 2

After the Mart, head to the gym and go through the Wally catching tutorial.

Next, head west towards Route 104. Scott will stop you and talk to you, afterwards head into Route 104.

## Route 104
From entering, head south on to the beach, then west, then north, picking up the hidden Potion on the top-left tile of the beach.

![](https://raw.githubusercontent.com/rekyuu/speedfuns/master/pokemon/gen3/img/rse/route-104_potion.png)

Pick up the Oran berries above and head towards the second patch of grass.

  - Potion Mudkip if he is `12 HP` or less.
  - Repel.
  - Give Mudkip an Oran Berry.

Run through the grass, behind the trainer, and enter Petalburg Woods.

## Petalburg Woods
![](http://i.imgur.com/zULmMFn.png)

Avoid the spinner.

Talk to the Devon Researcher, and battle the Aqua Grunt.

### Team Aqua Grunt
Pokemon | Actions
:--|:--
Poochyena | Tackle until it faints.

Pick up the Ether above the next spinner and head out of Petalburg Woods to the other side of Route 104.

## Route 104
At the exit of Petalburg Woods, collect the Oran berries to the west if the Aqua Grunt's Poochyena did a lot of damage.

Head east and then north across the bridge, towards Rustboro City, avoiding the remaining trainers.
  - The double battle on the bridge wont activate with only one Pokemon in your party.

## Rustboro City
Head north, and straight into Rustboro Gym.

If necessary, heal Mudkip and attach an Oran berry before fighting Youngster Josh (the southern-most youngster).

### Youngster Josh
Pokemon | Actions
:--|:--
Geodude | Mud Slap until it faints.

Mudkip will level up to lvl.10, and learn Water Gun.

Take note of Mudkip's speed. If it is 13 at lvl.10 you will need to buy an extra X Speed at the Fallarbor Shopping Trip.

Next, fight the other Youngster.

### Youngster Tommy
Pokemon | Actions
:--|:--
Geodude | Water Gun
Geodude | Water Gun

Heal to full health and attach an Oran berry, then speak to Roxanne to start the first Gym Leader battle.

### Leader Roxanne
Pokemon | Holding | Actions
:--|:--|:--
Geodude | | Water Gun
Geodude | | Water Gun
Nosepass | Oran Berry | Water Gun

> If your speed is above 18 here, Nosepass will Rock Tomb initially, to lower your speed.

> If you are at a HP level that a Rock Tomb will kill (around `20 HP`) it will also use Rock Tomb, so potion at these HP levels.

-----