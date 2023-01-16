import settings

win_height = 800
win_width = 800

pipe_w = 100
pipe_h = 60

list_pipe_matrix = [
    "00000000000",
    "20000000000",
    "12100000000",
    "12100000000",
    "20000000000",
    "20000000000",
    "20000000000",
    "12210000000",
    "00020000000", 
    "00012100000",
    "00000200000",
    "00000110000",
    "00122210000",
    "00000000000"
]

dict_right_directions= {
    "0": 2,
    "1": 2
                    }

    
list_pipes = []
list_rect_pipe = []
class Pipes(settings.Settings):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.DIRECTION = 1

def create_world(level):
    list_pipes = []
    list_rect_pipe = []
    x = 0
    y = 0
    for string in level:
        for el in string:
            if el == "1":
                pipe = Pipes(
                    x= x,
                    y= y,
                    width= pipe_w,
                    height= pipe_h,
                    color= (255, 165, 0),
                    name_image= ("game2/images/pipes/pipe1.png")
                )
                list_pipes.append(pipe)
                list_rect_pipe.append(pipe)
            if el == "2":
                pipe = Pipes(
                    x= x,
                    y= y,
                    width= pipe_w,
                    height= pipe_h,
                    color= (255, 165, 0),
                    name_image= ("game2/images/pipes/pipe2.png")
                )
                list_pipes.append(pipe)
                list_rect_pipe.append(pipe)
            if el == "3":
                pipe = Pipes(
                    x= x,
                    y= y,
                    width= pipe_w,
                    height= pipe_h,
                    color= (255, 165, 0),
                    name_image= ("game2/images/pipes/pipe3.png")
                )
                list_pipes.append(pipe)
                list_rect_pipe.append(pipe)
            x += pipe_w
        x = 0
        y += pipe_h
    return list_pipes, list_rect_pipe