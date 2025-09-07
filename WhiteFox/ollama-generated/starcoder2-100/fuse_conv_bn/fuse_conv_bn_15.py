class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        conv = torch.nn.Conv2d(3, 64, kernel_size=7)
        conv = torch.nn.Conv2d(3, 50, kernel_size=9)

        # Before optimization:
        v1  = conv(x1)
        v2  = torch.nn.functional.batch_norm(v1)

        # After optimization:
        v2  = torch.nn.functional.fuse_conv_bn(
            v1, torch.nn.Conv2d(3, 50, kernel_size=9), torch.nn.BatchNorm2d(50))

        return v2
