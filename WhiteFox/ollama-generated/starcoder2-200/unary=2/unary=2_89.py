class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, kernel_size=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise transposed convolution to the input tensor
        v2  = v1 * 0.5
        v3  = v1 * v1
        v4  = torch.tensor([0.044715])
        v6  = v3 * v4
        v8  = v6 + v2 # Add the output of the transposed convolution to the output of the multiplication 
        v9  = torch.tensor([0.7978845608028654])
        v10 = self.conv(v1) 
        v11 = v1 * v10 # Cube the output of the transposed convolution 
        v13 = v11 + 1 
        v14 = torch.tanh(v9 * v13) # Apply the hyperbolic tangent function to the output of the multiplication
        return v8
