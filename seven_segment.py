def broken_timer(working_leds,broken_leds):
    first_screen = []
    second_screen = []
    for i in working_leds:
        first_screen.append(i.lower()) if i.isupper() else second_screen.append(i)
    first_screen.sort()
    second_screen.sort()
    first_screen=tuple(first_screen)
    second_screen=tuple(second_screen)
    first_screen_broken = []
    second_screen_broken = []
    for i in broken_leds:
        first_screen_broken.append(i.lower()) if i.isupper() else second_screen_broken.append(i)
    first_screen_broken.sort()
    second_screen_broken.sort()
    first_screen_broken=tuple(first_screen_broken)
    second_screen_broken=tuple(second_screen_broken)
    n1=1 if first_screen in dic_of_digits else 0
    n2=1 if second_screen in dic_of_digits else 0
    for i in first_screen_broken:
        newlist = list(first_screen+tuple(i))
        newlist.sort()
        newlist = tuple(newlist)
        if newlist1st in dic_of_digits.keys():
            n1+=1
    for i in second_screen_broken:
        newlist = list(second_screen+tuple(i))
        newlist.sort()
        newlist = tuple(newlist)
        if newlist1st in dic_of_digits.keys():
            n2+=1
    print(n1+n2)