
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        s1 = torch.split(x1, [8, 4, 2], dim=1)
        c = torch.cat([s1[i] for i in range(len(s1))])
        return c

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(3, 8, 64, 64)
