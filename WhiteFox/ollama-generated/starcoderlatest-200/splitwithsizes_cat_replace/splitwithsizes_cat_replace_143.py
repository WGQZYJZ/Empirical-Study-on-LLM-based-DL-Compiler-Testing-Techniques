
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1 = torch.split(x1, 8, dim=1)
        v2 = torch.cat([v1[i] for i in range(len(v1))], dim=1)
        return True


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
