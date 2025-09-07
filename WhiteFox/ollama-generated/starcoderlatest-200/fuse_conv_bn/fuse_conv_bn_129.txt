
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 2, 3)

    def forward(self, x1):
        v1 = x1.permute(0, 2, 1)
        v2 = self.conv(v1).permute(0, 2, 1)
        return v2

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 2, 2, 2)
