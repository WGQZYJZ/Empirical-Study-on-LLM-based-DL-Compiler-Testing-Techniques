
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self._other = torch.randn((64, 5))
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + self._other 
        v3  = F.relu(v2)
        return v3


# Initializing the model
m  = Model()

 # Inputs to the model
