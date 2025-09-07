
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(3, 8, bias=False)

    def forward(self, x1):
        v1 = self.conv(x1)

        v2 = clamped_sum(v1 + 6.0) / 6.0
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3)
