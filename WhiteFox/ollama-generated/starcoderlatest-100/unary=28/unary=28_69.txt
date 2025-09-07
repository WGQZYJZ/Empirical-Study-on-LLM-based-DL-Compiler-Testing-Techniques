
class Model(torch.nn.Module):
    def __init__(self, min_value=-10, max_value=10):
        super().__init__()
        self.linear = torch.nn.Linear(8, 4)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3


# Initializing the model
m = Model(min_value=-50, max_value=50)
x1 = torch.randn(1, 8)
