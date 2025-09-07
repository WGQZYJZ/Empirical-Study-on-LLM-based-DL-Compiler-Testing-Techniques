
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(8, 10)

    def forward(self, x1):
        v2 = self.linear(x1) - other
        return v2


# Initializing the model
m = Model()

# Inputs to the model
__inputs__ = [torch.randn(1, 8), torch.tensor(-0.5)]
m(*__inputs__)