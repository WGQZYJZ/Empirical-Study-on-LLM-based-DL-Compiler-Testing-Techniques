
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 64, (3, 1), (1, 1))

    def forward(self, x):
        v = self.conv(x)
        return torch.nn.functional.batch_norm(v, 0, 1e-5, v.shape[2], v.shape[3])


# Inputs to the model
x = torch.randn(1, 3, 28, 28)
