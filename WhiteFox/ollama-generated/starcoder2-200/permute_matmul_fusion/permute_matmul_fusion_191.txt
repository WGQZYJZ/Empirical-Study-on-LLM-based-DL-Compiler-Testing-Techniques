
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1: Tensor, x2: Tensor) -> Tensor:
        t1 = x1.permute((0, 2, 1))
        t3 = torch.bmm(t1, x2).sum()

        return t3


# Initializing the model
m  = Model()


# Inputs to the model
x1 = torch.randn(1, 2, 4)
x2 = torch.randn(1, 5, 4)
