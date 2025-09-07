
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v = torch.nn.functional.conv_transpose2d() + 1
        return v
 
 # Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(10, 3, 8)
 
__output__  = m(x1)

