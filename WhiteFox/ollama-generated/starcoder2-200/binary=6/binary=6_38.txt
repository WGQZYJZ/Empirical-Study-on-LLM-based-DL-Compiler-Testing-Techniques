
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(25088, 1469)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = v1 - other  # Subtract 'other' from the output of the linear transformation
        return v2

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 40, 40)
__output__  = m(x1)
