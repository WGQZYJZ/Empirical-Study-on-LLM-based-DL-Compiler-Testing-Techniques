
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        if not isinstance(other, type(None)):
            v2 = v1 + other
        else:
            v2 = v1
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(256, 32, 64, 64)
