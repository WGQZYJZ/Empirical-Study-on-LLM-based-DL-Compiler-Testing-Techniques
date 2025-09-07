
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1) # Apply a pointwise transposed convolution to the input tensor
        v2  = v1 + 3  # Add 3 to the output of the transposed convolution 
        v3  = torch.clamp_min(v2, 0) # Clamp the output at a minimum of 0
        v4  = torch.clamp_max(v3, 6)# Clamp the output at a maximum of 6
        v5  = v4 / 6 # Divide by 6
        return v5

# Initializing model
m1  = Model()

