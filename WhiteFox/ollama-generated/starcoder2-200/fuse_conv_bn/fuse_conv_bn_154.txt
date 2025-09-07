
class ConvBN(torch.nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size, padding=0):
        super().__init__()

        self.conv = torch.nn.Conv2d(in_channels, out_channels,
                                    kernel_size, bias=False)
        self.bn   = torch.nn.BatchNorm2d(out_channels)

    def forward(self, x1):
       return torch.nn.functional.batch_norm(
            conv=torch.nn.functional.conv2d(x1), 
            weight=self.conv.weight, bias=self.conv.bias, running_mean=self.bn.running_mean)


m  = ConvBN(3, 8, (7,5))
x1 = torch.randn(10, 3, 240, 640).cuda() # GPU is recommended!
__output__  = m(x1)


