
class Model(torch.nn.Module):
    def __init__(self, other: torch.Tensor):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other
        return v2


# Initializing the model with a constant tensor as input
other = torch.ones(1, 3, 64, 64) * 0.5
m = Model(other=other)
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
