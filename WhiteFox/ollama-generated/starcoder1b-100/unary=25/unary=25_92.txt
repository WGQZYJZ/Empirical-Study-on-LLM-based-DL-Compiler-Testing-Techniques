
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear  = torch.nn.Linear(8, 4)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.where(v1 > 0, v1, - v1 * self.negative_slope)
        v3 = v2 * - self.negative_slope
        v4 = torch.nn.functional.leaky_relu(self.linear(v3), negative_slope=self.negative_slope)
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
