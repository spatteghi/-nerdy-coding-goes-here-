#funky shins my guy

# puts seereees or simbuls at start and end of text (for emfasus)
def statement_generator(text, decoration):

    #make some bullshit decorations real quick
    ends = decoration * 5
    
    # add deckarashin to start and end statment
    statement = "{}  {}  {}".format(ends, text, ends)

    print()
    print(statement)
    print()

    return""

# main shit go hea
statement_generator("cash monay", "$")