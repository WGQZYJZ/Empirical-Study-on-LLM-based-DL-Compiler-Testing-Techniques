
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x1):
         v1 = self.conv(x1)
         v2 = torch.clamp_min(v1, min_value=0.95)
         v3 = torch.clamp_max(v2, max_value=-2.78)
         return v3


m  = Model()
__output__  = m(x1)


