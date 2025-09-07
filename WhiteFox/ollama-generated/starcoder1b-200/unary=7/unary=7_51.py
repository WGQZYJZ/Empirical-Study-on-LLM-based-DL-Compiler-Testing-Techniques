
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 8)

    def forward(self, x):
        v  = self.linear(x) * clamped_value
        return v


# Initializing the model
m = Model()

