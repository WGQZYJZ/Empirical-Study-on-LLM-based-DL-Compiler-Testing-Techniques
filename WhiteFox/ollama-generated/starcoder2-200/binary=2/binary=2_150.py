
class Model(torch.nn.Module):
    def __init__(self, num_classes=10):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 5)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = v1 - other
        return v2
# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(3, 8, 64, 64)
 
other  = torch.randn(v1).abs()
other = other.mean(dim=[0]) 
 
__output__  = m(x1)

