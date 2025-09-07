
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1.clamp_min(-50.) # Applying the clamp function to the previous tensor
        v3  = v2.clamp_max(+50.) # Applying another clamp function with a minimum and maximum value of +50. and -50., respectively, to the previous tensor 
        return v1
 
