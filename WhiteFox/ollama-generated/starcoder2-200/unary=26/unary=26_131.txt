
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.5):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, kernel_size=(17, 19), stride=4)
 
        self.mask = negative_slope >= 0
        self.mask &= negative_slope < 1
    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.where(v1 > 0, 0 * x + 1, -self.negative_slope + 1)
