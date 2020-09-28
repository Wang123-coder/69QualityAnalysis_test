'''
“main.py”：作为整个项目的主程序入口
'''
import ipywidgets as widgets
from IPython.display import display
import qa_initial
import qa_pages

main_out = widgets.Output(layout={'border': '1px solid black'})
init_grid = qa_initial.initGrid(main_out)

display(main_out)

qa_pages.firstPage(main_out,init_grid)     #直接显示目录界面
