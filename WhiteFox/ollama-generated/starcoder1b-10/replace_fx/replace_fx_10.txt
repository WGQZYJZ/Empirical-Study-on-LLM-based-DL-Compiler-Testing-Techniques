
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(2, 2)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        return self.linear(v1)


# Initializing the model
m = Model()
m.set_fallback_random(True)

x1 = torch.randn(1, 2, 2)
