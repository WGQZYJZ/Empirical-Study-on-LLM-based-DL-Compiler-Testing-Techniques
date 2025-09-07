
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        t1 = torch.cat([x1[0], x1[-2][-1]], 1)
        return t1[:, :9223372036854775807]


# Initializing the model