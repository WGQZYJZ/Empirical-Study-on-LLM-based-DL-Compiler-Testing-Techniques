
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv1d(...)  # X should be either 2 or 3, and represent the dimension
        self.bn    = torch.nn.BatchNorm1d(...)
        self.linear = torch.nn.Linear(...)

    def forward(self, x):
        return self.linear(self.conv(x))


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 2, 4)
