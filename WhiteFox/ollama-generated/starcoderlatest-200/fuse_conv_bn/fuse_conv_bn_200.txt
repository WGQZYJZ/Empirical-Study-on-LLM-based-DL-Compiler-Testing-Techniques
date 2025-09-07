
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 32, kernel_size=3)

    def forward(self, x):
        return self.conv(x)

 # Initializing the model
m = Model()
# Inputs to the model
input = torch.randn(1, 1, 4, 4)
