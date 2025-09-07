
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, other=None):
        v1 = torch.nn.Linear()(x1) 
        return v1 + other 
m = Model()


# Initializing the model
x1 = torch.randn(20, 3584)
__output__  = m(x1, None)


# Initializing the model