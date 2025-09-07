
class Model(torch.nn.Module):
    def __init__(self, min_value=-0.79769313485300421, max_value=0.79769313485300421):
        super().__init__()
        self.linear = torch.nn.Linear(2, 1)

    def forward(self, x):
        v = self.linear(x)
        v = torch.clamp_min(v, min_value=min_value)
        v = torch.clamp_max(v, max_value=max_value)
        return v


# Initializing the model
m = Model(min_value=-10, max_value=10)


