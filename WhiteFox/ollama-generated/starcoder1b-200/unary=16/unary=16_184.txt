
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Linear(8, 1)
        self.relu = torch.nn.ReLU()

    def forward(self, x):
        v1 = self.conv(x)
        return self.relu(v1)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 8)
