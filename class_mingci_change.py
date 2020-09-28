import xlrd
import ipywidgets as widgets
from IPython.display import display, Javascript
import numpy as np

def sort_index(x,data):

    index = 1

    for i in data:
        if i > x:
            index = index + 1
    
    return index 

def mingci_change(grid,table,nrows,ncols,shikao_count):

    temp_grid = widgets.GridspecLayout(18,19,width = 'auto',height = 'auto')
    
    for i in range(2,18):
        for j in range(19):
            temp_grid[i,j] = widgets.Button(layout = widgets.Layout(width='auto',height='0.8cm'))
            if j == 0:
                temp_grid[i,j].description = str(i-1)

    temp_grid[0:2,0] = widgets.Button(style = {'button_color':'#004080'},
                                      button_style = 'info',
                                      layout = widgets.Layout(width='auto',height='1.6cm'),
                                      description = '班')
    temp_grid[0,1:4] = widgets.Button(style = {'button_color':'#004080'},
                                      button_style = 'info',
                                      layout = widgets.Layout(width='auto',height='0.8cm'),
                                      description = '数学')
    temp_grid[0,4:7] = widgets.Button(style = {'button_color':'#004080'},
                                      button_style = 'info',
                                      layout = widgets.Layout(width='auto',height='0.8cm'),
                                      description = '语文')
    temp_grid[0,7:10] = widgets.Button(style = {'button_color':'#004080'},
                                      button_style = 'info',
                                      layout = widgets.Layout(width='auto',height='0.8cm'),
                                      description = '英语')
    temp_grid[0,10:13] = widgets.Button(style = {'button_color':'#004080'},
                                      button_style = 'info',
                                      layout = widgets.Layout(width='auto',height='0.8cm'),
                                      description = '物理')
    temp_grid[0,13:16] = widgets.Button(style = {'button_color':'#004080'},
                                      button_style = 'info',
                                      layout = widgets.Layout(width='auto',height='0.8cm'),
                                      description = '化学')
    temp_grid[0,16:19] = widgets.Button(style = {'button_color':'#004080'},
                                      button_style = 'info',
                                      layout = widgets.Layout(width='auto',height='0.8cm'),
                                      description = '总分')

    
    for i in range(1,19):
        if i in [1,4,7,10,13,16]:
            temp_grid[1,i] = widgets.Button(style = {'button_color':'#FFC125'},
                                      button_style = 'info',
                                      layout = widgets.Layout(width='auto',height='0.8cm'),
                                      description = '基')
        elif i in [2,5,8,11,14,17]:
            temp_grid[1,i] = widgets.Button(style = {'button_color':'#FFC125'},
                                      button_style = 'info',
                                      layout = widgets.Layout(width='auto',height='0.8cm'),
                                      description = '本')
        elif i in [3,6,9,12,15,18]:
            temp_grid[1,i] = widgets.Button(style = {'button_color':'#CD3333'},
                                      button_style = 'info',
                                      layout = widgets.Layout(width='auto',height='0.8cm'),
                                      description = '变')
    
    grid[1:19,0:30].children[0].children[1].children = [temp_grid]

    # ------------  相关计算    --------------------#
    '''
    sort_math = all_math = [0] * 16
    sort_chinese = all_chinese = [0] * 16
    sort_english = all_english = [0] * 16
    sort_physical = all_physical = [0] * 16
    sort_chemistry = all_chemistry = [0] * 16
    sort_total = all_total = [0] * 16

    

    for i in range(2, nrows):#第0、1行为表头
        
        alldata = table.row_values(i)#循环输出excel表中每一行，即所有数据
        class_num = int(alldata[0])
        all_chinese[class_num - 1] = all_chinese[class_num - 1] + alldata[3]
        all_math[class_num - 1] = all_math[class_num - 1] + alldata[4]
        all_english[class_num - 1] = all_english[class_num - 1] + alldata[5]
        all_physical[class_num - 1] = all_physical[class_num - 1] + alldata[6]
        all_chemistry[class_num - 1] = all_chemistry[class_num - 1] + alldata[7]
        all_total[class_num - 1] = all_total[class_num - 1] + alldata[18]

    all_data = [all_chinese,all_math,all_english,all_physical,all_chemistry]
    


    for i in range(16):
        all_math[i] = all_math[i] / shikao_count[i]
        all_chinese[i] = all_chinese[i] / shikao_count[i]
        all_english[i] = all_english[i] / shikao_count[i]
        all_physical[i] = all_physical[i] / shikao_count[i]
        all_chemistry[i] = all_chemistry[i] / shikao_count[i]
        all_total[i] = all_total[i] / shikao_count[i] 
        
    for i in range(16):
        sort_math[i] = sort_index(all_math[i],all_math)
        sort_chinese[i] = sort_index(all_chinese[i],all_chinese)
        sort_english[i] = sort_index(all_english[i],all_english)
        sort_physical[i] = sort_index(all_physical[i],all_physical)
        sort_chemistry[i] = sort_index(all_chemistry[i],all_chemistry)
        sort_total[i] = sort_index(all_total[i],all_total)

    for i in range(16):
        for j in [2,5,8,11,14,17]:
            if j == 2:
                temp_grid[i,j].description = str(sort_math[i])
            elif j == 5:
                temp_grid[i,j].description = str(sort_chinese[i])
            elif j == 8:
                temp_grid[i,j].description = str(sort_english[i])
            elif j == 11:
                temp_grid[i,j].description = str(sort_physical[i])
            elif j == 14:
                temp_grid[i,j].description = str(sort_chemistry[i])
            elif j == 17:
                temp_grid[i,j].description = str(sort_total[i])
    '''
    
    return
