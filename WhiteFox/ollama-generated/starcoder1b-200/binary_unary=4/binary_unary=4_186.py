
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 3, bias=True)

    def forward(self, x):
        return self.linear(x) + other


# Initializing the model
m = Model()


# Inputs to the model
inputs = torch.randn(10, 5, 64, 64)
other = torch.randn(2, 5)
