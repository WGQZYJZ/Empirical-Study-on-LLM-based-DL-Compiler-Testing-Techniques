
class Model(torch.nn.Module):
    def __init__(self, arg1: int = 32):
        super().__init__()
 
        self.conv  = torch.nn.Conv2d(8, 64, 1)
 
    def forward(self, x1, y1=None):
        v1  = torch.full([arg1], 1.) 
        v2  = convert_element_type(v1, self.conv[0].weight.dtype)
        v3  = torch.cumsum(v2, 1)
        return v3


# Initializing the model
m  = Model()

 # Inputs to the model:
x1 = torch.randn(4, 8, 64, 64), y1=torch.ones_like(tensor=x1).shape
