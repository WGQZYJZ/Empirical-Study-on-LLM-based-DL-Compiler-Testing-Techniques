
class Model(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        self.linear = torch.nn.Linear(**kwargs)

    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = torch.clamp_min(v1, -64.) # Here `torch` and `64.` are provided as keyword arguments.
        v3  = torch.clamp_max(v2, 89.) 
        return v3

# Initializing the model
m = Model(in_features=300, out_features=15)

# Inputs to the model
x1 = torch.randn(10, 300)
