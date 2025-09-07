
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1) # Apply a linear transformation to the input tensor
        v2 = torch.sigmoid(v1)  # Apply the sigmoid function to the output of the linear transformation
        v3 = v1 * v2
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 500)

__output__  = m(x1)

