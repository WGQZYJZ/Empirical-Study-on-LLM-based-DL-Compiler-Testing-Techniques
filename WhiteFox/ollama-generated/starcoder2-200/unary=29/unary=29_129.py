
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.deconv(x1) # Apply pointwise transposed convolution to the input tensor
        v2 = torch.clamp_min(v1, min_value=-8.035794)  # Clamp the output of the transposed convolution to a minimum value (-8.035794 in this case)
        v3 = torch.clamp_max(v2, max_value=6.457153)  # Clamp the output of the previous operation to a maximum value (6.457153 in this case)
        return v3


# Initializing the model