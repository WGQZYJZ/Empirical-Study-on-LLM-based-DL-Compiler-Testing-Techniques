
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.conv_transpose2d(x1) # Apply pointwise transposed convolution to the input tensor
        v2  = torch.sigmoid(v1)  # Apply the sigmoid function to the output of the transposed convolution
        return v2

# Initializing the model
m  = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

