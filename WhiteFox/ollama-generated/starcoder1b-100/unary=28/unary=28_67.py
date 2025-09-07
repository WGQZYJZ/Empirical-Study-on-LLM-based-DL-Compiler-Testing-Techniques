
class Model(torch.nn.Module):
    def __init__(self, min_value=0.25, max_value=1.75):
        super().__init__()
        self.linear = torch.nn.Linear(1, 1)
        self.min_value = min_value
        self.max_value = max_value

    def forward(self, x1):
        v1 = self.linear(x1)
        return (torch.clamp_min(v1, self.min_value), torch.clamp_max(v1, self.max_value))

# Initializing the model
m = Model(min_value=0.5)

 # Inputs to the model
x1 = torch.randn(3, 1)
