
class Model(torch.nn.Module):
    def __init__(self, maxv=256, minv=-100):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min=maxv / 4) # Clamp the output of the convolution to a minimum value (default: -inf)
        v3 = torch.clamp_max(v2, max=80) # Clamp the output of the previous operation to a maximum value (default: inf)
        return v3

# Initializing the model with maxv and minv
m = Model()


# Inputs to the model with maxv=-15  minv=-76
x2 = torch.randn(1, 3, 64, 64)  # Creating an input tensor of shape (number_of_batches x number_of_channels x rows x columns) in PyTorch with random values. In this case, we have created a 1 channel, 64x64 image with 8 batches.


__output___ = m(x2)

