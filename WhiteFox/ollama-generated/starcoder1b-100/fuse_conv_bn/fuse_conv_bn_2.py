
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv1d(...)  # X can be 1, 2, or 3 representing the dimension of a batch
        self.bn  = torch.nn.BatchNorm1d(...)

    def forward(self, x1):
        v1 = x1.permute(0, 2)
        v2 = self.conv(v1)
        v2 = self.bn(v2)
        return v2


# Inputs to the model
x1 = torch.randn(1, 3, 4)
