
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.02):
        super().__init__()
        self.conv1 = torch.nn.ConvTranspose2d(8, 4, kernel_size=2, stride=2)
        self.relu = torch.nn.LeakyReLU()
        self.conv2 = torch.nn.Conv2d(4, 1, kernel_size=1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1 > 0
        v3 = v1 * negative_slope
        v4 = torch.where(v2, v1, v3)
        