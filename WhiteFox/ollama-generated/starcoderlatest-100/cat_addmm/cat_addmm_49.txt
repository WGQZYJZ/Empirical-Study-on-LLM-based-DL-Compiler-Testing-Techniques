
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.addmm(x1, x1.T, x2)
        v2 = torch.cat([v1], dim=0)
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(32, 512, 4, 4)
x2 = torch.randn(512, 16, 4, 4)
