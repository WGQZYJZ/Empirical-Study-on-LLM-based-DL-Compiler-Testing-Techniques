
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear()
 
    def forward(self, x1, other=None):  # The argument is defined as `other` with a default value of `None`.
        v1  = self.linear(x1)           # Apply the linear transformation to the input tensor
        if other == None:
            return v1                   # If the argument is not provided (or its value is None), simply pass through it directly 
        else:                           # Otherwise, add another tensor `other` to the output of the linear transformation.
            return v1 + other


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(100)
other=torch.zeros([1]) # A tensor of zeros with the same shape as `v3`

# Resulting values
v2, v4  = m(x1, other), m(x1)

