
class Model(torch.nn.Module):
    def __init__(self, min_value=-0.2, max_value=1.8):
        super().__init__()
        self.linear = torch.nn.Linear(4, 8)
 
    def forward(self, x):
        return torch.clamp_min(self.linear(x), min_value)


# Inputs to the model
x = torch.randn(1, 4, 32, 32)
