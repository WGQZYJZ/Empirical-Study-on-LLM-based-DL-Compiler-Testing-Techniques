
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(10, 10)

    def forward(self, x):
        v = self.linear(x)
        return torch.clamp_min(v, min_value)

# Initializing the model
m = Model()


