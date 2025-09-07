
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=1)
 
    def forward(self, x):
        v01    = self.conv(x)
        v02    = torch.sigmoid(v01)
        v03    = v01 * v02 
        return v03


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1,3,64,64)
__output__     = m(x1)

