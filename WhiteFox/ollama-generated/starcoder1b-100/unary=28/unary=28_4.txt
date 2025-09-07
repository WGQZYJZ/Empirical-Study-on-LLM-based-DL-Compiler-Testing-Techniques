
class Model(torch.nn.Module):
    def __init__(self, min_value=1e-8, max_value=50.0):
        super().__init__()
        self.linear = torch.nn.Linear(10, 20)
        self.min_value  = min_value
        self.max_value  = max_value

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp_min(v1, self.min_value)
        v3 = torch.clamp_max(v2, self.max_value)
        return v3


# Initializing the model
m = Model()


