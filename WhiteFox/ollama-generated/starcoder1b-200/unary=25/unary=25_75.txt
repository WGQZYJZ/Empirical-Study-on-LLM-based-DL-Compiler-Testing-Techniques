
class Model(torch.nn.Module):
    def __init__(self, negative_slope: float = 0.2):
        super().__init__()
        self.linear  = torch.nn.Linear(1, 2)
        self.negative_slope  = negative_slope
 
    def forward(self, x: torch.Tensor) -> torch.Tensor:
        v1 = self.linear(x) > 0
        v2 = v1 * -self.negative_slope
        v3 = torch.where(v2, v1, v2)
        return v3


# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(4, 10)
