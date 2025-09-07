
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.transv = torch.nn.ConvTranspose2d(8, 3, 4, stride=1, padding=0)

    def forward(self, x):
        v1 = self.conv(x) # Apply pointwise convolution with kernel size 1 to the input tensor
        v2 = v1 + 3 # Add 3 to the output of the convolution
        v3 = torch.clamp(v2, min=0) # Clamp the output of the addition operation to a minimum of 0
        v4 = torch.clamp(v3, max=6) # Clamp the output of the previous clamp operation to a maximum of 6
        v5 = v1 * v4 # Multiply the output of the convolution by the output of the clamp operation
        v6 = self.transv(x2) / 6 
        return v1


# Initializing the model