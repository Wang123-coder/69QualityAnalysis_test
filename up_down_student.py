import xlrd
import ipywidgets as widgets
from IPython.display import display, Javascript

def upStudent(grid,table,nrows,ncols):

    temp_grid = widgets.GridspecLayout(31,6,width = 'auto',height = 'auto')

    for i in range(1,32):
        alldata = table.row_values(i)
        for j in range(3):
            temp_grid[i - 1,j+1] = widgets.Button(description = str(alldata[j]))
            if i == 1:
                temp_grid[i - 1,j+1].style = {'button_color':'#004080'}
                temp_grid[i - 1,j+1].button_style = 'info'
        temp_grid[i - 1,4] = widgets.Button(description = str(alldata[20]).split('.')[0])
    temp_grid[0,4].style = {'button_color':'#004080'}
    temp_grid[0,4].button_style = 'info'
    
    grid[1:19,0:30].children[0].children[2].children = [temp_grid]

    return

def downStudent(grid,table,nrows,ncols):
    
    temp_grid = widgets.GridspecLayout(31,6,width = 'auto',height = 'auto')

    temp_grid[0,1]  = widgets.Button(style = {'button_color':'#FFC125'},
                                     button_into = 'info',
                                     description = '班级')
    temp_grid[0,2]  = widgets.Button(style = {'button_color':'#FFC125'},
                                     button_into = 'info',
                                     description = '学号')
    temp_grid[0,3]  = widgets.Button(style = {'button_color':'#FFC125'},
                                     button_into = 'info',
                                     description = '姓名')
    temp_grid[0,4]  = widgets.Button(style = {'button_color':'#FFC125'},
                                     button_into = 'info',
                                     description = '年名')
    for i in range(nrows-30,nrows):
        alldata = table.row_values(i)
        for j in range(3):
            temp_grid[i - nrows+31,j+1] = widgets.Button(description = str(alldata[j]))
        temp_grid[i - nrows+31,4] = widgets.Button(description = str(alldata[20]).split('.')[0])
    
    grid[1:19,0:30].children[0].children[3].children = [temp_grid]

    return

def stuUpDown(grid,table,nrows,ncols):

    upStudent(grid,table,nrows,ncols)
    downStudent(grid,table,nrows,ncols)

    return
