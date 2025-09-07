
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y2, z3, zz4):
        v1  = torch.mm(x1,y2)
        v2  = torch.mm(z3,zz4) 
        v3 = v1 + v2
        return v3


# Initializing the model
m = Model()


# Inputs to the model