
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, x2=None):
        v1 = torch.mm(x1,y1)
        v3  = [v1] * 50
        v4 = torch.cat([v for v in v3], -1)
        return v4

# Initializing the model
m  = Model()

 # Inputs to the model