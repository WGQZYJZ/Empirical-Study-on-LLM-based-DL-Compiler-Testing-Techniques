
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1, other):
        v1 = self.linear(x1) - other
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3)
other = 0.5  # Please refer to https://docs.python.org/3/library/functions.html#float
