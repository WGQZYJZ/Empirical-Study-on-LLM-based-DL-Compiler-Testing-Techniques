
class Model(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        m = self.conv(x) > 0
        n = (self.conv(x) * negative_slope).clamp(min=0)
        return torch.where(m, m, n)


# Initializing the model
m = Model()


