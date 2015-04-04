given_string = "I think %s is a perfectly normal thing to do in public."
given_string2 = "I think %s and %s are perfectly normal things to do in public."
given_string3 = "I'm %(nickname)s. My real name is %(name)s, but my friends call me %(nickname)s."

def sub1(s):
    #return given_string%s
    print given_string%s

def sub2(s1, s2):
    #return given_string2 %(s1,s2)
    print given_string2 %(s1,s2)

def sub_m(name, nickname):
    #return given_string3% {"nickname": nickname, "name" : name}
    print given_string3% {"nickname": nickname, "name" : name} 

sub1("Me")
sub2("Me","You")
sub_m("Hasitha", "Haz")
