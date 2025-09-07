
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1, t2, ...):
        v  = torch.cat([t1, t2, ...], dim=0)
        v  = v.view(...)
        v  = torch.relu(v)
        return v

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 3)
x2 = torch.randn(1, 4, 6)
