
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1, t2):
        return torch.cat([t1, t2], 0).view(-1, ...)


# Initializing the model