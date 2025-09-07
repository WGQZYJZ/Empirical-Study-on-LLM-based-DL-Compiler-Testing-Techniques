
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv1d(...)  # Conv1d for simplicity
        self.bn = torch.nn.BatchNorm1d(...)

    def forward(self, x):
        return self.bn(self.conv(x))

# Initializing the model
m = Model()

# Inputs to the model
input_tensor = torch.randn(32, 5, 10)
__output__  = m(input_tensor)

