
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.nn.functional.conv_transpose2d(x1) # Apply the pointwise transposed convolution to the input tensor
        v2  = torch.nn.functional.sigmoid(v1)        # Apply the sigmoid function to the output of the transposed convolution
        return v2 * v1                                # Multiply the output of the transposed convolution by the output of the sigmoid function


# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(1, 3, 64, 64)
__output__  = m(x)

