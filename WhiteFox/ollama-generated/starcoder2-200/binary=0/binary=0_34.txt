
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) + self._other_tensor
        return v1

# Initializing the model and setting _other_tensor
m = Model()
m._other_tensor = torch.randn(32, 8, 64, 64)

 # Inputs to the model
 x1  = torch.randn(1, 3, 64, 64)
 
 __output__  = m(x1)
 