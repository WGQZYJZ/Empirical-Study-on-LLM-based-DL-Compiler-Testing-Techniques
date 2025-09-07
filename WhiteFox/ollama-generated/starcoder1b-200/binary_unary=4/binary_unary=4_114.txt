
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 1)

    def forward(self, x):
        return self.linear(x) + other


# Initializing the model
m = Model()
