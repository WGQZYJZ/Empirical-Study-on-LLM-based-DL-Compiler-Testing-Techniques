
class Model(torch.nn.Module):
    def __init__(self, min_value=-5.0, max_value=5.0):
        super().__init__()
        self.linear = torch.nn.Linear(32*4*4, 16)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1, 32*4*4))
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3


# Inputs to the model
min_value = -5.0
max_value = 5.0
x1 = torch.randn(1, 32*4*4)
