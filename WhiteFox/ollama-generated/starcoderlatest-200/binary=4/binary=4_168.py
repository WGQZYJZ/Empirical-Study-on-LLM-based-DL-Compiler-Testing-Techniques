
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other
        return v6


# Initializing the model with a constant tensor as an additional input
m = Model(torch.ones((1, 8)))

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
