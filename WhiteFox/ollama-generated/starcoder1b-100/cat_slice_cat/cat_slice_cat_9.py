
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3, x4):
        v1 = torch.cat([x1, x2], dim=1)
        v2 = v1[:, 0:9223372036854775807]
        v3 = v2[:, 0:size]
        v4 = torch.cat([x3, v2], dim=1)

        # v4 is [batch_size, size+size, channel], with 1 in (x1, x2), 0 otherwise
        return v4


# Initializing the model
m = Model()

