
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = torch.conv_transpose2d(x1)
        v2  = v1 + 3
        v3  = torch.clamp(v2, min=0, max=6) 
        return torch.div(v3, 6)


# Initializing the model
m = Model()
 
# Inputs to the model
x1  = torch.randn(1, 3, 87, 45)
__output__  = m(x1)



