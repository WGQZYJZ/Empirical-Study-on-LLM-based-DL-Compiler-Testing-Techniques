
class Model(torch.nn.Module):
    def __init__(self, negative_slope=1.0):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
        self.negative_slope = negative_slope

    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 > 0).float() * self.negative_slope
        return torch.where(v2, v1, v2)


# Initializing the model
m = Model()


