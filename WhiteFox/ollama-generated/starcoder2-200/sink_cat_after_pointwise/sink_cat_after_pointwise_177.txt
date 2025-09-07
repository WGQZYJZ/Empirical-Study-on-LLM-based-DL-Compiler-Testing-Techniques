
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):  # Forward function to be optimized.
        # First reshaping layer.
        v = torch.nn.functional.relu(x1)

        # Concatenation and reshaping layers.
        v2 = torch.cat([v, v], dim=0).view(-1, 5, 3)
        v3 = v2[:, 4]

        return v3


# Initializing the model
m = Model()

