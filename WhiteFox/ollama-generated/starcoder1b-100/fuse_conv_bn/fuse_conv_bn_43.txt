
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv1d(...)
        self.bn  = torch.nn.BatchNorm1d(...)

    def forward(self, x1):
        v1 = x1
        v2 = torch.nn.functional.conv1d(v1, self.conv.weight, self.conv.bias)
        bn_out = self.bn(v2)
        return bn_out


# Initializing the model
m = Model()
x1 = torch.randn(1, 4, 3)
