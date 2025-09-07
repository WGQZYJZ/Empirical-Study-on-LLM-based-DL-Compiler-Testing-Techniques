
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise transposed convolution to the input tensor
        v2  = torch.relu(v1) # Apply ReLU activation function to the output of the transposed convolution
        return v2


# Initializing the model
m = Model()
 
# Inputs to the model
x1  = torch.randn(1, 8, 64, 64)
__output__  = m(x1)

