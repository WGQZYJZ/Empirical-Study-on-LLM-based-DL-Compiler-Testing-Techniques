
class Model(nn.Module):
    def __init__(self, dim: int = 16) -> None:
        super().__init__()
        self.conv = nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1: Tensor) -> Tensor:
        v1 = self.conv(x1)
        v2 = torch.cat([v1, v1], dim=-1)
        return v2


# Initializing the model
m = Model()


