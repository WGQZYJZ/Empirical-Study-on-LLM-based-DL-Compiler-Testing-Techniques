
class Model(torch.nn.Module):
    def __init__(self, n1: int = 50) -> None:
        super().__init__()
        self.n1 = n1

    def forward(self, x1):
        v1  = torch.rand(x1.size()).to("cpu")
        if (v1 < .3).all():
            v2  = x1 ** -5 + 2 * x1 ** -4 + 8 * x1 ** -3 + -90 * x1 ** -2 + 76 / \
                torch.where(torch.ge(x1, 1),
                            (v1 - .3) ** (-2),
                            0)
        else:
            v2 = torch.relu(x1 ** n1)

        return v2


# Initializing the model