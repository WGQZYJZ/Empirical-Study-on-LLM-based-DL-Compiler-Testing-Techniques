
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.split(x1, 64, dim=0) 
        return [i for i in range(len(v1))]


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(257, 3, 8, 8)
 
 