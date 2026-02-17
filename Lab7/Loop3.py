# designing an adventure game where the character has a health bar 
# Loop example 3

health = 100

while health > 0:
    print(f"Current health: {health}")
    damage = int(input("Enter damage taken: "))
    health -= damage

print("Game Over!")