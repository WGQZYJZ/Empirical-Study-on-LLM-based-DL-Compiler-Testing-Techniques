
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 16, kernel_size=5)

    def forward(self, x):
      output = torch.nn.functional.conv2d(x, self.conv.weight, bias=None, stride=(2, 2))

# Initializing the model:
m = Model()

 # Inputs to the model
x1 = torch.randn(30)
