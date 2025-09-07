
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 64, (3, 3))

    def forward(self, x1):
        v1 = x1.permute(0, 3, 2, 1)
        v2 = torch.nn.functional.batch_norm(v1, [1], [0.5])
        v3 = self.conv(v2)
        return v3


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
