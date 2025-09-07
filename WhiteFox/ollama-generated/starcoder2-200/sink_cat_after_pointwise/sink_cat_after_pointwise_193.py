
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, t1: torch.Tensor) -> torch.Tensor:
        v2  = torch.relu(t1.view(-1))
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
__output__  = m(torch.randn(3, 100))


