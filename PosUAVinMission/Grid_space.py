class Grid_space:
    id = 0

    x_init = 0
    x_end = 0

    y_init = 0
    y_end = 0

    altura = 0
    windSpeed = 0
    #Action
    actions = {}

    r = 10

    # construtor grid
    def __init__(self, id, x_init,x_end,y_init,y_end,actions,r):
        self.id = id
        self.x_init = x_init
        self.x_end = x_end
        self.y_init = y_init
        self.y_end = y_end
        self.actions = actions
        self.r = r
        #self.altura = altura
        #self.windSpeed = windSpeed
