
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v4  = -v1 / math.sqrt(math.expm1(9)) * 0 + 1
        return torch.relu6(v4)

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(2, 3, 32, 32)
__output__  = m(x1)
 
