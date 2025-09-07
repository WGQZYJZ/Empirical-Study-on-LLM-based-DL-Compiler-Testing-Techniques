
class Model(torch.nn.Module):
    def __init__(self, other: torch.Tensor = None):
        super().__init__()
        if other is not None:
            self.linear = torch.nn.Linear(32, 64)
        else:
            self.linear = torch.nn.Linear(32, 64, bias=False)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        if other is not None:
            v2 = v1 + other
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 32, 64)
other_tensor = torch.randn(1, 64, 8, requires_grad=True)
