
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.linear = torch.nn.Linear(1024, 3)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x1):
        v1 = self.linear(x1)
        if other is not None:
            v2 = v1 + other 
        else:
            v2 = v1
        v3 = self.relu(v2)
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 1024, 64, 64)
