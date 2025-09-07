
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1  = torch.nn.Conv2d(3, 8, 3)
        self.conv2  = torch.nn.ConvTranspose2d(8, 3, 4)
 
    def forward(self, x1):
        v1  = self.conv1(x1)
        v2  = self.conv2(v1)
        return v2


# Initializing the model
m = Model()
 
 # Inputs to the model
x1  = torch.randn(5, 3, 784, 784)
  __output__  = m(x1)

