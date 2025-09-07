
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + 3 
        v3 = F.clamp(v2, min=0) # Clamp to a minimum of `0`
        v4 = F.clamp(v3, max=6) # Clamp the clamped tensor to a maximum of 6
        v5 = v1 * v4 # Multiply by clamp
        v6 = v5 / 6 
        return v6
