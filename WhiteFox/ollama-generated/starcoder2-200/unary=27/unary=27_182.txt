
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, min=0.5) # Clamp the output of the convolution to a minimum value equal to `0.5`
        v3  = torch.clamp_max(v2, max=-0.7071067811865475) # Clamp the output of the previous operation to a maximum value equal to `-0.7071067811865475`
        return v3


# Initializing model