import re
##### A new variable can't hold a name found in lst_key_words
lst_key_words = ["sifir", "bir", "iki", "uc", "dort", "bes", "alti", "yedi", "sekiz", "dokuz"
                 ,"dogru","yanlis","arti","eksi","carpi","ve","veya","degeri","olsun"," kapa-parantez"
                 ,"ac-parantez","1","2","3","4","5","6","7","8","9","0" ]
values = {"sifir": 0, "bir": 1, "iki" :2, "uc":3, "dort":4 , "bes":5 ,
"alti":6, "yedi":7, "sekiz":8, "dokuz":9,"dogru": True, "yanlis": False,"nokta": ".","arti": "+",
          "eksi" :"-","carpi" : "*"}
Final_result = []
variables = dict()
file_source = open("calc.in")
line_reader = file_source.readlines()
global_counter = 0
height = len(line_reader)
###############################################################
def calculations (elements_2):
        while "*" in elements_2:
            try:
                index_op = elements_2.index("*")
                first = elements_2[index_op - 1]
                second = elements_2[index_op + 1]
                if first in ["True", "False"] or second in ["True", "False"] or type(first) == bool or type(second) == bool:
                    return "Not Valid"
                else:
                    elements_2[index_op] = float(first) * float(second)
                    elements_2.pop(index_op + 1)
                    elements_2.pop(index_op - 1)
            except:
                 return "Not Valid"
        while "+" in elements_2:
            try:
                index_op = elements_2.index("+")
                first = elements_2[index_op - 1]
                second = elements_2[index_op + 1]
                if first in ["True", "False"] or second in ["True", "False"] or type(first) == bool or type(second) == bool:
                    return "Not Valid"
                else:
                    elements_2[index_op] = float(first) + float(second)
                    elements_2.pop(index_op + 1)
                    elements_2.pop(index_op - 1)
            except:
                return "Not Valid"
        while "-" in elements_2:
            try:
                index_op = elements_2.index("-")
                first = elements_2[index_op - 1]
                second = elements_2[index_op + 1]
                if first in ["True", "False"] or second in ["True", "False"] or type(first) == bool or type(second) == bool:
                    return "Not Valid"
                else:
                    elements_2[index_op] = float(first) - float(second)
                    elements_2.pop(index_op + 1)
                    elements_2.pop(index_op - 1)

            except:
                 return "Not Valid"
        while "ve" in elements_2:
            for member in elements_2:
                if member == 'True':
                    elements_2[elements_2.index(member)] = True
                elif member == 'False':
                    elements_2[elements_2.index(member)] = False
                else:
                    pass
            index_op = elements_2.index("ve")
            first = elements_2[index_op - 1]
            second = elements_2[index_op + 1]
            if type(first) == bool and type(second) == bool:
                elements_2[index_op] = first and second
                elements_2.pop(index_op + 1)
                elements_2.pop(index_op - 1)
            else:
                return "Not Valid"
        while "veya" in elements_2:
            for member in elements_2:
                if member == 'True':
                    elements_2[elements_2.index(member)] = True
                elif member == 'False':
                    elements_2[elements_2.index(member)] = False
                else:
                   pass
            index_op = elements_2.index("veya")
            first = elements_2[index_op - 1]
            second = elements_2[index_op + 1]
            if type(first) == bool and type(second) == bool:
                elements_2[index_op] = first or second
                elements_2.pop(index_op + 1)
                elements_2.pop(index_op - 1)
            else:
                return "Not Valid"
        if len(elements_2) == 3:
            if type(elements_2[1]) == str:
                if elements_2[1] == "True":
                    return (True)
                elif elements_2[1] == "False":
                    return (False)
                else:
                    try:
                        elements_2[1] = float(elements_2[1])
                        return (elements_2[1])
                    except:
                         return "Not Valid"
            else:
                return elements_2[1]
        elif len(elements_2) == 1:
            if type(elements_2[0]) == str:
                if elements_2[0] == "True":
                    elements_2[0] = True
                    return (elements_2[0])
                elif elements_2[0] == "False":
                    elements_2[0] = False
                    return (elements_2[0])
                else:
                    try:
                        elements_2[0] = float(elements_2[0])
                        return (elements_2[0])
                    except:
                        return "Not Valid"

            else:
                return elements_2[0]
        else:
             return "Not Valid"
####################################################################
def filtration (excerpt):
    while "(" in excerpt and ")" in excerpt:
        parce_tier_one = re.findall("\([^\(\)]+\)", excerpt)
        elements = parce_tier_one[0].split()
        for i in range(len(elements)):
            if elements[i] in variables.keys():
                elements[i] = variables[elements[i]]
        for i in range(len(elements)):
            if elements[i] in values.keys():
                elements[i] = values[elements[i]]
        result = calculations(elements)
        if result == "Not Valid":
            return "Not Valid"
        else:
           excerpt = excerpt.replace(parce_tier_one[0], str(result))
    elements = excerpt.split()
    for i in range(len(elements)):
        if elements[i] in variables.keys():
            elements[i] = variables[elements[i]]
    for i in range(len(elements)):
        if elements[i] in values.keys():
            elements[i] = values[elements[i]]
    result = calculations(elements)
    return result
###############################################################
def Sonuc (k):
    if_passed = False
    result = 1
    while k < height:
        if len(re.findall("[^ \n]", line_reader[k])) == 0:
            k += 1
        else:
            if if_passed == True:
                return 0
            replacement = re.sub("ac-parantez", "(", line_reader[k])
            line_reader[k] = replacement
            replacement = re.sub("kapa-parantez",")",line_reader[k])
            line_reader[k] = replacement
            if len(re.findall("\.\s+|\s+\.", line_reader[k])) != 0:
                return 0
            if len(re.findall("[0-9]\s+nokta\s[0-9]", line_reader[k])) != 0:
                return 0
            test = line_reader[k]
            zero_check = re.findall("[^\s]*[0-9]{2}[^\s]*", test)
            for element in zero_check:
                if element in variables:
                    pass
                else:
                    return 0
            nokta = "\s+nokta\s+"
            replacement = re.sub(nokta,".",line_reader[k])
            line_reader[k] = replacement
            line_reader[k] = " " + line_reader[k]
            decimal_number = re.findall("\s[^ ]*\.[^ ]*\s", line_reader[k])
            if len(decimal_number) > 0:
                for u in range(len(decimal_number)):
                    decimal = decimal_number[u]
                    for i in values.keys():
                        if len(re.findall(i, decimal_number[u])) > 0:
                            decimal = re.sub(i, str(values[i]), decimal)
                    replacement = re.sub(decimal_number[u], decimal, line_reader[k])
                    line_reader[k] = replacement
            result = filtration(line_reader[k])
            if result == "Not Valid":
               return 0
            else:
                if_passed = True
                k +=1
                Final_result.append(result)

    return 1
#######################################################################
def YeniDegiskenler(j):
    while j < height:
        verify = re.findall("\s*.+\s+degeri.+olsun\s*\n", line_reader[j])
        if len(re.findall("[^ \n]",line_reader[j])) == 0:
            j += 1
        else:
            if len(re.findall("\s*Sonuc\s*",line_reader[j])) == 1:
                return (j+1)
            elif len(verify) == 1:
                replacement = re.sub("ac-parantez", "(", line_reader[j])
                line_reader[j] = replacement
                replacement = re.sub("kapa-parantez", ")", line_reader[j])
                line_reader[j] = replacement
                if len(re.findall("\.\s+|\s+\.",line_reader[j])) !=0:
                    return 0
                if len(re.findall("[0-9]\s+nokta\s[0-9]", line_reader[j])) != 0:
                    return 0
                test = re.sub("olsun", "", line_reader[j])
                test = re.sub(".+degeri", "", test)
                zero_check = re.findall("[^\s]*[0-9]{2}[^\s]*",test)
                for element in zero_check:
                    if element in variables:
                        pass
                    else:
                        return 0
                nokta = "\s+nokta\s+"
                replacement = re.sub(nokta, ".", line_reader[j])
                line_reader[j] = replacement
                decimal_number = re.findall("\s[^ ]+\.[^ ]+\s", line_reader[j])
                if len(decimal_number) > 0:
                        for u in range(len(decimal_number)):
                            decimal = decimal_number[u]
                            for i in values.keys():
                                if len(re.findall(i, decimal_number[u])) > 0:
                                    decimal = re.sub(i, str(values[i]),decimal)
                            replacement = re.sub(decimal_number[u], decimal,line_reader[j])
                            line_reader[j] = replacement
            if len(re.findall("\([^a-zA-Z0-9]\)", line_reader[j])) > 0:
                return 0
            if len(re.findall("\(", line_reader[j])) == len(re.findall("\)", line_reader[j])):
                line_reader[j] = line_reader[j].strip()
                lst_elements = line_reader[j].split()
                if len(lst_elements[0]) > 10 or len(re.findall("[^a-zA-Z0-9]", lst_elements[0])) > 0 or lst_elements[
                    0] in variables:
                    return 0
                else:
                    replacement = line_reader[j]
                    line_reader[j] = re.sub("olsun", "", replacement)
                    replacement = line_reader[j]
                    line_reader[j] = re.sub(".+degeri", "", replacement)
                    replacement = line_reader[j]
                    line_reader[j] = line_reader[j].strip()
                    result = filtration(line_reader[j])
                    if result == "Not Valid":
                        return 0
                    else:
                        variables[lst_elements[0]] = result
                        j += 1
            else:
                return 0

    else:
        return 0
#######################################################################
def AnaDegiskenler (i):
    while i<height:
        if len(re.findall("[^ \n]",line_reader[i])) == 0:
            i+=1
        else:
            verify_blanck = re.findall("\s*AnaDegiskenler\s*\n", line_reader[i])
            if len(verify_blanck) == 1:
                    i+=1
                    break
            else:
                return 0
    while i < height:
        if len(re.findall("[^ \n]",line_reader[i])) == 0:
            i += 1
        else:
            if len(re.findall("\.\s+|\s+\.", line_reader[i])) != 0:
                return 0
            if len(re.findall("[0-9]\s+nokta\s[0-9]", line_reader[i])) != 0:
                return 0
            nokta = "\s+nokta\s+"
            lst_nokta = re.findall(nokta, line_reader[i])
            if len(lst_nokta) == 1:
                line_reader[i] = line_reader[i].replace(lst_nokta[0], ".")
            verify = re.findall("\s*([^ \n]+)\s*", line_reader[i])
            if len(verify) == 1:
                if verify[0] == "YeniDegiskenler":
                    final = i + 1
                    break
                else:
                    return 0
            else:
                if len(re.findall("\s*.+\s+degeri\s+.+\s+olsun\s*", line_reader[i])) == 1:
                    lst_line = verify
                    if lst_line[0] in variables or lst_line[0] in lst_key_words:
                        return 0
                    else:
                        if len(lst_line[0]) > 10 or len(re.findall("[^a-zA-Z0-9]", lst_line[0])) > 0:
                            return 0
                        else:
                            test = re.sub("olsun","",line_reader[i])
                            test = re.sub(".+degeri","", test)
                            if len(re.findall("[0-9]{2}",test)) != 0:
                                return 0
                            else:
                                elements_list = test.split()
                                if len(elements_list) != 1:
                                    return 0
                                else:
                                    variables[lst_line[0]] = lst_line[2]
                                    i += 1

                else:
                    return 0
    for i, k in variables.items():
        for element in values:
            if len(re.findall(element, k)) > 0:
                m = re.sub(element, str(values[element]),str(k))
                k = m
        if k == "True":
            variables[i] = True
        elif k == "False":
            variables[i] = False
        elif len(re.findall("[^[1-9]\.]", k)) > 0:
            return 0
        else:
            try:
              variables[i] = float(k)
            except:
                return 0
    return final
########################################################################
failed = open("calc.out", "w")
global_counter = AnaDegiskenler(global_counter)
if global_counter !=0:
    global_counter = YeniDegiskenler(global_counter)
    if global_counter !=0:
        global_counter = Sonuc(global_counter)
        if global_counter != 0:
            failed.write("Here Comes the Sun")
        else:
            failed.write("Dont Let Me Down")
    else:
       failed.write("Dont Let Me Down")
else:
    failed.write("Dont Let Me Down")
###########################################################
failed.close()
file_source.close()
