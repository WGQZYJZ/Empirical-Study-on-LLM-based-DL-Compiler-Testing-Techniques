The 'other' could be a tensor of the same shape as the output of the convolution or a scalar.


# Model
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        other = torch.randn(1, 3, 64, 64).view(-1)
        return v1 - other
