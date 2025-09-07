
class Model(torch.nn.Module):
    def __init__(self, num_channels=3):
        super().__init__()
        self.conv = torch.nn.Conv2d(num_channels, 8, 1)
        self.linear = torch.nn.Linear(16 * 7 * 7, 8)
 
    def forward(self, x):
        y = x.view(x.shape[0], -1)
        z = torch.sigmoid(self.conv(y))
        w = x.view(x.shape[0], 1, -1).contiguous().view(x.shape[0], 7, 7) * (z[:, :, None] * 0.5 + 1e-8)
        b = self.linear(w)
        y = torch.addmm(y, z, b)
        return y


# Inputs to the model
x = torch.randn(2, 3, 64, 64)
