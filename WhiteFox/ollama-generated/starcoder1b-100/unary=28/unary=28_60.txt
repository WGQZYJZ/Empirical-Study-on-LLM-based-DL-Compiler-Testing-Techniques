
class Model(torch.nn.Module):
    def __init__(self, min_value=1e-6, max_value=2e-6):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 - self.min_value) / (self.max_value - self.min_value)
        v3 = torch.clamp(v2 + 0.5, min=0.5, max=1.0)
        return v3


# Initializing the model
m = Model()


