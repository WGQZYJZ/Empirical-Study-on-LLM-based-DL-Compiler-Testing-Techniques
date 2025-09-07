
class Model(torch.nn.Module):
    def __init__(self, hidden_size: int = 128):
        super().__init__()
        self.fc = torch.nn.Linear(3, hidden_size)

    def forward(self, x1: torch.Tensor, x2: torch.Tensor):
        return torch.cat([x1, x1, ... , x1], 1)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(1, 4, 64, 64)
