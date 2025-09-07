
class Model(torch.nn.Module):
    def __init__(self, neg_slope=100):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)
        self.neg_slope = neg_slope

    def forward(self, x1):
        v1 = self.linear(x1) > 0
        v2 = (torch.where(v1, x1, torch.mul(v1, -1 * self.neg_slope)))
        return v2


# Initializing the model
m = Model()


