
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(3, 8)

    def forward(self, x1):
        v1 = self.linear1(x1)
        return clamp(min=0, max=6, l1 + 3) / 6


# Initializing the model
m = Model()


