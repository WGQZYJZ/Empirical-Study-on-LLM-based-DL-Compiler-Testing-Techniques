
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convtranspose = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.convtranspose(x1)
        v2 = torch.clamp_min(v1, min=0.5)
        v3 = torch.clamp_max(v2, max=4.9)
