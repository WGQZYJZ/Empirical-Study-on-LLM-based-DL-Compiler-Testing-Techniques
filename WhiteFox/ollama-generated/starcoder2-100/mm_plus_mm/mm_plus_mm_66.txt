
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm  = torch.nn.functional.mm
 
    def forward(self, x1=None, y1=None, z1=None):
        v1  = self.mm(x1, y1)
        v2  = self.mm(z1, y1) 
        v3  = v1 + v2
        return v3

# Initializing the model
m  = Model()

 # Inputs to the model
input1  = torch.randn(50, 64)
input2  = torch.randn(64, 78)
 
input3  = torch.randn(50, 78)
input4  = torch.randn(64, 78) 
 
__output__  = m(x1=input1, y1=input2, z1=input3)

