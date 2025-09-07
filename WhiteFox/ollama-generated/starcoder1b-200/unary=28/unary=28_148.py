
class Model(torch.nn.Module):
    def __init__(self, min_value=-1.0, max_value=1.0):
        super().__init__()
        self.linear  = torch.nn.Linear(32, 4)

    def forward(self, x1):
        v1 = self.linear(x1)
        return torch.clamp(v1, min_value=min_value, max_value=max_value)

# Initializing the model
m = Model(min_value=-0.5, max_value=0.5)


