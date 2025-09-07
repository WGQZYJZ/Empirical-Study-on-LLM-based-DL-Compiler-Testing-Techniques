
class Model(torch.nn.Module):
    def __init__(self, min_value=1e-3, max_value=0.5):
        super().__init__()
        self.linear = torch.nn.Linear(784, 1)

    def forward(self, x):
        v = self.linear(x)
        v = torch.clamp_min(v, min_value)
        v = torch.clamp_max(v, max_value)
        return v
# Initializing the model
m = Model()


