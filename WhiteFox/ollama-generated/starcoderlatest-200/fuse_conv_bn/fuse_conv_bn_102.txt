
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 4, kernel_size=3)

    def forward(self, x1):
        v1 = x1.permute(0, 3, 1, 2)
        v2 = self.conv1(v1)
        return v2


# Initializing the model
m = Model()
x = torch.randn(1, 3, 4, 5)
