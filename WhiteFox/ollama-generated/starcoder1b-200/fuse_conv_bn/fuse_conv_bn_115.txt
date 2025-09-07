
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvXd(...)  # X can be 1, 2, or 3 representing the dimension
        self.bn   = torch.nn.BatchNormXd(...) # X should match with ConvXd
        self.linear  = torch.nn.Linear(64, 1)

    def forward(self, x1):
        conv  = self.conv(x1)
        bn    = self.bn(conv)
        return self.linear(bn)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 4, 4)
