
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv1d(...)

    def forward(self, x):
        y = F.batch_norm(F.conv1d(x), ...)
        return y


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(10, 20, 3)
