
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1, t2, ..., tN):
        v  = torch.cat([t1, t2, ...], dim=...)
        v  = v.view(...)
        v  = torch.relu(v)

# Initializing the model
m = Model()

# Inputs to the model
t1 = torch.randn(1, 3, 2)
t2 = torch.randn(1, 3, 2)
...
tN = torch.randn(1, 3, 2)
