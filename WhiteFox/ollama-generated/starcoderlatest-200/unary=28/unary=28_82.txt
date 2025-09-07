
class Model(torch.nn.Module):
    def __init__(self, min_value: float = -100.0, max_value: float = 100.0):
        super().__init__()
        self.linear = torch.nn.Linear(28*28, 100)
 
    def forward(self, x1):
        v1 = self.linear(x1.view(-1, 784))
        v2 = torch.clamp_min(v1, min_value=min_value)
        v3 = torch.clamp_max(v2, max_value=max_value)
        return v3


# Initializing the model
m = Model()
x1 = torch.randn(1, 1, 28, 28)
