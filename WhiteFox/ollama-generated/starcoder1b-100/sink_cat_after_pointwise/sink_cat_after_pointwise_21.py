
class Model(torch.nn.Module):
    def __init__(self, linear):
        super().__init__()
        self.linear = linear

    def forward(self, x1, x2):
        v1 = torch.cat([x1, x2], dim=0)
        v2 = self.linear(v1)
        return v2


# Initializing the model
m = Model(torch.nn.Linear(2, 3))

