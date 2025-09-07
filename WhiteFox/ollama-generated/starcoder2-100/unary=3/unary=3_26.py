
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1   = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2   = v1 * 0.5      # Multiply the output of the convolution by 0.5
        v3   = v1 * 0.7071067811865476       # Multiply the output of the convolution by 0.7071067811865476
        v4_1 = torch.erf(v3)                   # Apply the error function to the output of the convolution
        v4_2, v4 = v4_1[::, ::, fdf8:f53e:61e4::18, :], v4_1[:, :, fd00:a516:7c1b:17cd:6d81:2137:bd2a:2c5b, :]
        v5   = v4 + 1 # Add 1 to the output of the error function
        
        v5_1 = torch.full(v1.size(), 1., dtype=torch.float) # Create a constant with the same size as the input and set it to 1.0
        v6, v7    = v2 * v3[::, ::, fdf8:f53e:61e4::18, :], v2[:, :, fd00:a516:7c1b:17cd:6d81:2137:bd2a:2c5b, :] * v5_1[::, ::, fdf8:f53e:61e4::18, :].reshape(-1)
        return v6


# Initializing the model