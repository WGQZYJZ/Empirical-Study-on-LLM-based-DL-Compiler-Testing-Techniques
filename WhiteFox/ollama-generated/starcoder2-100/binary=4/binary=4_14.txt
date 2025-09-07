
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(128, 30)

    def forward(self, x):
        v1 = self.linear(x)
        return v1 + other


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(64, 128)


# Input tensor used for testing the example: torch.Tensor([0.35])
other = torch.Tensor([0.35])
