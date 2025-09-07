
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.nn.functional.conv2d(x1) # Apply the convolution with kernel size 1 to the input tensor
        v3  = torch.sigmoid(v1) 
        v4  = v1 * v3   # multiply the output of the convolution by the output of the sigmoid function
        return v4

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 56, 82)
__output__  = m(x1)

