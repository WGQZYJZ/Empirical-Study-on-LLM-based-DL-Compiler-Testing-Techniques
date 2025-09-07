
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, size=9223372036854775807):
        v1 = torch.cat([x1, torch.ones_like(x1[:, 0:size])], dim=1)
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
