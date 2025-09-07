

class Model(torch.nn.Module):
    def __init__(self, size):
        super().__init__()

    def forward(self, x):
        v1 = torch.cat([x])
        v2 = v1[:, :size]
        v3 = torch.cat([v1], 0)


# Initializing the model