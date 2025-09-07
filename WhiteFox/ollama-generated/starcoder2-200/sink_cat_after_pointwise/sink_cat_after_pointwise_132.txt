
class Model(torch.nn.Module):
    def __init__(self, x1, x2):
        super().__init__()

    def forward(self, x1):
        v = torch.relu(
            torch.cat([
                torch.randn((x1 + 1), (4 * x1 + 10)),
                torch.randn_like((v2 * x3), 750000, 26) + 987654
            ], dim=1).view(v))
        return v


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randint(low=1, high=200000, size=(3,))
x2 = 987654
