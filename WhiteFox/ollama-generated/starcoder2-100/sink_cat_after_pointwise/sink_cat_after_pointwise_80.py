
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 3, 3)

    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.cat([v1, torch.zeros_like(v1)], dim=0) 
        v3  = v2[..., ::-1] # Flipped along the channel dimension of v2 (for demonstration purpose)
        return v3

# Initializing the model