
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2=None):  # No inputs here.

        v1 = torch.cat([x1, x2], dim=-1)
        v2 = torch.relu(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 2)  # Note that inputs are not needed here
