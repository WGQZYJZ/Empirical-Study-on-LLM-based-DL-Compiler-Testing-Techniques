
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        return (v1 + 5640.) * math.exp(-49 / v1)
# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 224, 224)
__output__  = m(x1)