
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v = torch.cat([x1[:, :, 0], x1[:, :, 1], ...], dim=2)
        return torch.relu(v)


# Initializing the model
m = Model()


