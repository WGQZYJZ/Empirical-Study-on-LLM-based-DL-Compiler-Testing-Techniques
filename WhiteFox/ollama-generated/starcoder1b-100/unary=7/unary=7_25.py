
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 2, bias=False)

    def forward(self, x1):
        v1 = self.linear1(x1) + 3
        return clamp(min=0, max=6, v1) / 6


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 3)
