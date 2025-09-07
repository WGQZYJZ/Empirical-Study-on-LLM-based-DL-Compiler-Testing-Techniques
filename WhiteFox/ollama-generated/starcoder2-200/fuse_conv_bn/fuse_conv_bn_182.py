
class ConvBN(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.dim = dim

        self.conv  = torch.nn.ConvXd(32, 64, kernel_size=5)
        self.bn    = torch.nn.BatchNormXd(64)

    def forward(self, x):
        conv  = F.convXd(x, weight=self.conv.weight, bias=None,  dim=self.dim) # dim can be one of {1, 2 or 3}
        return self.bn(conv)

model  = ConvBN()

