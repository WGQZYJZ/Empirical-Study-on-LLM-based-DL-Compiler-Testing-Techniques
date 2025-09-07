
class FuseConvBN(torch.nn.Module):
    def __init__(self, in_channel=1):
        super().__init__()
        self.conv  = torch.nn.ConvXd(...) # X can be 1, 2, or 3 representing the dimension
        self.bn    = torch.nn.BatchNormXd(...) # X should match with ConvXd
        self.relu  = nn.ReLU()

    def forward(self, input_tensor):
        conv = self.conv(input_tensor)
        bn   = self.bn(conv)
        return self.relu(bn)


# Input to the model
x1 = torch.randn(1, 1, 1, 3)
