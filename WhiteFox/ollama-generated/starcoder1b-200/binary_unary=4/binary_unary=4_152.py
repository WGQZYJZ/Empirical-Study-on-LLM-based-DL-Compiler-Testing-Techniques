
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(20, 3)
 
    def forward(self, x1, other=None):
        v1 = self.linear(x1)
        v2 = v1 + other
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 20)
other = torch.randn(1, 20)
