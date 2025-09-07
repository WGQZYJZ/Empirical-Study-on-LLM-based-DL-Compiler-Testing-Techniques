
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.bmm = torch.nn.Bilinear(2, 3, 1)

    def forward(self, x1, x2):
        v1 = x1.permute(0, 2, 1)
        v2 = x2.permute(0, 2, 1)
        return torch.bmm(v1, v2)


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 2, 3)
x2 = torch.randn(1, 2, 1)
