
class Model(torch.nn.Module):
    def __init__(self, input_size: Tuple[int]):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 3)
        self.conv2 = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = torch.cat([v2, v2, ..., v2], dim=-1)  # The result tensor of the matrix multiplication operation should be concatenated along the -1 dimension
        return v3


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
