
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * 0.5
        v3  = v1  +  1
        v4  = torch.erf(v3)
        v5  = v4 
        return v5

# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(1, 3, 67, 208)
__output__  = m(x1)

