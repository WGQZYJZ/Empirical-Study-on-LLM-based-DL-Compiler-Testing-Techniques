
class Model(torch.nn.Module):
    def __init__(self, min_value=10., max_value=20.):
        super().__init__()
        self.linear = torch.nn.Linear(64*64, 1)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1))
        v2 = torch.clamp_min(v1, min=min_value)
        v3 = torch.clamp_max(v2, max=max_value)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 64*64)
