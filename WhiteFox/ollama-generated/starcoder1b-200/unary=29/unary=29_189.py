
class Model(torch.nn.Module):
    def __init__(self, min_value=0, max_value=1.):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, kernel_size=2)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v2 + 1e-4 * torch.rand_like(v2)
        return v3


# Initializing the model
m = Model()


