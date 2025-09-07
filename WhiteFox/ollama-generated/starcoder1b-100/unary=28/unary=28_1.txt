
class Model(torch.nn.Module):
    def __init__(self, min_value=1e-6, max_value=100):
        super().__init__()
        self.linear = torch.nn.Linear(32, 8)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x):
        v  = self.linear(x)
        return torch.clamp_min(v, self.min_value), torch.clamp_max(v, self.max_value)


# Initializing the model
m = Model(min_value=256)


# Inputs to the model
x1 = torch.randn(1, 3, 32, 32)
__output1__, __output2__ = m(x1)

# Inputs of new generated model that should be different from the previous one
new_x1 = torch.randn(1, 8, 64, 64)
__output_new__ = m(new_x1)


