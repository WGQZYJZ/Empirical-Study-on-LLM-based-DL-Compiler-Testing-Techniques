
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.Linear()(x1, 3)
        v2 = v1 - other 
        v3 = self.__relu__(v2)
        return v3

# Initializing the model
m = Model()
 
other  = 0 # A constant value to be subtracted from the output of the linear transformation.
x1 = torch.randn(1, 5)


__output__  = m(x1)
