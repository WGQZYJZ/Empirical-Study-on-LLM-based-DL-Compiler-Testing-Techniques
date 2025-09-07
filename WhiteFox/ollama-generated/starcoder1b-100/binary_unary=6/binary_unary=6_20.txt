
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(64*64, 10)
 
    def forward(self, x):
        v1 = torch.zeros_like(x)
        v2 = self.linear(x) - 1
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 64*64)
