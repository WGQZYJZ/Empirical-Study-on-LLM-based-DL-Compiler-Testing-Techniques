
class ConvBnModel(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv = torch.nn.Conv2d(3, 64, kernel_size=7)
        bn  = torch.nn.BatchNorm2d(64)
        v1  = conv(x1) # 3*7*7
        v1bnv  = bn(v1) 
        return v1bnv

m  = ConvBnModel()
m1  = m(torch.randn(2, 3, 7, 7))

