
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(784, 10)

    def forward(self, x):
        v1  = self.linear(x)
        v2  = v1 + other
        v3  = F.relu(v2) 
        return v3

# Initializing the model
m = Model()
other = torch.randn(10,) # randomly initialized tensor with shape [784, 1] or [1, 784].

# Inputs to the model
x = torch.randn(64, 784)
