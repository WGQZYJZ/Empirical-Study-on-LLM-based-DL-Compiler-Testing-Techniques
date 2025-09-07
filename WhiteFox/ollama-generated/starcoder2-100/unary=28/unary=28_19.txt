
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v0  = self.lrelu32(x1)

        return v0


# Initializing the model