
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(320, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 + other
        return v2


# Initializing the model with an external tensor (specified by the keyword argument "other")
m = Model(torch.randn(64, 8))


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
