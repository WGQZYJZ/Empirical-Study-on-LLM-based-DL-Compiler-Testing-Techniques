
class Model(torch.nn.Module):
    def __init__(self, min_value=-10, max_value=10):
        super().__init__()
        self.linear = torch.nn.Linear(32*64*64, 8)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp(v1, min_value=min_value)
        v3 = torch.clamp(v2, max_value=max_value)
        return v3

# Initializing the model