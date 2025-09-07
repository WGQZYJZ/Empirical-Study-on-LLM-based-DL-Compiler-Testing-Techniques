
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other
        return v2


# Initializing the model
m = Model()

# Inputs to the model
other = torch.randn(1, 3) * 0.5 # Multiply the output of a linear transformation by a constant '0.5'
x1 = torch.randn(1, 3, 64, 64)
