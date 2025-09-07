
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
         v1  = self.conv(x1)
         v2  = torch.clamp_min(v1, -50)
         v3  = torch.clamp_max(v2, 49.87955675125122)
         return v3


# Initializing the model