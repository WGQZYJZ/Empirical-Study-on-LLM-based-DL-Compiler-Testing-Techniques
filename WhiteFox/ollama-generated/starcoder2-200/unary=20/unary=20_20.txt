
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(32, 8, 1)
 
    def forward(self, x1):
        v0 = self.conv(x1)
        v1  = torch.sigmoid(v0) 
        return v1


# Initializing the model