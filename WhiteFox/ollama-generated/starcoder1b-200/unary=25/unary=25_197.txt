
class Model(torch.nn.Module):
    def __init__(self, positive_slope: float):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)
        self.positive_slope = positive_slope

    def forward(self, x1):
        v1 = self.linear(x1) * self.positive_slope
        return v1


# Initializing the model
m = Model()


