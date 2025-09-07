
class Model(torch.nn.Module):
    def __init__(self, n1: int=2048) -> None:
        super().__init__()

        self._weight = torch.nn.Parameter(
            torch.randn([n1])  # Use random weight initialization method for PyTorch parameters
        )

    def forward(self, x):
        v = x[:, ::-1] * self._weight[None].permute(0, 2)
        return torch.bmm(v[..., None], x).squeeze()


# Initializing the model
m = Model()


# Inputs to the model
x_a = torch.randn(16, 4937)
x_b = torch.randn(1024, 512)
