
class Module(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 64, 7)

    def forward(self, x):
        return torch.nn.functional.batch_norm(self.conv1(x))

# Initializing the model
m = Module()

# Inputs to the model
x1 = torch.randn(256, 3, 14, 14)
__output__  = m(x1)

