
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v = torch.cat([x1, x2], dim=1)
        v = v[:, 0:9223372036854775807]
        v = v[:, 0:size]
        return v


# Initializing the model
m = Model()


