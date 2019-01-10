with open( "sampletexttable2.txt" ) as f:
  for item in f:
    st = ""
    for char in item:
        if char == " ":
            st += "*"
        else:
            st += char
    print st
    st = ""
