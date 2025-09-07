
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2, x3):
        v1 = self.conv(x1)
        v2 = self.conv(x2)
        v3 = self.conv(x3)
        t1 = torch.cat([x1, v3], dim=1)
        t2 = t1[:, 0:9223372036854775807]
        return t2


# Initializing the model
m = Model()

# Inputs to the model
inputs1 = [torch.randn(1, 3, 16, 16),
            torch.randn(1, 3, 16, 16),
            torch.randn(1, 3, 16, 16)]
inputs2 = [torch.randn(1, 3, 8, 8),
            torch.randn(1, 3, 8, 8),
            torch.randn(1, 3, 8, 8)]
inputs3 = [torch.randn(1, 3, 4, 4),
            torch.randn(1, 3, 4, 4),
            torch.randn(1, 3, 4, 4)]
