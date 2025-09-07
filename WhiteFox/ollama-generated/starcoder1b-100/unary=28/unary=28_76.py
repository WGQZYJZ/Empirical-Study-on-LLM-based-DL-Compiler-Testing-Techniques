
class Model(torch.nn.Module):
    def __init__(self, min_value=0.1, max_value=1.0):
        super().__init__()
        self.linear = torch.nn.Linear(3, 4)
        self.clamp = torch.nn.Clamp(min_value=min_value, max_value=max_value)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = self.clamp(v1)
        return v2


# Initializing the model
m = Model(0.5, 1.5)


