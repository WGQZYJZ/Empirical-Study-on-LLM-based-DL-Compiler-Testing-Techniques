
class Model(torch.nn.Module):
    def __init__(self, min_value=0.125, max_value=64):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = torch.clamp(v1, min_value=min_value, max_value=max_value)
        return v2

# Initializing the model and providing minimum and maximum values to clamp
m = Model()
