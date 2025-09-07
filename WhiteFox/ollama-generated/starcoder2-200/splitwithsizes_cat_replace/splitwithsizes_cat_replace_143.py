

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        x2 = torch.split(x1, 30768, dim=2)
        x3 = torch.cat([t for t in x2], dim=2)

# Initializing the model