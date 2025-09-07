
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 3)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = v1 - other # Subtract 'other' from the output of the linear transformation
        return v2

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(64, 3)
other = x1[:, [0]] + x1[:, [1]] + x1[:, [2]] + x1[:, [7]] # Generate an array of 64 scalars by adding a particular set of 4 columns of the input tensor to each other column in that specific order
__output__  = m(x1)

