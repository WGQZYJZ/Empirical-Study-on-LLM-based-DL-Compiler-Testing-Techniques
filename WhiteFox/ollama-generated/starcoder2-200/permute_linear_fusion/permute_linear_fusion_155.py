
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = x1.permute(0, 2, 1) # permute(x, dim0, dim1), swap the 3rd and 4th dimensions of a 5D tensor.
        v2  = torch.nn.functional.linear(v1, self.linear.weight, self.linear.bias)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 5, 3, 4) # Generate an input tensor with more than 2 dimensions for demonstration purpose.
