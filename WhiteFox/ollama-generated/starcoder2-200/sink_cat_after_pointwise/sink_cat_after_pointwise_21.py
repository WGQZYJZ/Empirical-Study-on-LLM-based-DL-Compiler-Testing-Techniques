
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):  # Input shape: (batch size, 3)
        v1 = torch.cat([x1, x2], dim=1)
        v2 = v1.view(-1, 6)

        return v2

# Initializing the model