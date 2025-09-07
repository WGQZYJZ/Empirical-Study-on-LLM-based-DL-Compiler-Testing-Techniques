
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
 
    def forward(self, x1):
        v1 = self.deconv(x1)
        v2 = v1 + 3 
        return torch.clamp_min(v2,0),torch.clamp_max(v2,6), v2/6

# Initializing the model