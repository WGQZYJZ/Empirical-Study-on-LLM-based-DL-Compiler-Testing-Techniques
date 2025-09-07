
class Model(torch.nn.Module):
    def __init__(self, maxv = 32., minv = -10.) :
        super().__init__()
        self.transposeconv= torch.nn.ConvTranspose2d(in_channels=8, out_channels=4)

    def forward(self,x):
        v1 = self.transposeconv(x1)
        v3  = torch.clamp_max(v2, max_value)
