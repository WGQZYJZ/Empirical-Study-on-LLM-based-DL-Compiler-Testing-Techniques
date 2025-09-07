
class Model(torch.nn.Module):
    def __init__(self, in1 = torch.nn.Conv2d(3, 8, 1)):
        super().__init__()
        self.conv = in1
 
    def forward(self, x1, x2):
        v0 = self.conv(x2) 
        v1 = torch.mm(v0, v0)   
        v2 = torch.cat([v1] * len(x2), 3)
        return v2, [v0, v1, v2]

# Initializing the model
m  = Model()

 # Inputs to the model
 x1  = torch.randn(8, 3, 64, 64)  
 x2  = torch.randn(3, 1, 10, 10).type_as(x1)
 
 __output__  = m(x1, x2)
