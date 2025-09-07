
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, kernel_size=1)
        self.conv2 = torch.nn.Conv2d(3, 8, kernel_size=1)

    def forward(self, x):
        conv1 = self.conv1(x).relu()
        conv2 = self.conv2(x).relu()
        add   = conv1 + conv2
        return add

m = Model()

x = torch.randn(1, 3, 64, 64)
