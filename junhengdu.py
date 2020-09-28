import xlrd
import ipywidgets as widgets
from IPython.display import display, Javascript
from matplotlib import pyplot as plt 

def drawing(index,temp_out,subject_list,alldata,ave):

    difference_list = []

    temp_out.clear_output()

    with temp_out:
        for i in range(3,8):
            difference_list = difference_list + [(alldata[str(index)][i] - ave)]
        plt.bar(subject_list, difference_list, align =  'center') 
        plt.title('Five subjects balance') 
        plt.ylabel('Difference') 
        plt.xlabel('Subject')
        for a,b in zip(subject_list,difference_list):
            plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=11)
        plt.show()
    
    return

def jianyousheng(grid,table,nrows):

    temp_grid = widgets.GridspecLayout(10,2,width = 'auto',height = 'auto')
    temp_out = widgets.Output(layout={'border': '1px solid black','width':'16cm','height':'9cm'})
    alldata = {}
    data = []
    
    for i in range(2,32):
        data = table.row_values(i)
        alldata[str(i-2)] = data
        

    temp_grid[0,0] = widgets.Dropdown(options=[('第一名', 0),('第二名', 1),('第三名', 2),('第四名', 3),('第五名', 4),
                                                       ('第六名', 5),('第七名', 6),('第八名', 7),('第九名', 8),('第十名', 9),
                                                       ('第十一名', 10),('第十二名', 11),('第十三名', 12),('第十四名', 13),('第十五名', 14),
                                                       ('第十六名', 15),('第十七名', 16),('第十八名', 17),('第十九名', 18),('第二十名', 19),
                                                       ('第二十一名', 20),('第二十二名', 21),('第二十三名', 22),('第二十四名', 23),('第二十五名', 24),
                                                       ('第二十六名', 25),('第二十七名', 26),('第二十八名', 27),('第二十九名', 28),('第三十名', 29)],
                                      index = 0,
                                      layout = widgets.Layout(width = '3cm'))
    temp_grid[1,0] = widgets.Button(description = alldata['0'][0],tooltip = '班级',layout = widgets.Layout(width = '3cm'))
    temp_grid[2,0] = widgets.Button(description = alldata['0'][1],tooltip = '学号',layout = widgets.Layout(width = '3cm'))
    temp_grid[3,0] = widgets.Button(description = alldata['0'][2],tooltip = '姓名',layout = widgets.Layout(width = '3cm'))
    temp_grid[4,0] = widgets.Button(description = str(alldata['0'][18]).split('.')[0],tooltip = '总分',layout = widgets.Layout(width = '3cm'))

    ave = alldata['0'][18] / 5
    subject_list = ['Chinese','Math','English','Physical','Chemistry']

    drawing(0,temp_out,subject_list,alldata,ave)

    grid[1:19,0:30].children[0].children[4].children = [widgets.HBox([temp_grid,temp_out])]    
    

    def show_info(change):

        value  = change['new']
        
        temp_grid[1,0].description = alldata[str(value)][0]
        temp_grid[2,0].description = alldata[str(value)][1]
        temp_grid[3,0].description = alldata[str(value)][2]
        temp_grid[4,0].description = str(alldata[str(value)][18]).split('.')[0]

        drawing(value,temp_out,subject_list,alldata,ave)
            
    temp_grid[0,0].observe(show_info,names = 'index')
    

    return
