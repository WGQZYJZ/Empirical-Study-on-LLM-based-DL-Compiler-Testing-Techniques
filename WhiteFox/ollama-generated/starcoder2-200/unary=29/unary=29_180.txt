
class Model(torch.nn.Module):
    def __init__(self, max_value=10., min_value=-5.):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, kernel_size=(1, 1), stride=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * min_value / max_value
        v3  = torch.clamp_max(v2, max_value) + (torch.ones(size=v2.shape) - torch.erf(v3))
        return v3


# Initializing the model