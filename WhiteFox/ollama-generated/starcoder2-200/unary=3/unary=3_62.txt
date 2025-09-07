
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self._weights  = self.conv.weight
 
    def forward(self, x1):
        v1  = self._weights * x1 # Multiplication in the model definition
        v4  = torch.erf(v3)
        v5  = v4 + 1
        v6  = v2  * v5 
        return v6


# Initializing the model
m  = Model() 


# Inputs to the model
x1  = torch.randn(8, 3, 60, 60)
