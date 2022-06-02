def run():

    counts = dict()
    name_list = []
    print('Enter a name: ')
    name = input('')
    name_lower = name.lower(), name_list.append(name_lower)
    add_name = name_list.append(name_lower)
    ask = input('Do you want to enter another name?(y/n): ')
    ask_lower = ask.lower()
    while ask_lower == 'y':
        print('Enter a name: ')
        name = input('')
        name_lower = name.lower(), name_list.append(name_lower)
        add_name = name_list.append(name_lower)
        ask = input('Do you want to enter another name?(y/n): ')
        ask_lower = ask.lower()
        
        if ask_lower == 'n':
            break
    for names in name_list:
        counts[names] = counts.get(names, 0) + 1
    print(counts)
    

if __name__ == "__main__":
    run()