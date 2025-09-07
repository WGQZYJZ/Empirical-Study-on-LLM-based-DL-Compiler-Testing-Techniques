
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self._other  = torch.randn(3, 8, 64, 64)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + self._other 
        v3  = torch.relu(v2)  
        return v3


# Initializing the model
m = Model()

 # Inputs to the model
__output__  = m(torch.randn(1, 3, 64, 64))
 