from sleeper_wrapper import League

def test():
    league = League('732312711840550912')
    d_users = league.get_users()
    names = []
    for u in d_users:
        names.append(u['display_name'])
    
    return names
