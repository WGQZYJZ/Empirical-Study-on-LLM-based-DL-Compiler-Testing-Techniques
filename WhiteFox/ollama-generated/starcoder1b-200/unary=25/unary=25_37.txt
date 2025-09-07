
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.linear = torch.nn.Linear(3, 1)

    def forward(self, x1):
        v1 = self.linear(x1) > 0
        v2 = torch.where(v1, x1, -self.linear.weight * self.linear.negative_slope)
        return v2


# Initializing the model
m = Model()


