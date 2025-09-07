
class Model(torch.nn.Module):
    def __init__(self, min_value=-1, max_value=1):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 64 * 3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1, 64*64*3))
        v2 = torch.clamp_min(v1, min=min_value)
        v3 = torch.clamp_max(v2, max=max_value)
        return v3


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
m = Model(min_value=-0.5, max_value=1.5)
