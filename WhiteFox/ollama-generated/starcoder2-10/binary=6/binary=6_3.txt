
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 1)
 
    def forward(self, x1):
        v1  = self.linear(x1) - other # Subtract 'other' from the output of the linear transformation
        return v1


# Initializing the model
m = Model()
 

# Inputs to the model: 'v1' and 'v2'. 'v1' is 3-dimensional, and 'v2' has only one element.
x1  = torch.randn(10, 32)
other = x1[:,5] # Subscript to access an array
__output__  = m(x1).sum()

