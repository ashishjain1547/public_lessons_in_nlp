import copy

with open('list_of_entity_names.txt') as f:
    entity_names = f.read()
entity_names = list(set(entity_names.split(";")))

#print(entity_names)


def getAnnotatedStrings(textStr, entity_label = 'MY_ENTITY'):
    textStr = textStr.replace("'", "").replace("^ ", "") # Cleaning of text from Wikipedia
    haveMoreEntities = True
    
    entity_position = []
    entity_titles = []
    for entityStr in entity_names:
        start = textStr.find(entityStr)
        end = start + len(entityStr)
        if start != -1 and (not textStr[start - 1].isalnum()):
            # By the condition (not textStr[start - 1].isalnum()) we check that the match found is not in the middle of another word.
            try:
                if (not textStr[end].isalnum()):
                    entity_position += [(start, end, entity_label)]
                    entity_titles += [entityStr]
            except:
                entity_position += [(start, end, entity_label)]
                entity_titles += [entityStr]
    

    print("Initial discovery of entities: ", entity_position)
    print("Initial discovery of entity titles: ", entity_titles)
    print()

    # This "if" block was used for an activity with data related to 'pragramming languages'.
    # entity_titles.index('C') Throws "ValueError: element is not in list"
    if 'C' in entity_titles:
        c_variants = []
        if 'C#' in entity_titles:
            c_variants.append('C#')
        if 'C++' in entity_titles:
            c_variants.append('C++')
        if 'Objective-C' in entity_titles:
            c_variants.append('Objective-C')
        if len(c_variants) > 0:
            for i in c_variants:
                try:
                    c_start = entity_position[entity_titles.index('C')][0]
                except:
                    break
                i_start = entity_position[entity_titles.index(i)][0]
                i_end = entity_position[entity_titles.index(i)][1]
                if c_start >= i_start and c_start <= i_end:
                    del entity_position[entity_titles.index('C')]
                    entity_titles.remove('C') # First 'C' removed.

    overlap_detection_arr = []
    entity_position_out = copy.deepcopy(entity_position)
    
    for i in entity_position:
        temp_arr = []
        for j in entity_position:
            # This "i[1] < j[1] and i[1] > j[0]" is the overlap of kind: 
            # 'ashish', 'ishleen' being picked from a hypothetical word 'ashishleen'.
            if i[1] < j[1] and i[1] > j[0]:
                len1 = i[1] - i[0]
                len2 = j[1] - j[0]
                if len1 > len2:
                    try:
                        entity_position_out.remove(j)
                        del entity_titles[entity_position.index(j)]
                    except:
                        #print("Element not found.")
                        pass
                else:
                    try:
                        entity_position_out.remove(i)
                        del entity_titles[entity_position.index(i)]
                    except:
                        #print("Element not found.")
                        pass
                print("Overlap detected.")  
            else:
                temp_arr.append(False)

            # This "i[0] > j[0] and i[0] < j[1]" is the overlap of kind: jean (denoted by 'i'), greyjean (denoted by 'j')
            if i[0] > j[0] and i[0] < j[1]:
                len1 = i[1] - i[0]
                len2 = j[1] - j[0]
                if len1 > len2:
                    try:
                        entity_position_out.remove(j)
                        del entity_titles[entity_position.index(j)]
                    except:
                        #print("Element not found.")
                        pass
                else:
                    try:
                        entity_position_out.remove(i)
                        del entity_titles[entity_position.index(i)]
                    except:
                        #print("Element not found.")
                        pass
                print("Overlap detected.")  
            else:
                temp_arr.append(False)
        overlap_detection_arr.append(temp_arr)

    if len(entity_titles) > 0:
        rv = (str(textStr), {'entities': entity_position_out})
        print(rv)
        print()
        return rv
