
class Model(torch.nn.Module):
    def __init__(self, other: torch.Tensor):
        super().__init__()
        self.linear = torch.nn.Linear(10, 20)

    def forward(self, x1):
        v1 = self.linear(x1) + other
        return v1


# Inputs to the model
x1 = torch.randn(1, 10)
other  = torch.randn(10)
