
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(12, 8)

    def forward(self, x1):
        v1 = self.linear(x1)
        t2 = v1 > 0
        t3 = v1 * -1
        v4 = torch.where(t2, v1, t3)
        return v4


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 12, 64, 64)
