
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, z1, u2, v3):
        v1  = torch.mm(x1,y1)
        v2  = torch.mm(z1,u2) 
        v3  = v1 + v2
        return v3

# Initializing the model
m = Model()

