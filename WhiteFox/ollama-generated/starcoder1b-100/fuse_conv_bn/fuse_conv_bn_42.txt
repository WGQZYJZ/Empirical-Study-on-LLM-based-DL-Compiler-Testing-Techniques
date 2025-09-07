
class Model(torch.nn.Module):
    def __init__(self, in_channels, num_filters, filter_size):
        super().__init__()
        self.conv = torch.nn.Conv2d(...) # X can be 1, 2 or 3 representing the dimension
        self.bn   = torch.nn.BatchNorm2d(...) # X should match with Conv2d

        self.linear  = torch.nn.Linear(in_channels * filter_size ** 2, num_filters)

    def forward(self, x1):
        conv = self.conv(x1)
        bn   = self.bn(conv)
        return self.linear(bn)


# Initializing the model
m = Model(...) # Input must be of the format [n, c, h, w] where c is the number of channels,
    m_fuse = FuseConvBn(m, out_channels=64, in_channels=3) # X can be 1, 2 or 3 representing the dimension
