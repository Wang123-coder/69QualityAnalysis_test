import xlrd
import ipywidgets as widgets

#  计算参考率
def cankaolv(out,grid,table,nrows,ncols):

    cankaolv_grid = widgets.GridspecLayout(17,5,width = 'auto',height = 'auto')
    shikao_count = [0] * 16
    quekao_name = ['']*16
    
    for j in range(17):
        for i in range(4):

            cankaolv_grid[j,i] = widgets.Button(layout = widgets.Layout(width='auto',height='0.8cm'))
                
            if j == 0:
                cankaolv_grid[j,i].style = {'button_color':'#004080'}
                cankaolv_grid[j,i].button_style = 'info'
            if i == 0:
                cankaolv_grid[j,i].description = str(j)+'班'
            elif i == 1:
                cankaolv_grid[j,i].description = '50'
            
    cankaolv_grid[0,4] = widgets.Dropdown(options=[('1班', 0), ('2班', 1), ('3班', 2),('4班',3),
                                                   ('5班', 4), ('6班', 5), ('7班', 6),('8班',7),
                                                   ('9班', 8), ('10班', 9), ('11班', 10),('12班',11),
                                                   ('13班', 12), ('14班', 13), ('15班', 14),('16班',15),
                                                   ('',16)],
                                          index = 16,
                                    layout = widgets.Layout(width = 'auto'),
                                    description='缺考名单： ')
    cankaolv_grid[0,0].description = '班级'
    cankaolv_grid[0,1].description = '在籍人数'
    cankaolv_grid[0,2].description = '实考人数'
    cankaolv_grid[0,3].description = '参考率'
    cankaolv_grid[1:10,4] = widgets.HBox([widgets.Label(layout = widgets.Layout(width = '0.2cm')),widgets.Textarea(layout = widgets.Layout(width = '4cm',height = '6cm'))])
    grid[1:19,0:30].children[0].children[0].children = [cankaolv_grid]

    
    for i in range(2, nrows):#第0、1行为表头
        alldata = table.row_values(i)#循环输出excel表中每一行，即所有数据
        if str(alldata[0]).split('.')[0] == '1' and alldata[18] > 0.01:
            shikao_count[0] = shikao_count[0] + 1
        elif str(alldata[0]).split('.')[0] == '1' and alldata[18] < 0.01:
            quekao_name[0] = '   ' + quekao_name[0] + alldata[2] + '\n'

        if str(alldata[0]).split('.')[0] == '2' and alldata[18] > 0.01:
            shikao_count[1] = shikao_count[1] + 1
        elif str(alldata[0]).split('.')[0] == '2' and alldata[18] < 0.01:
            quekao_name[1] = '   ' + quekao_name[1] + alldata[2] + '\n'
            
        if str(alldata[0]).split('.')[0] == '3' and alldata[18] > 0.01:
            shikao_count[2] = shikao_count[2] + 1
        elif str(alldata[0]).split('.')[0] == '3' and alldata[18] < 0.01:
            quekao_name[2] = '   ' + quekao_name[2] + alldata[2] + '\n'
            
        if str(alldata[0]).split('.')[0] == '4' and alldata[18] > 0.01:
            shikao_count[3] = shikao_count[3] + 1
        elif str(alldata[0]).split('.')[0] == '4' and alldata[18] < 0.01:
            quekao_name[3] = '   ' + quekao_name[3] + alldata[2] + '\n'

        if str(alldata[0]).split('.')[0] == '5' and alldata[18] > 0.01:
            shikao_count[4] = shikao_count[4] + 1
        elif str(alldata[0]).split('.')[0] == '5' and alldata[18] < 0.01:
            quekao_name[4] = '   ' + quekao_name[4] + alldata[2] + '\n'

        if str(alldata[0]).split('.')[0] == '6' and alldata[18] > 0.01:
            shikao_count[5] = shikao_count[5] + 1
        elif str(alldata[0]).split('.')[0] == '6' and alldata[18] < 0.01:
            quekao_name[5] = '   ' + quekao_name[5] + alldata[2] + '\n'

        if str(alldata[0]).split('.')[0] == '7' and alldata[18] > 0.01:
            shikao_count[6] = shikao_count[6] + 1
        elif str(alldata[0]).split('.')[0] == '7' and alldata[18] < 0.01:
            quekao_name[6] = '   ' + quekao_name[6] + alldata[2] + '\n'

        if str(alldata[0]).split('.')[0] == '8' and alldata[18] > 0.01:
            shikao_count[7] = shikao_count[7] + 1
        elif str(alldata[0]).split('.')[0] == '8' and alldata[18] < 0.01:
            quekao_name[7] = '   ' + quekao_name[7] + alldata[2] + '\n'

        if str(alldata[0]).split('.')[0] == '9' and alldata[18] > 0.01:
            shikao_count[8] = shikao_count[8] + 1
        elif str(alldata[0]).split('.')[0] == '9' and alldata[18] < 0.01:
            quekao_name[8] = '   ' + quekao_name[8] + alldata[2] + '\n'

        if str(alldata[0]).split('.')[0] == '10' and alldata[18] > 0.01:
            shikao_count[9] = shikao_count[9] + 1
        elif str(alldata[0]).split('.')[0] == '10' and alldata[18] < 0.01:
            quekao_name[9] = '   ' + quekao_name[9] + alldata[2] + '\n'

        if str(alldata[0]).split('.')[0] == '11' and alldata[18] > 0.01:
            shikao_count[10] = shikao_count[10] + 1
        elif str(alldata[0]).split('.')[0] == '11' and alldata[18] < 0.01:
            quekao_name[10] = '   ' + quekao_name[10] + alldata[2] + '\n'

        if str(alldata[0]).split('.')[0] == '12' and alldata[18] > 0.01:
            shikao_count[11] = shikao_count[11] + 1
        elif str(alldata[0]).split('.')[0] == '12' and alldata[18] < 0.01:
            quekao_name[11] = '   ' + quekao_name[11] + alldata[2] + '\n'

        if str(alldata[0]).split('.')[0] == '13' and alldata[18] > 0.01:
            shikao_count[12] = shikao_count[12] + 1
        elif str(alldata[0]).split('.')[0] == '13' and alldata[18] < 0.01:
            quekao_name[12] = '   ' + quekao_name[12] + alldata[2] + '\n'

        if str(alldata[0]).split('.')[0] == '14' and alldata[18] > 0.01:
            shikao_count[13] = shikao_count[13] + 1
        elif str(alldata[0]).split('.')[0] == '14' and alldata[18] < 0.01:
            quekao_name[13] = '   ' + quekao_name[13] + alldata[2] + '\n'

        if str(alldata[0]).split('.')[0] == '15' and alldata[18] > 0.01:
            shikao_count[14] = shikao_count[14] + 1
        elif str(alldata[0]).split('.')[0] == '15' and alldata[18] < 0.01:
            quekao_name[14] = '   ' + quekao_name[14] + alldata[2] + '\n'

        if str(alldata[0]).split('.')[0] == '16' and alldata[18] > 0.01:
            shikao_count[15] = shikao_count[15] + 1
        elif str(alldata[0]).split('.')[0] == '16' and alldata[18] < 0.01:
            quekao_name[15] = '   ' + quekao_name[15] + alldata[2] + '\n'
            
    for i in range(16):
        cankaolv_grid[i+1,2].description = str(shikao_count[i])
        cankaolv_grid[i+1,3].description = str(shikao_count[i] / int(cankaolv_grid[i+1,1].description)) + '%'

    def show_quekao(change):
        value = change['new']
        if value == 0:
            cankaolv_grid[1:10,4].children[1].value = quekao_name[0]
        elif value == 1:
            cankaolv_grid[1:10,4].children[1].value = quekao_name[1]
        elif value == 2:
            cankaolv_grid[1:10,4].children[1].value = quekao_name[2]
        elif value == 3:
            cankaolv_grid[1:10,4].children[1].value = quekao_name[3]
        elif value == 4:
            cankaolv_grid[1:10,4].children[1].value = quekao_name[4]
        elif value == 5:
            cankaolv_grid[1:10,4].children[1].value = quekao_name[5]
        elif value == 6:
            cankaolv_grid[1:10,4].children[1].value = quekao_name[6]
        elif value == 7:
            cankaolv_grid[1:10,4].children[1].value = quekao_name[7]
        elif value == 8:
            cankaolv_grid[1:10,4].children[1].value = quekao_name[8]
        elif value == 9:
            cankaolv_grid[1:10,4].children[1].value = quekao_name[9]
        elif value == 10:
            cankaolv_grid[1:10,4].children[1].value = quekao_name[10]
        elif value == 11:
            cankaolv_grid[1:10,4].children[1].value = quekao_name[11]
        elif value == 12:
            cankaolv_grid[1:10,4].children[1].value = quekao_name[12]
        elif value == 13:
            cankaolv_grid[1:10,4].children[1].value = quekao_name[13]
        elif value == 14:
            cankaolv_grid[1:10,4].children[1].value = quekao_name[14]
        elif value == 15:
            cankaolv_grid[1:10,4].children[1].value = quekao_name[15]
    cankaolv_grid[0,4].observe(show_quekao,names='value')
    
    return shikao_count
