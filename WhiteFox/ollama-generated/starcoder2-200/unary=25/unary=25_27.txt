
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.linear = torch.nn.Linear(4*5136+8*96+37768+20160+256 + 2*703984, 1)

    def forward(self, x1):
        v1 = self.linear(x1)

        v2 = torch.where((v1 > 0), v1, v1 * negative_slope)
        return v2


# Initializing the model