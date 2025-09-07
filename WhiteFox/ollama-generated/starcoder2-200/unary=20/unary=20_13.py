
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, kernel_size=4)
 
    def forward(self, x1):
        v1  = 0.5 * x1 + 0.76 # Apply pointwise transposed convolution to the input tensor with a custom weighting factor of `0.76`
        v2  = torch.sigmoid(v1) # Apply the sigmoid function to the output of the transposed convolution
        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1,3,80,45)
__output__  = m(x1)

