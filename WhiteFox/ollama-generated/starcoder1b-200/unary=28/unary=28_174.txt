
class Model(torch.nn.Module):
    def __init__(self, min_value=1e-30, max_value=1e+30):
        super().__init__()
        self.linear  = torch.nn.Linear(8, 4)
 
    def forward(self, x):
        v = self.linear(x)
        return torch.clamp_min(v, min_value), torch.clamp_max(v, max_value)


# Inputs to the model
x1 = torch.randn(1, 8)
