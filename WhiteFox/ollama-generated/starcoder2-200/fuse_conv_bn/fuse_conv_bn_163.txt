
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, kernel_size=(1, 1))
        self.bn = torch.nn.BatchNorm2d(8)

    def forward(self, x):
        x = self.conv(x)
        return self.bn(x)


m = Model()

x = torch.randn(4, 3, 5, 6) # shape of the input tensor can be (N, 3, H, W), where N is the batch size, 3 represents the number of channels in the input data, and H and W are height and width respectively.

x1 = m(x)
