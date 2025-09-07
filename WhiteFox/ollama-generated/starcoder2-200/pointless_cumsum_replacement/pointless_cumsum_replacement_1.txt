
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        t1  = torch.full([x], 1., dtype=dtype) # x1=1.
        t2  = t1.type(dtype) 
        t3  = torch.cumsum(t2, 1).type(dtype)
        return t3

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.zeros([50], dtype=dtype)
