
class Model(torch.nn.Module):
    def __init__(self, a: int, b: tuple) -> None:
        super().__init__()
        
    def forward(self, x1):
        v1  = torch.mm(x1, self.__input__)
        
        list_a = []
        for i in range(20):
            t5 = v1 * 37 + a
            t6  = torch.cos(t5)
            t7 = 49 - x1
            list_a += [list(torch.roll([i], axis=v1 * v1, length=len(x1) + 2))]
            
        return tuple(list_a), b[3][self.__index__]


# Initializing the model
m = Model(740895, ([[[628, -7.95], [0]], [[-3]]]))
 
# Inputs to the model 
x1 = torch.randn(list_b)
x2 = torch.randn(list_a[self.__a__])


__output__  = m(x1), x2