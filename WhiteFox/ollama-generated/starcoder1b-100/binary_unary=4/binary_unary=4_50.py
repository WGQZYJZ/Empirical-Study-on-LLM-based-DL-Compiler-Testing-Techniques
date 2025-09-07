
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(100, 50)
        self.relu   = torch.nn.ReLU()
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 + other
        v3 = self.relu(v2)
        return v3


# Initializing the model
m = Model(torch.randn(100, 10))


