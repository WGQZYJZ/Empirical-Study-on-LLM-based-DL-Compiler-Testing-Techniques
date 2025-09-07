
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 8, bias=True)
 
    def forward(self, x):
        v = self.linear(x).clamp_min(0).clamp_max(6).mul_(6).div_(6)
        return v


# Inputs to the model
x = torch.randn(1, 1, 32, 32)
