
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(5, 3)
 
    def forward(self, x1):
        v2 = other
        v1  = self.linear(x1) 
        return (v1 + v2), v2


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(5,)
other = torch.randn(3, ) 

__output__, __out_var__ = m(x1) 

