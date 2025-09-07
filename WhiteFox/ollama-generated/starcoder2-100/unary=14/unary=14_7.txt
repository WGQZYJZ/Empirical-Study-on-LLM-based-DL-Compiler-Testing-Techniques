
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1d = torch.nn.ConvTranspose2d(3,8, 1, stride=1)
 
    def forward(self, x1):
        v1  = self.conv1d(x1)
        v2  = F.sigmoid(v1) 
        return v2 * v1


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
  