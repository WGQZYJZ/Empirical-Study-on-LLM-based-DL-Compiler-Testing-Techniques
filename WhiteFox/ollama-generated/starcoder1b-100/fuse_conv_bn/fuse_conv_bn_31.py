
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv1d(...)
        self.bn = torch.nn.BatchNorm1d(...)

    def forward(self, x):
        x = self.conv(x)
        return self.bn(x)


# Initializing the model
m = Model()


