
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        y = x + 10

        return torch.cumsum(y, 1)


x = torch.zeros([4, 3, 64, 64], dtype=torch.uint8)
