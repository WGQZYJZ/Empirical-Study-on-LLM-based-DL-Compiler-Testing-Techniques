
class Model(torch.nn.Module):
    def __init__(self, ...):
        super().__init__()
        ...

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = torch.cat([x1, x2], dim=1)
        # If this is a sink_cat after pointwise operation, this will be triggered during optimization and removed after analysis.
        return torch.relu(v2).view(-1)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 2)
x2 = torch.randn(1, 4, 5)
