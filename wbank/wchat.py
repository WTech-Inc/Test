from j import complie

jCode = """
  // prints : print string
  // printIn : print Integer
  // printf : print with float
  public static void start() {
    for ( Integer i = 0 ; i < 5 ; System.output.printIn(i)) {
      i += 1;
    }
    System.output.prints("Loop complete");
  }
"""

print(complie(jCode, target="py"))
# Then it will transfer to py lang