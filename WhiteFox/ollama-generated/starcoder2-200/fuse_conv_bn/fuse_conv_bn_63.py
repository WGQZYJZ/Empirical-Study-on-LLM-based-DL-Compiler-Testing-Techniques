class Model(torch.nn.Module):
    def __init__(self, channel=32):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(channel, 64, kernel_size=(7,7), stride=[0,3], padding=[3,3])

    def forward(self, x1):
        v1 = torch.nn.functional.pad(x1,(3,3,3,3))
        v2 = self.conv1(v1)
        return v2
