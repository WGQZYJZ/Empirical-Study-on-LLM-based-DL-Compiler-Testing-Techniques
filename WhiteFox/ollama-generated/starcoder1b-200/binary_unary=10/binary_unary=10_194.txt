
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 16)
        self.relu = torch.nn.ReLU()
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1) + other
        return self.relu(v1)


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 32)
other = torch.rand(1, 16)
