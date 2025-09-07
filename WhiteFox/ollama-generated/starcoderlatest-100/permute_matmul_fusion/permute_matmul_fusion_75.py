
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1, x2):
        v1 = torch.bmm(x1, x2) # (10, 8, 4) * (4, 3, 5) -> (10, 8, 3)
        return v1


# Inputs to the model
x1 = torch.randn(10, 8, 4)
x2 = torch.randn(4, 3, 5)
