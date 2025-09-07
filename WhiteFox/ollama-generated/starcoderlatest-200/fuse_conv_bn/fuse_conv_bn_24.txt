
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv1d(...)
        self.bn = torch.nn.BatchNorm1d(...)

    def forward(self, x):
        output  = self.conv(x)
        output += self.bn(output)
        return output

# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 2, 3)
