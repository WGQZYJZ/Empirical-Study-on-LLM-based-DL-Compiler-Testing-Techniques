
class Model(torch.nn.Module):
    def __init__(self, positive_slope, negative_slope):
        super().__init__()
        self.linear = torch.nn.Linear(100, 5)
        self.pos_linear = torch.nn.Linear(200, 200)
        self.negative_slope = positive_slope
        self.neg_linear = torch.nn.Linear(500, 500)
 
    def forward(self, x):
        v1 = self.linear(x)
        v2 = torch.relu(v1)
        v3 = self.pos_linear(v2)
        v4 = v3 * self.negative_slope
        v5 = v4 + 1
        v6 = torch.where(v5 < 1, v2, v4)
        return v6


# Initializing the model
m = Model(-0.81873199, -0.185629394)


