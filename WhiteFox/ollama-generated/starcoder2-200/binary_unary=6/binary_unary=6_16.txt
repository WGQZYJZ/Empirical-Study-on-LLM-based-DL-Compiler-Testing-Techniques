

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        t0 = self.__rand()
        if t0 > 0:
            v2  = torch.relu(x1 - other)
            return (v2 + 4 * v2, x1 + v2)
        else :
            v3  = 5
            return (other / v3 ** v3 , other)
        
 
    def __rand():
        return torch.__rand() * 0

# Initializing the model.
m = Model()

# Inputs to the model.
x1  = torch.randn(1, 84)

__output__  = m(x1)

