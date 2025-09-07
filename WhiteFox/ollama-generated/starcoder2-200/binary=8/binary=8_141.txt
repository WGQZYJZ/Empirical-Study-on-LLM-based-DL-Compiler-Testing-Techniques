
class Model(torch.nn.Module):
    def __init__(self, oth):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self._oth = oth
    
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + self._oth

# Initializing the model
m = Model(oth=torch.randn())

 # Inputs to the model 
x1 = torch.randn(1, 3, 64, 64)
