
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, y2):
        v1 = torch.cat([x1[:, None], y2])
        return v1


# Initializing the model