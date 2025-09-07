
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + 3
        v3 = F.relu6(v2) # Clamp the output of the addition operation at a minimum of 0 and a maximum of 6
        v4 = torch.div(v3, 8)
        return v4


# Initializing the model