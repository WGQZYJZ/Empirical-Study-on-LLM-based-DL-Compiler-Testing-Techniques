
class Model(torch.nn.Module):
    def __init__(self, min_value=1., max_value=3.):
        super().__init__()
        self.linear = torch.nn.Linear(5, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 * torch.clamp_min(torch.ones_like(v1), min_value)
        v3 = v2 * torch.clamp_max(torch.ones_like(v2), max_value)
        return v3


# Initializing the model
m = Model(min_value=1., max_value=3.)
