
class Model(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.clamp_min(v1, min=0.5)
        return torch.clamp_max(v2, max=1)


m = Model()
__output__  = m(torch.randn(1, 3, 64, 64))

