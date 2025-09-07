
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = (v1 > 0).float() 
        v4  = -0.5 * torch.ones_like(v1)
        v3  = torch.where(v2, v1, v4)
        return v3


# Initializing the model
m = Model()


