
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        return torch.split(x1, 64 * 256 // 3 + [0], dim=1)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 9875, 32, 32)
