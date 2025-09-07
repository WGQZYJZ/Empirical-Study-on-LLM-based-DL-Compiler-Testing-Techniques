
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x1):
      v0 = self.conv(x1)
      v1 = v0 - other
      return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(245, 3, 64, 64)
other = torch.randn(245,8,64,64) / x1.shape[0] # other is a randomly generated tensor of shape [batch_size , channel size, height, width].
__output__= m(x1)


