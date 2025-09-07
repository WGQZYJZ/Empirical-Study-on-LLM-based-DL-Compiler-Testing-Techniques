
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=1)
 
    def forward(self, x):
      v1  = self.conv(x)
      v2  = torch.sigmoid(v1)
      v4  = v1 * v2
      return v4


# Initializing the model
m = Model()


# Inputs to the model
x = torch.randn(3,3,64,64)
