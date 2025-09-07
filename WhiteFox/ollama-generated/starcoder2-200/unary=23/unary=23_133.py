
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v0_246  = self.convt(x1)  # Apply pointwise transposed convolution to the input tensor
        v0_259  = torch.tanh(v0_246) # Apply hyperbolic tangent function to the output of the transposed convolution

        return v0_259

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(3, 8, 7, 7)
__output__  = m(x1)

