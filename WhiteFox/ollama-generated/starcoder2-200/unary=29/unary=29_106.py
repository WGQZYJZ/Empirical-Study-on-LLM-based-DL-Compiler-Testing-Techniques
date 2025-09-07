class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.convt(x1)
        v2 = torch.clamp_min(v1, -0.5) # min value provided as keyword argument
        v3 = torch.clamp_max(v2, 84)   # max value provided as keyword argument
        return v3
