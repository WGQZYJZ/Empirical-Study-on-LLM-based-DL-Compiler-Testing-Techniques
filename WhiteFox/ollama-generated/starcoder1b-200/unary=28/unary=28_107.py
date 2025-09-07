
class Model(torch.nn.Module):
    def __init__(self, min_value=-1., max_value=1.):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min_value=min_value)
        v3 = torch.clamp_max(v2, max_value=max_value)
        return v3


# Inputs to the model
inputs  = torch.randn(1, 3, 64, 64)
