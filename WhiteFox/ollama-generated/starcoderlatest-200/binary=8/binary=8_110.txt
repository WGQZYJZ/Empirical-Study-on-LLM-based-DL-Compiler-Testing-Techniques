
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, other_tensor=None):
        v1 = self.conv(x1)
        v2 = v1 + (other_tensor if other_tensor is not None else torch.randn(4))
        return v2
# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
v1 = m(x1)

 # Another inputs to the model
other_tensor = torch.randn(4)
