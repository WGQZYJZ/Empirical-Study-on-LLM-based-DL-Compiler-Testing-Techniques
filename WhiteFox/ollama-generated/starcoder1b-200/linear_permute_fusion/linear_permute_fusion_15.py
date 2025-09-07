
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)

    def forward(self, x):
        v = torch.tanh(self.linear(x))
        return v


# Initializing the model
m = Model()

