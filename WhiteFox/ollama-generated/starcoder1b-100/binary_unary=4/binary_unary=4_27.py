
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.linear = torch.nn.Linear(4, 1)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x):
        v = self.linear(x)
        v = self.relu(v)
        return v + other


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 4)
