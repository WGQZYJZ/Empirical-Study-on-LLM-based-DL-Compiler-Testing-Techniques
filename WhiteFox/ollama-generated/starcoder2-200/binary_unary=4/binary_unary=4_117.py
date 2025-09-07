
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.nn.functional.linear(x1) # Apply a linear transformation to the input tensor
        v2  = v1 + other                        # Add another tensor to the output of the linear transformation
        v3  = torch.nn.functional.relu(v2)     # Apply the ReLU activation function to the result
        return v3


# Initializing the model with `other` as 0
m = Model(other=None)

# Inputs to the model without `other` keyword argument
x1  = torch.randn(1, 256*8*8)
