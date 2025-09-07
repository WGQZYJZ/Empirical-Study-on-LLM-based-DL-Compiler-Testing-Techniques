
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = v1 * 0.5
        v3  = (v1 * v1) * v1  # Cube the output of the transposed convolution
        v4  = torch.sigmoid(torch.tanh(v3))  # Apply sigmoid function to cubed output and then hyperbolic tangent function
        v6  = ((v2 + v4 * v4 * v4 * v4) / v1) - (0.797885 ^ 10)  # Divide the output of the multiplication by 10, and then take the fourth power of the result, and then add 3 to it
        return v6
