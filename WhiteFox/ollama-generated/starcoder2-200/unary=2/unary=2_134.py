

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convTranspose = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v1  = self.convTranspose(x1) # Apply pointwise transposed convolution to the input tensor 
        v2  = v1 * 0.5   # Multiply the output of the transposed convolution by 0.5
        v3  = v1*v1*v1      # Cube the output of the transposed convolution
        v4  = v3 * 0.044715     # Multiply the cubed output by 0.044715
        v5  = v2 + v4         # Add the output of the transposed convolution to the output of the multiplication
        v6  = v5*0.7978845608028654   # Multiply the output of the addition by 0.7978845608028654 
        v7  = torch.tanh(v6)      # Apply the hyperbolic tangent function to the output of the multiplication
        v8  = v7 + 1        # Add 1 to the output of the hyperbolic tangent function
        v9  = v2 * v8       # Multiply the output of the multiplication by the output of the addition 
        return v9

# Initializing the model
m = Model()
# Input for the model
x1 = torch.randn(4, 3, 64, 64)
