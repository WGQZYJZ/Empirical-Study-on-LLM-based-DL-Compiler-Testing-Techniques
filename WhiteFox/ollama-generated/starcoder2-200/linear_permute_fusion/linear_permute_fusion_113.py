
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.nn.functional.linear(x1)  # Apply linear transformation to the input tensor.
        v2 = v1.permute(-3, -2, -4, -1)    # Permute the output tensor from the linear transformation.
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(50, 60, 70) 

__output__  = m(x1)

# Expected output
[Tensor of size (50, 48, 2)]
