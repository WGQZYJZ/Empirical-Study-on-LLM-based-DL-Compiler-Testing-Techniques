
class ResidualModel(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = self.net(x1) + x2
        return v1

model  = ResidualModel()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
