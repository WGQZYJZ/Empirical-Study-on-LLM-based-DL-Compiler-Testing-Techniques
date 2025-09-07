
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv1d(...)  # Use Conv1d for testing
        self.bn = torch.nn.BatchNorm1d(...)

    def forward(self, x):
        conv = self.conv(x)
        bn = self.bn(conv)
        return conv

model  = Model()
__output__  = model(torch.randn(32, 4096))

