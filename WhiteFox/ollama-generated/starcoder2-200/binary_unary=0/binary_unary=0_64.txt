
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)

    def forward(self, x1):
        v1 = self.conv(x1)

        def add_tensor(a: torch.Tensor) -> torch.Tensor:
            return a + other

        return torch.relu(v1)

# Initializing the model
m  = Model()
other = ... # Any tensor with same shape and type of v1

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
