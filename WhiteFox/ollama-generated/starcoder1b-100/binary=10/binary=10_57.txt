
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(4, 2)
 
    def forward(self, x1, other):
        v1 = self.linear(x1)
        return v2 + other


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 5)
other = torch.randn(4)
