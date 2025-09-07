
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1, min_value=1e-4, max_value=0.999):
        v1 = self.conv(x1)
        v2 = v1 - min_value
        v3 = torch.clamp(v2, max_value, None) + min_value
        return v3
