
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2  = v1 * 0.5      # Multiply the output of the convolution by 0.5
        v3  = v1  + 3       # Add 3 to the output of the convolution 
        v4  = torch.clamp(v3, min=0, max=6)  # Clamp the output between 0 and 6
        v5  = v2 * v4    # Multiply the output of the convolution by the clamped output
        v6  = v5 / 6      # Divide the output of the multiplication by 6
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
