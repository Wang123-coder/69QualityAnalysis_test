import xlrd
import ipywidgets as widgets
from IPython.display import display, Javascript
import matplotlib
import matplotlib.pyplot as plt

def drawing(temp_out,x,chinese_y,math_y,english_y,physical_y,chemistry_y,class_num):

    temp_out.clear_output()

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
    temp_grid[25,0] = widgets.Button(description = '确定当前数据内容')

    
    grid[1:19,0:30].children[0].children[5].children = [widgets.HBox([temp_grid,temp_out])]

    

    with temp_out:
        print('请先在左侧进行选择！')

    def button_click(b):
        chinese_y = []
        math_y = []
        english_y = []
        physical_y = []
        chemistry_y = []
        x = []
        count = 0
        
        if temp_grid[0,0].value == '' or temp_grid[2,0].value == '' or temp_grid[3,0].value == '' or temp_grid[4,0].value == '' or temp_grid[5,0].value == '' or temp_grid[6,0].value == '':
            temp_out.clear_output()
            with temp_out:
                print('班级与第一次考试排名不能为空！')
        else:
            for i in [2,8,14,20]:
                if temp_grid[i,0].index < 16:
                    count = count + 1
                    chinese_y = chinese_y + [temp_grid[i,0].index + 1]
            for i in [3,9,15,21]:
                if temp_grid[i,0].index < 16:
                    math_y = math_y + [temp_grid[i,0].index + 1]
            for i in [4,10,16,22]:
                if temp_grid[i,0].index < 16:
                    english_y = english_y + [temp_grid[i,0].index + 1]
            for i in [5,11,17,23]:
                if temp_grid[i,0].index < 16:
                    physical_y = physical_y + [temp_grid[i,0].index + 1]
            for i in [6,12,18,24]:
                if temp_grid[i,0].index < 16:
                    chemistry_y = chemistry_y + [temp_grid[i,0].index + 1]
            print(chinese_y)
            for i in range(count):
                x = x + [str(i + 1)]
            drawing(temp_out,x,chinese_y,math_y,english_y,physical_y,chemistry_y,str(temp_grid[0,0].index + 1))
        
    temp_grid[25,0].on_click(button_click)
    
    return
