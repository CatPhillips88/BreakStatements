places = ['Tokyo', 'Jamaica', 'Santorini', 'Scotland']

for place in places:
  new_place = input('Where to next? ')

  if new_place == 'quit':
    print('MY LIST:')
    for final_list_item in places:
      print(final_list_item)
    break
  elif new_place in places:
    print('THIS DESTNATION IS ALREADY IN YOUR LIST! ')
  else:
    places.append(new_place)
    for new_list_item in places:
      print(new_list_item)
