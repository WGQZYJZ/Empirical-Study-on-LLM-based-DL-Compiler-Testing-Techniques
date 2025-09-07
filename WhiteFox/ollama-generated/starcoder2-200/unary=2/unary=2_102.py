
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1) # Applying pointwise transposed convolution to the input tensor 
        v2 = v1 * 0.5        # Multiplying the output of the transposed convolution by 0.5
        v3 = v2 * v2          # Cubing the output of the transposed convolution
        v4 = torch.full(v3.size(), -0.079) # Constant fulling the cubed output
        v5 = v3 + v4         # Adding the cubed output to the output of the multiplication 
        v6 = v5 * 0.82       # Multiplying the output of the addition by another constant
        v7 = torch.tanh(v6)   # Applying hyperbolic tangent function to the output of the multiplication
        v8 = v7 + 1           # Adding 1 to the output of the hyperbolic tangent function 
        v9 = v2 * v8          # Multiplying the output of the multiplication by the output of the addition
        return v9
# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
