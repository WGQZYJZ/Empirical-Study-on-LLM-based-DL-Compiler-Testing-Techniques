
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convtranspose = torch.nn.ConvTranspose2d(8, 3, 1, stride=1)
 
    def forward(self, x1):
        v1  = self.convtranspose(x1)
        v2  = v1 * 0.5
        v3  = v1 * v1 * v1 # Cube the output of the transposed convolution
        v4  = v3 * 0.044715 # Multiply the cubed output by 0.044715
        v5  = v1 + v4
        v6  = v5 * 0.7978845608028654 
        v7  = torch.tanh(v6) # Apply the hyperbolic tangent function to the output of the multiplication
        v8  = v7 + 1
        v9  = v2 * v8 
        return v9

