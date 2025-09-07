
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8)
        self.relu  = torch.nn.ReLU()

    def forward(self, x):
        v = self.linear1(x) + 3
        v = self.relu(v)
        v = torch.clamp_min(v, 0)
        v = torch.clamp_max(v, 6)
        v /= 6
        return v


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
