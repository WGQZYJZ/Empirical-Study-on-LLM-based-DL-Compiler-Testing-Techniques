
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self,__input__):
        v0  = __input__
        v1  = self.conv(__input__)
        v2  = v1 > 0
        v3  = v1 * negative_slope
        v4  = torch.where(v2, v1, v3)
        return v4

# Initializing the model
m  = Model()

 # Inputs to the model
x1 = torch.randn(1,3,64,64)
 
 # Outputs of the model
__output__= m(x1)

