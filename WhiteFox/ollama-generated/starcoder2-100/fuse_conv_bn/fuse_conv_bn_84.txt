
class ConvBNModel(torch.nn.Module):
    def __init__(self, conv1d: bool = True) -> None:
        super().__init__()

        self.conv2d  = torch.nn.Conv2d(3, 3, kernel_size=1, padding=(0, 0)) if not conv1d else torch.nn.Conv1d(3, 3, kernel_size=1, padding=0)
        self.bn2d  = torch.nn.BatchNorm2d(3, track_running_stats=True)
        self.conv3d  = torch.nn.Conv3d(3, 3, kernel_size=(1,), stride=(1,)) if not conv1d else torch.nn.Conv1d(3, 3, kernel_size=(1,), stride=(1,))

    def forward(self):
        return self.bn2d(self.conv2d(self.conv3d(torch.randn((3, 3) + (0,) * self.conv3d.kernel_size[1]))) / 4.)

model = ConvBNModel()


inputs = torch.rand(10, 5, 5).cuda()

__outputs__ = model()(inputs) # fuse_conv_bn is enabled by default in torch.compile

