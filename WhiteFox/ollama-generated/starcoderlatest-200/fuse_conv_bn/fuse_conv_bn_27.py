
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(...)

    def forward(self, x1):
        v1 = self.conv(x1)  # Fuse conv and batch norm layers here
        return v1

# Inputs to the model
x1 = torch.randn(1, 3, 48, 48)
