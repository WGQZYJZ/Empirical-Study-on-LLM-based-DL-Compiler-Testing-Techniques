
class Model(torch.nn.Module):
    def __init__(self, other: torch.Tensor):
        super().__init__()
        self.linear = torch.nn.Linear(3, 8)

    def forward(self, x1):
        return self.linear(x1) + other


# Initializing the model
m = Model(torch.tensor([[0]]))

