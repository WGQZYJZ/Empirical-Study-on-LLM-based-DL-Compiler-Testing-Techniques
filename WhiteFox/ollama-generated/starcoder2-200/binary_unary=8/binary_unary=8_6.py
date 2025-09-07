
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + self._other_tensor
        return v2
 
m = Model()

 # Initializing the model with custom tensor 
m.__other_tensor__ = torch.randn(1, 3, 4000, 58697)

 # Inputs to the model and outputs of the model 
x1 = torch.randn(20, 3, 3, 4000, 58697)
__output__  = m(x1)

