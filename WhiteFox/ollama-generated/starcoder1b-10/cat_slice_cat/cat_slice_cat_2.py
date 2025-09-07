
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = torch.cat((x1[:, :9223372036854775807],
                        x1[:, 9223372036854775807:]), dim=1)  # Slices along dimension 1
        v2 = torch.cat([v1[:, :2147483647], v1[:, 2147483647:]], dim=1)  # Slices along dimension 1
        return torch.cat((x1, v2), dim=1)


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
