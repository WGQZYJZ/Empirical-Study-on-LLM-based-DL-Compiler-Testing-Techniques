
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1.clamp_min(-1000) # Clamp the output of the transposed convolution to a minimum value -1000 in this case
        v3  = v2.clamp_max(1000) # Clamp the output of the previous operation to a maximum value 1000 in this case
        return v3
