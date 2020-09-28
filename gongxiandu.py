import xlrd
import ipywidgets as widgets
from IPython.display import display, Javascript
import matplotlib
import matplotlib.pyplot as plt

def drawing(temp_out,chinese_y,math_y,english_y,physical_y,chemistry_y,class_num):

    temp_out.clear_output()

    x = ['1', '2', '3', '4']

    with temp_out:
        plt.plot(x, chinese_y, marker='*', ms=10, label="Chinese")
        plt.plot(x, math_y, marker='*', ms=10, label="Math")
        plt.plot(x, english_y, marker='*', ms=10, label="English")
        plt.plot(x, physical_y, marker='*', ms=10, label="Physical")
        plt.plot(x, chemistry_y, marker='*', ms=10, label="Chemistry")
        plt.xlabel("Test times",fontsize=20)
        plt.ylabel("Ranking",fontsize=20)
        plt.title("Contribution of subject to class " + class_num,fontsize=20)
        plt.legend(loc="upper left")
        plt.ylim(0,32)
        # 在折线图上显示具体数值, ha参数控制水平对齐方式, va控制垂直对齐方式
        for y in [chinese_y, math_y, english_y, physical_y, chemistry_y]:
            for x1, yy in zip(x, y):
                plt.text(x1, yy+1, str(yy), ha='center', va='bottom', fontsize=20, rotation=0)
        plt.savefig("a.jpg")
        plt.show()

    return

def gongxianToClass(grid,table,nrows):

    temp_grid = widgets.GridspecLayout(30,1,width = 'auto',height = 'auto')
    temp_out = widgets.Output(layout={'border': '1px solid black','width':'16cm','height':'9cm'})

    temp_grid[0,0] = widgets.Dropdown(options=[('1班', 0),('2班', 1),('3班', 2),('4班', 3),('5班', 4),
                                               ('6班', 5),('7班', 6),('8班', 7),('9班', 8),('10班', 9),
                                               ('11班', 10),('12班', 11),('13班', 12),('14班', 13),('15班', 14),('16班', 15),('',16)],
                                      index = 16,
                                      layout = widgets.Layout(width = '5cm'),
                                      description = '班级')
    for i in range(1,25):
        
        if i == 1:
            temp_grid[i,0] = widgets.Text(value = '考次1',layout = widgets.Layout(width = '5cm'),disabled = True)
        elif i == 7:
            temp_grid[i,0] = widgets.Text(value = '考次2',layout = widgets.Layout(width = '5cm'),disabled = True)
        elif i == 13 :
            temp_grid[i,0] = widgets.Text(value = '考次3',layout = widgets.Layout(width = '5cm'),disabled = True)
        elif i == 19:
            temp_grid[i,0] = widgets.Text(value = '考次4',layout = widgets.Layout(width = '5cm'),disabled = True)
        else:
            temp_grid[i,0] = widgets.Dropdown(options = [('第1名', 0),('第2名', 1),('第3名', 2),('第4名', 3),('第5名', 4),
                                               ('第6名', 5),('第7名', 6),('第8名', 7),('第9名', 8),('第10名', 9),
                                               ('第11名', 10),('第12名', 11),('第13名', 12),('第14名', 13),('第15名', 14),('第16名', 15),('',16)],index = 16,
                                              layout = widgets.Layout(width = '5cm'))
            if i in [2,8,14,20]:
                temp_grid[i,0].description = '语文'
            elif i in [3,9,15,21]:
                temp_grid[i,0].description = '数学'
            elif i in [4,10,16,22]:
                temp_grid[i,0].description = '英语'
            elif i in [5,11,17,23]:
                temp_grid[i,0].description = '物理'
            elif i in [6,12,18,24]:
                temp_grid[i,0].description = '化学'
            
    
    
    grid[1:19,0:30].children[0].children[5].children = [widgets.HBox([temp_grid,temp_out])]

    chinese_y = [0]*4
    math_y = [0]*4
    english_y = [0]*4
    physical_y = [0]*4
    chemistry_y = [0]*4

    with temp_out:
        print('请先在左侧进行选择！')

    def show_info_20(change):
        chinese_y[0] = change['new'] + 1
        drawing(temp_out,chinese_y,math_y,english_y,physical_y,chemistry_y,str(temp_grid[0,0].index + 1))   
    temp_grid[2,0].observe(show_info_20,names = 'index')

    def show_info_30(change):
        math_y[0] = change['new'] + 1
        drawing(temp_out,chinese_y,math_y,english_y,physical_y,chemistry_y,str(temp_grid[0,0].index + 1))   
    temp_grid[3,0].observe(show_info_30,names = 'index')

    def show_info_40(change):
        english_y[0] = change['new'] + 1
        drawing(temp_out,chinese_y,math_y,english_y,physical_y,chemistry_y,str(temp_grid[0,0].index + 1))   
    temp_grid[4,0].observe(show_info_40,names = 'index')

    def show_info_50(change):
        physical_y[0] = change['new'] + 1
        drawing(temp_out,chinese_y,math_y,english_y,physical_y,chemistry_y,str(temp_grid[0,0].index + 1))   
    temp_grid[5,0].observe(show_info_50,names = 'index')

    def show_info_60(change):
        chemistry_y[0] = change['new'] + 1
        drawing(temp_out,chinese_y,math_y,english_y,physical_y,chemistry_y,str(temp_grid[0,0].index + 1))   
    temp_grid[6,0].observe(show_info_60,names = 'index')

    #--------------------------------------------------#

    def show_info_80(change):
        chinese_y[1] = change['new'] + 1
        drawing(temp_out,chinese_y,math_y,english_y,physical_y,chemistry_y,str(temp_grid[0,0].index + 1))   
    temp_grid[8,0].observe(show_info_80,names = 'index')

    def show_info_90(change):
        math_y[1] = change['new'] + 1
        drawing(temp_out,chinese_y,math_y,english_y,physical_y,chemistry_y,str(temp_grid[0,0].index + 1))   
    temp_grid[9,0].observe(show_info_90,names = 'index')

    def show_info_100(change):
        english_y[1] = change['new'] + 1
        drawing(temp_out,chinese_y,math_y,english_y,physical_y,chemistry_y,str(temp_grid[0,0].index + 1))   
    temp_grid[10,0].observe(show_info_100,names = 'index')

    def show_info_110(change):
        physical_y[1] = change['new'] + 1
        drawing(temp_out,chinese_y,math_y,english_y,physical_y,chemistry_y,str(temp_grid[0,0].index + 1))   
    temp_grid[11,0].observe(show_info_110,names = 'index')

    def show_info_120(change):
        chemistry_y[1] = change['new'] + 1
        drawing(temp_out,chinese_y,math_y,english_y,physical_y,chemistry_y,str(temp_grid[0,0].index + 1))   
    temp_grid[12,0].observe(show_info_120,names = 'index')

    #--------------------------------------------------#
    def show_info_140(change):
        chinese_y[2] = change['new'] + 1
        drawing(temp_out,chinese_y,math_y,english_y,physical_y,chemistry_y,str(temp_grid[0,0].index + 1))   
    temp_grid[14,0].observe(show_info_140,names = 'index')

    def show_info_150(change):
        math_y[2] = change['new'] + 1
        drawing(temp_out,chinese_y,math_y,english_y,physical_y,chemistry_y,str(temp_grid[0,0].index + 1))   
    temp_grid[15,0].observe(show_info_150,names = 'index')

    def show_info_160(change):
        english_y[2] = change['new'] + 1
        drawing(temp_out,chinese_y,math_y,english_y,physical_y,chemistry_y,str(temp_grid[0,0].index + 1))   
    temp_grid[16,0].observe(show_info_160,names = 'index')

    def show_info_170(change):
        physical_y[2] = change['new'] + 1
        drawing(temp_out,chinese_y,math_y,english_y,physical_y,chemistry_y,str(temp_grid[0,0].index + 1))   
    temp_grid[17,0].observe(show_info_170,names = 'index')

    def show_info_180(change):
        chemistry_y[2] = change['new'] + 1
        drawing(temp_out,chinese_y,math_y,english_y,physical_y,chemistry_y,str(temp_grid[0,0].index + 1))   
    temp_grid[18,0].observe(show_info_180,names = 'index')

    #--------------------------------------------------#
    def show_info_200(change):
        chinese_y[3] = change['new'] + 1
        drawing(temp_out,chinese_y,math_y,english_y,physical_y,chemistry_y,str(temp_grid[0,0].index + 1))   
    temp_grid[20,0].observe(show_info_200,names = 'index')

    def show_info_210(change):
        math_y[3] = change['new'] + 1
        drawing(temp_out,chinese_y,math_y,english_y,physical_y,chemistry_y,str(temp_grid[0,0].index + 1))   
    temp_grid[21,0].observe(show_info_210,names = 'index')

    def show_info_220(change):
        english_y[3] = change['new'] + 1
        drawing(temp_out,chinese_y,math_y,english_y,physical_y,chemistry_y,str(temp_grid[0,0].index + 1))   
    temp_grid[22,0].observe(show_info_220,names = 'index')

    def show_info_230(change):
        physical_y[3] = change['new'] + 1
        drawing(temp_out,chinese_y,math_y,english_y,physical_y,chemistry_y,str(temp_grid[0,0].index + 1))   
    temp_grid[23,0].observe(show_info_230,names = 'index')

    def show_info_240(change):
        chemistry_y[3] = change['new'] + 1
        drawing(temp_out,chinese_y,math_y,english_y,physical_y,chemistry_y,str(temp_grid[0,0].index + 1))   
    temp_grid[24,0].observe(show_info_240,names = 'index')

    #--------------------------------------------------#
    

    '''
    for  i in range(25):
        if i not in [1,7,13,19] and temp_grid[i,0].index != 16:
            temp_grid[i,0].observe(show_info,names = 'index')'''
    
    
    return
