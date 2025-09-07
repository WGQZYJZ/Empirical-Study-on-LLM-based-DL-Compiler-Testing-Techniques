
class Model(torch.nn.Module):
    def __init__(self, linear):
        super().__init__()
        self.linear = linear

    def forward(self, x1):
        t1  = torch.cat([x1, x2, ...], dim=...)
        v1  = self.linear(t1)
        return v1


# Initializing the model
m = Model(torch.nn.Linear(2, 2))
