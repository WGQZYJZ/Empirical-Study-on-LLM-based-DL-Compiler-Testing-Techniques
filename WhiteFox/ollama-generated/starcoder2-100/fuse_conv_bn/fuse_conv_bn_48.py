class Model(torch.nn.Module):
    def __init__(self, channels):
        super().__init__()
        self.conv = torch.nn.Conv2d(channels, 30, kernel_size=1)

    def forward(self, x1):
        v1  = self.conv(x1) 
        v2 = torch.nn.functional.batchnorm(v1)
        return v2


m = Model()
x1 = torch.randn(4, 65, 38) # Input tensor shape is (N x 65 X C)

