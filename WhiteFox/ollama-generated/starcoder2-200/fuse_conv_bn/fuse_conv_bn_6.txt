
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv1d(2, 4, 3)
        self.batchnorm = torch.nn.BatchNorm1d(4)

    def forward(self, x1):
        v1 = self.conv(x1).permute(0, 2, 1)
        v2 = torch.nn.functional.linear(v1, self.batchnorm.weight, self.batchnorm.bias)

        return v2

# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(30, 5, 14)
