
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.deconv(x1)
        v2 = v1 * 0.5
        v3 = v1 * v1 * v1 # Cube the output of the transposed convolution
        v4 = v3 * 0.044715 # Multiply the cubed output by 0.044715
        v5 = v2 + v4 # Add the output of the transposed convolution to the output of the multiplication
        v6 = v5 * 0.7978845608028654 # Multiply the output of the addition by 0.7978845608028654
        v7 = torch.tanh(v6) 
        v8 = v7 + 1 # Add 1 to the output of the hyperbolic tangent function
        v9 = v2 * v8 # Multiply the output of the multiplication by the output of the addition
        return v9
