
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1): 
        v1  = torch.conv_transpose2d(x1)
        v2  = v1 + 3
        v3  = torch.clamp(v2, min=0)
        v4  = torch.clamp(v3, max=6)
        v5  = v1 * v4 
        v6  = v5 / 6
        return v6

# Initializing the model
m  = Model()

 # Inputs to the model
 x1  = torch.randn(1, 7, 832, 90)
 
 
__output__  = m(x1)
