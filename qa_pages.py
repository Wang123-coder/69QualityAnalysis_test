'''
“pages.py”：包含项目的所有界面设计，
                 当部件事件发生时，会被调用以更新界面内容
'''
import ipywidgets as widgets
import qa_initial
import xlrd
import cankaolv
import class_mingci_change
import up_down_student
import junhengdu
import gongxiandu
from IPython.display import display, Javascript

#---------------1.关闭上一个页面，并重新加载，返回新的grid------------#
def close_FrontPage(out,grid):
    grid.close()
    return qa_initial.initGrid(out)

#---------------------------2.目录界面-----------------------#
def firstPage(out,grid):
    grid = close_FrontPage(out,grid)

    with open('./image/leftup.png', 'rb') as f1:
        leftup = f1.read()
        grid[1:5,:4] = widgets.Image(value = leftup)
    f1.close()
    
    with open('./image/rightdown.png', 'rb') as f2:
        rightdown = f2.read()
        grid[15:,25:29] = widgets.Image(value = rightdown)
    f2.close()

    with open('./image/xiaohui.png', 'rb') as f3:
        content = f3.read()
        grid[4:13,9:24] = widgets.Image(value = content)
    f3.close()

    file_upload = widgets.FileUpload(accept='.xlsm',
                                     multiple=False,
                                     layout = widgets.Layout(height = '0.8cm',width = '3cm'),
                                     description = '选择文件')
    enter_button = widgets.Button(description = '确定',
                                  style = {'button_color':'#004080'},
                                  button_style = 'info',
                                  disabled = True,
                                  layout = widgets.Layout(height = '0.8cm',width = '3cm'))
    grid[15:17,10:24] = widgets.HBox([file_upload,
                                     widgets.Label(layout = widgets.Layout(height = '1cm',width = '1cm')),
                                     enter_button],
                                    layout = widgets.Layout(height = 'auto',width = 'auto'))

    #监测选择文件组件的变化
    def file_upload_metadata_change(change):
        if change['new'] != []:                     #已选择文件
            enter_button.disabled = False

    file_upload.observe(file_upload_metadata_change, names='metadata')
    '''
    设置按钮事件:
    '''
    def act_enterButton(b):
        mainPage(out,grid,file_upload.metadata[0]['name'])
    enter_button.on_click(act_enterButton)

    return

#---------------------------3.主界面-----------------------#
def mainPage(out,grid,filename):
    grid = close_FrontPage(out,grid)
    
    filepath = './'+ filename

    data = xlrd.open_workbook(filepath, encoding_override='utf-8')
    table = data.sheets()[0]#选定表
    nrows = table.nrows#获取行号
    ncols = table.ncols#获取列号
    

    # ------------------------------------ #
    grid[0,0:29].description = '质量检测分析'
    grid[19,9:11] = widgets.Dropdown(options=[('目       录', 0)],
                                    layout = widgets.Layout(width = '5cm'),
                                    description='跳转到： ')
    grid[19,17:18] = widgets.Button(description = '进入',
                                    style = {'button_color':'#004080'}, 
                                    button_style = 'info',
                                    layout = widgets.Layout(width = '2.5cm'))
    
    #跳转页面
    def jumpToPage(b):
        value = grid[19,9:11].value
        if value == 0:
            firstPage(out,grid)
    grid[19,17:18].on_click(jumpToPage)
    
    #-------------------------------------#
    class_accordion = widgets.Accordion([widgets.GridspecLayout(10,5,width='auto',height='9.5cm'),
                                         widgets.GridspecLayout(10,5,width='auto',height='9.5cm'),
                                         widgets.GridspecLayout(10,5,width='auto',height='9.5cm'),
                                         widgets.GridspecLayout(10,5,width='auto',height='9.5cm'),
                                         widgets.GridspecLayout(10,5,width='auto',height='9.5cm'),
                                         widgets.GridspecLayout(10,5,width='auto',height='9.5cm')])
    class_accordion.set_title(0, '参与率')
    class_accordion.set_title(1, '名次变化')
    class_accordion.set_title(2, '尖优生名单')
    class_accordion.set_title(3, '学困生名单')
    class_accordion.set_title(4, '尖优生学科均衡度')
    class_accordion.set_title(5, '各科对班级的贡献度')

    subject_accordion = widgets.Accordion([widgets.GridspecLayout(10,5,width='auto',height='9.5cm'),
                                           widgets.GridspecLayout(10,5,width='auto',height='9.5cm'),
                                           widgets.GridspecLayout(10,5,width='auto',height='9.5cm')])
    subject_accordion.set_title(0, '学科名次变化')
    subject_accordion.set_title(1, '学科尖优生变化')
    subject_accordion.set_title(2, '学科学困生变化')
    
    tab = widgets.Tab(children = [class_accordion,subject_accordion])
    tab.set_title(0, '班级评价')
    tab.set_title(1, '学科评价')

    grid[1:19,0:30] = tab

    #-------------班级评价--------------#
    shikao_count = cankaolv.cankaolv(out,grid,table,nrows,ncols)
    class_mingci_change.mingci_change(grid,table,nrows,ncols,shikao_count)
    up_down_student.stuUpDown(grid,table,nrows,ncols)
    junhengdu.jianyousheng(grid,table,nrows)
    gongxiandu.gongxianToClass(grid,table,nrows)
    
    return
