
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(50, 10)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        v = self.linear(x) + other # Add a keyword argument "other" to the linear transformation and add it as a scalar `+`.
        return relu(v)


# Initializing the model
m  = Model()


