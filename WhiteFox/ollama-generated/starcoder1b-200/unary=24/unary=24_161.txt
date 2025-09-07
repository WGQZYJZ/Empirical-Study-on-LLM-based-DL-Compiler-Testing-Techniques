
class Model(torch.nn.Module):
    def __init__(self, negative_slope: float = 0.25):
        super().__init__()
        self.negative_slope = negative_slope

    def forward(self, x1: torch.Tensor) -> torch.Tensor:
        return torch.where(x1 > 0, x1 * self.negative_slope, 0)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
