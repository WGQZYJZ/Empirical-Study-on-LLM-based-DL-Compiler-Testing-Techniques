
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        v2 = torch.mm(x3, x4)
        v3 = v1 + v2
        return v6


# Initializing the model
m = Model()

 # Inputs to the model 
v1 = torch.randn(659, 870)
v2 = torch.randn(895, 222)
