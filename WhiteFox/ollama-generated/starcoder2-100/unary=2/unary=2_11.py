
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = v1 * 0.5
        v3  = v1 ** 3 # Cube the transposed convolution output
        v4  = v3 * 0.044715 # Multiply by 0.044715 
        v5  = v1 + v4 # Add the transposed convolution output to the multiplication
        v6  = v5 * 0.7978845608028654 # multiply by another constant of 0.7978845608028654 
        v7  = torch.tanh(v6) # Apply the hyperbolic tangent function to the multiplication
        v8  = v7 + 1 
        v9  = v2 * v8 # Multiply by another constant of 0.7978845608028654 
        return v9


# Initializing and feeding the input tensor
m  = Model()
x1 = torch.randn(1, 3, 64, 64) # Random 1-channel tensor with shape of (batch size, channel size, height, width)
__output__  = m(x1)

