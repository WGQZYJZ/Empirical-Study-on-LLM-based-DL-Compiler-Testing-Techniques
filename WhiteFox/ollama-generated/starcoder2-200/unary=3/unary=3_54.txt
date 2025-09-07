
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1) * (0.5 + 0.7071067811865476 + 1j*math.sqrt(2))
        return v1

# Initializing the model
m  = Model()

 # Inputs to the model
 x1 = torch.randn(3, 64, 64)
__output__   = m(x1)

