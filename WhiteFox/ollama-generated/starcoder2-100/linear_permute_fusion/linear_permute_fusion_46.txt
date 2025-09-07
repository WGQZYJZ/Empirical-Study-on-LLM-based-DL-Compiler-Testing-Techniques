

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)

    def forward(self, x1):
        v1 = torch.nn.functional.relu(x1 - 0.25 * (torch.ones_like(x1)))
        v2 = v1 ** 2 / 4

        out = self.linear(v2)
        return out


# Initializing the model
m  = Model()

# Input tensors to the model
__x1__, __x2__, __x3__ = torch.randn(1, 50), torch.randn(60,), torch.randn(70,)

# Outputs from the model with input tensors: __x1__, __x2__, and __x3__ respectively.
m(__x1__), m(__x2__), m(__x3__)
