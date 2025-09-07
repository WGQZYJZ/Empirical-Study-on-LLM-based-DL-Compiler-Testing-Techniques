
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = conv_transpose(x1) # Apply pointwise transposed convolution to the input tensor
        v2 = sigmoid(v1) # Apply the sigmoid function to the output of the transposed convolution
        v3 = v1 * v2 # Multiply the output of the transposed convolution by the output of the sigmoid function
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
