
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        s0  = torch.split(x1, [32, 64], dim=0)
        c0  = torch.cat([s0[i] for i in range(len(s0))], dim=0)
        return c0


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(2, 3, 64, 64)
