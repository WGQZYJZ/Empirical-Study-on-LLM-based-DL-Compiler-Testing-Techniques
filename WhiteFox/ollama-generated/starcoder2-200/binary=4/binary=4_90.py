
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear1 = torch.nn.Linear(256 * 3, 9)

    def forward(self, x1):
        v1 = self.linear1(x1)
        v2 = v1 + torch.randn(9,)
        return v2


# Initializing the model