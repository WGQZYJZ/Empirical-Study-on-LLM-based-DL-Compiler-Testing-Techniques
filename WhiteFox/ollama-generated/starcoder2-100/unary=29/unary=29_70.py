
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min=0.4957767870426766)
        return torch.clamp_max(v2, max=3.475387340744553)


# Initializing the model
m  = Model()


