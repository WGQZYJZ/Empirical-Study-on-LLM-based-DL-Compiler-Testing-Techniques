

class Model(torch.nn.Module):
    def __init__(self, min=0.0, max=1e3):
        super().__init__()
        self.linear = torch.nn.Linear(28 * 28 + 49, 5)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, min=0.0)
        v3 = torch.clamp_max(v2, max=1e3)
        return v3

# Initializing the model
m = Model()

