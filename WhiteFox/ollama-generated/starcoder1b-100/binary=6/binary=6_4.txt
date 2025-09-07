
class Model(torch.nn.Module):
    def __init__(self, other=10):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x):
        v = self.linear(x)
        return v - other


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3)
