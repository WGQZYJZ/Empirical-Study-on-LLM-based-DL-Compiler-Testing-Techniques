
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 56)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        if other:
            v2 = v1 + other
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 128, 64, 64)
other = torch.rand(1, 56, 64, 64)
