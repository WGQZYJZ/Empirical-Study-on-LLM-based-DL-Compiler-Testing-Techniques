
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1) # Apply a linear transformation to the input tensor using functional API
        v2  = v1 + other # Add another tensor "other" (specified by keyword argument 'other')to the output of the linear transformation
 
        return v2

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(10, 5)


# Parameters that should not be accessed:

`other`