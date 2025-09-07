
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    @property
    def conv(self):
      return torch.nn.Conv2d(in_channels=1, out_channels=2, kernel_size=(3, 3))

    def forward(self, x1):
      y = self.conv(x1)
      z = torch.nn.functional.batch_norm(y, running_mean=None, running_var=None)
      return z


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 1, 4, 4)
