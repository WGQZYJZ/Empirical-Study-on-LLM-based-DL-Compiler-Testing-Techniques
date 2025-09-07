
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.01):
        super().__init__()
        self.linear = torch.nn.Linear(3, 2)

    def forward(self, x1):
        v1 = self.linear(x1)
        mask = (v1 > 0).to(torch.uint8)
        x2 = torch.where((mask == True), v1, torch.neg(v3))
        return x2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
