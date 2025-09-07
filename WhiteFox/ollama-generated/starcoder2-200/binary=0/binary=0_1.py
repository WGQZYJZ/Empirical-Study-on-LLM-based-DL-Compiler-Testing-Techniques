
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        return v1 + torch.ones_like(v1)

# Initializing the model with keyword argument other
m = Model()

 # Inputs to the model
x2 = torch.randn(1, 3, 64, 64)
__output__  = m(x2)