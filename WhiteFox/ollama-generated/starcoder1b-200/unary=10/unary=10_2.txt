
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 4)
        self.relu   = torch.nn.ReLU()
        self.tanh   = torch.nn.Tanh()

    def forward(self, x):
        v = self.linear1(x)
        v = self.relu(v)
        v = self.tanh(v)
        return v


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(1, 3, 64, 64)
