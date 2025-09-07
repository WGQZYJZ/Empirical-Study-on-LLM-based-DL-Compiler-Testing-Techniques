
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x0):
        v1  = self.conv(x0)

# Initializing the model
m  = Model()

 # Inputs to the model
x0 = torch.randn(2, 3, 64, 64)
