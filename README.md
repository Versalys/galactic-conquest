# galactic-conquest

Welcome to galactic conquest, a 1v1 game of strategy to see who will rule deep space!

This is a game that I have wanted to make for a while, with inspiration from Sid Meier's 
Civilization and Star Wars.

In each game, there are two motherships on opposing sides for each player, and it is the goal
of each player to destroy the other mothership. To aid in conquest, the player may build
spacecraft using limited resources, nanites. Around the map, asteroids litter the plane
with some carrying the material which can be mined. Players then try to use miner spacecraft
to establish mining colonies and use military spacecraft to defend them.

The game is focused heavily on resource aquisition and preventing your opponent from doing
the same, so control of as many mining colonies is key as they can be destroyed by the other
player.

This game is a work in progress, and is being built in python. The reasoning for this is that
I'd rather focus on making a cool game over technical aspects that I am not as familiar with.
This game makes heavy use of the pygame library, found here https://www.pygame.org/news.

This game will eventually support...

- multiplayer
- balanced map generation
- 8 types of unique spacecraft with varied abilities
- a graphical shop system for buying spacecraft
- pretty game sprites

Right now, this game is meant to be peer 2 peer and hotseat 
as I don't have any way to have free, consistent infrastructure, 
but if this turns into a more serious thing I will adopt a client 
server model for security purposes.
