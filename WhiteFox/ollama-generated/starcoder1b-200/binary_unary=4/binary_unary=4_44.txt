
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)
        self.relu   = torch.nn.ReLU()
 
    def forward(self, x1, other=None):
        v1  = self.linear(x1)
        if not isinstance(other, type(None)):
            v2 = v1 + other
        else:
            v2 = None
        v3 = self.relu(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 5, 40, 40)
other = torch.randn(1, 5)
