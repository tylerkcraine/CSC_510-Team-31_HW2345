
def parser(data):
    col_header = []

    count = data.split("\n")

    pos = data.find('\n')
    col_header = data[0:pos].split(",")

    col_header_list = [ [] for l in range(len(col_header)) ]

    # Extracting data
    data_split = data.split("\n")
    j = 0
    while j < len(col_header_list):
            i = 1
            while i < len(count):
                    col_header_list[j].append(data_split[i].split(",")[j])
                    # print(data_split[i].split(",")[j])
                    i += 1
            j+= 1

    dicts = {}
    p = 0
    while p < len(col_header):
        dicts[col_header[p]] = col_header_list[p]
        p +=1

    return dicts
