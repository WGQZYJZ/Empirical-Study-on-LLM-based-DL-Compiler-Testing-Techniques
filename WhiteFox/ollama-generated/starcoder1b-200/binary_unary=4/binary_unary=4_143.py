
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.linear = torch.nn.Linear(1, 2, bias=False)
 
    def forward(self, x):
        v1 = self.linear(x) + other
        v2 = relu(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 1)
other = torch.randn(1, 3)
