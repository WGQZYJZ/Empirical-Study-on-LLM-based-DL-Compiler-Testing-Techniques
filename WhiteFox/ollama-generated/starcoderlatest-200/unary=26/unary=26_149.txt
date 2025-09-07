
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv1 = torch.nn.ConvTranspose2d(3, 8, 4, stride=16, padding=0) # output_size = (input - (kernel-1)/stride + 2*padding)/stride + 1
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=1, padding=1)

    def forward(self, x):
        v1 = self.conv1(x)
        v2 = v1 > 0
        v3 = v1 * negative_slope
        v4 = torch.where(v2, v1, v3)
        