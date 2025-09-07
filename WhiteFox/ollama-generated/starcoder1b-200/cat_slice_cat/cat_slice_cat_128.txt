
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        # Slice along dimension 1
        v1 = torch.cat([x1[:, i:i+1] for i in range(len(x1), -1, -1)], dim=1)
        v2 = torch.cat([x2[i:i+1] for i in range(len(x2), -1, -1)], dim=1)
        return v1 * v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = x2 = None  # No inputs
