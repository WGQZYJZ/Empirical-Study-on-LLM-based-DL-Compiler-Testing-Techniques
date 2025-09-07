
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2 = t.clamp_min(v1, minValue = -5) # Clamp the output of the transposed convolution to a minimum value with -5 as the minimum value
        v3 = t.clamp_max(v2, maxValue=40)# Clamp the output of the previous operation to a maximum value with 40 as the maximum value
        return v3
# Initializing the model