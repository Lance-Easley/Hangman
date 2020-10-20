def graphic(stage: int) -> str:
    """Prints the graphic for whichever stage the player is at.
    """
    if stage == 1:
        print("""
 
 
 
 
 
_ _ _ _ _
        """)
    elif stage == 2:
        print("""
 
 |
 |
 |
 |
_|_ _ _ _
        """)
    elif stage == 3:
        print("""
  _ _ _
 |/
 |
 |
 |
_|_ _ _ _
        """)
    elif stage == 4:
        print("""
  _ _ _
 |/    | 
 |     U
 |
 |
_|_ _ _ _
        """)
    elif stage == 5:
        print("""
  _ _ _
 |/    |
 |     0
 |
 |
_|_ _ _ _
        """)
    elif stage == 6:
        print("""
  _ _ _
 |/    |
 |     0
 |     |
 |
_|_ _ _ _
        """)
    elif stage == 7:
        print("""
  _ _ _
 |/    |
 |     0
 |    /|
 |
_|_ _ _ _
        """)
    elif stage == 8:
        print("""
  _ _ _
 |/    |
 |     0
 |    /|\\
 |
_|_ _ _ _
        """)
    elif stage == 9:
        print("""
  _ _ _
 |/    |
 |     0
 |    /|\\
 |    /
_|_ _ _ _
        """)
    elif stage == 10:
        print("""
  _ _ _
 |/    |
 |     0
 |    /|\\
 |    / \\
_|_ _ _ _
        """)
    else:
        print("\n\n\n\n\n\n\n")

if __name__ == "__main__":
    test = int(input("Stage? "))
    graphic(test)