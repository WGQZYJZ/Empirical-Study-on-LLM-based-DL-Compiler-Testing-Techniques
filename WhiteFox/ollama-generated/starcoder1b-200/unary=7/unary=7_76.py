
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(1, 64)

    def forward(self, x):
        v  = self.linear(x)
        return clamp(min=0, max=6, l1  + 3) / 6


# Initializing the model
m = Model()


