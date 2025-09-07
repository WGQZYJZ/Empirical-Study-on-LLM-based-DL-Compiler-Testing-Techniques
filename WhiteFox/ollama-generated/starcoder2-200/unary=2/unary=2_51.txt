
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1)

    def forward(self, x1):
        v1 = self.conv(x1) # Transposed convolution
        v2 = v1 * 0.5   # Multiplication by constant 0.5
        v3 = v1 ** 3    # Cube of the output of transposed convolution 
        v4 = v3 * 0.044715   # Multiplication by constant 0.044715
        v5 = v1 + v4     # Addition with the cube of the output of transposed convolution 
        v6 = v5 * 0.7978845608028654    # Multiplication by constant 0.7978845608028654
        v7 = torch.tanh(v6)   # Hyperbolic tangent function 
        v8 = v7 + 1        # Addition with the hyperbolic tangent of the output of multiplication
        v9 = v2 * v8     # Multiplication by the addition with constant 0.5
        return v9
