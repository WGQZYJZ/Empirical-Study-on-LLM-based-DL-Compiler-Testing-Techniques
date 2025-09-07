
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.split(x1, 64, dim=0)
        v3 = torch.cat([v2[i] for i in range(len(v2))], dim=0)
        return v3


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(8, 3, 64, 64)
