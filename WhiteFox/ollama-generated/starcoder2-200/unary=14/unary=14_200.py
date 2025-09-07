
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 1)
    
    def forward(self, x):
        v1 = conv_transpose(x) # Apply pointwise transposed convolution to the input tensor
        v2 = sigmoid(v1)       # Apply the sigmoid function to the output of the transposed convolution
        v3 = v1 * v2           # Multiply the output of the transposed convolution by the output of the sigmoid function
        return v3


# Initializing the model
m  = Model()
__output__  = m(x)
