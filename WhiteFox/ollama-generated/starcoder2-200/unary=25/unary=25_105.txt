
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
        v1  = torch.nn.Linear()(x1) 
        v2  = (v1 > 0).float() * (-1.) + (~(v1 > 0)).float()
        v3  = v1  * negative_slope # where negative slope is a float constant set to -1
        v4  = torch.where(v2, v1, v3)
        return v4
# Initializing the model
m = Model()
 
# Inputs to the model
x1  = torch.randn(1024, 512)
__output__  = m(x1)

