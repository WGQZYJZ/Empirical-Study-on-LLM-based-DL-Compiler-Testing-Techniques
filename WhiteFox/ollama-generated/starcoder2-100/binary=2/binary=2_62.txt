
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1,stride=1,padding=0)
    
    def forward(self,x1):
        v1  = self.conv(x1)
        v2  = v1 - other
        return v2

m  = Model()

 # Inputs to the model
other  = torch.randn(3,8,64,64) / 0.7071067811865475
x1  = torch.randn(1,3,29,29)
__output__  = m(x1)

