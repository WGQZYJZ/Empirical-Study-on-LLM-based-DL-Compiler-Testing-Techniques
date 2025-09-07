

class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.5, channel1=32, channel2=64):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(
            in_channels=channel1, 
            out_channels=channel2, 
            kernel_size=(3, 3), 
            stride=(2, 2),
            padding=(1, 1)
        )
        self.conv2 = torch.nn.Conv2d(in_channels=8, out_channels=5, kernel_size=7)

    def forward(self, x): 
        v1 = self.conv(x) # Apply pointwise transposed convolution to the input tensor
        v2 = (v1 > 0).float() # Create a mask where each element is True if the corresponding element in v1 is greater than 0, False otherwise
        v3 = negative_slope * torch.abs(v1) # Multiply the output of the transposed convolution by the negative slope
        v4 = v2.type_as(x) * x + (1 - v2).type_as(x) * v3 # Apply the where function to select elements from x or t3 based on the mask t2

        return self.conv2(v4)


# Initializing model
m = Model()

# Input to the model
__input__ = torch.randn(1, 8, 64, 64)

# Output of the model
