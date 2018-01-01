def print_table(table_data):
    col_widths = [0]*len(table_data)
    #print(col_widths)

    #各行の最大値を計測する
    for i in range(len(table_data)):
        for j in range(len(table_data[i])):
            #文字が長い場合、最大値を入れ替える
            if(col_widths[i] < len(table_data[i][j])):
                col_widths[i] = len(table_data[i][j])
    #print(col_widths)

    for i in range(len(table_data[0])):
        data = ''
        for j in range(len(table_data)):
            data += table_data[j][i].rjust(col_widths[j] + 1,' ')
        print(data)

table_data = [['apples', 'orange', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]

print_table(table_data)
