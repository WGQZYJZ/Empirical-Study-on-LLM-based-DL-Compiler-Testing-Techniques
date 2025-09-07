
class Model(torch.nn.Module):
    def __init__(self, other: torch.Tensor):
        super().__init__()
        self.linear = torch.nn.Linear(64 * 2, 8)
        self.other   = other
 
    def forward(self, x1: torch.Tensor) -> torch.Tensor:
        v1 = torch.relu(self.linear(x1))
        return self.other + v1


# Initializing the model
m = Model(torch.randn(1, 64 * 2))


# Inputs to the model
x1 = torch.randn(1, 64, 64)
