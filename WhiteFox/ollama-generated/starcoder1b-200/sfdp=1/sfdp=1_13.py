
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x, x_mask=None):
        kx = self.conv(x).mul_(0.5)
        vk = self.conv(x).mul_(0.7071067811865476)
        vk = torch.erf(vk) + 1
        vk = vk * x_mask
        vq = vk * kx
        return vq


# Inputs to the model
x  = torch.randn(1, 3, 64, 64)
