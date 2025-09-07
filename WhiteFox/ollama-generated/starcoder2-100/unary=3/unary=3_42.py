
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1   = self.conv(x1) 
        v2   = v1 * 0.5    
        v4   = v2 * 0.7071067811865476
        v3_1 = torch.erf(v4)   
        v5_1 = v3_1 + 1      
        v6_1 = v1 * v5_1
        return v6

# Initializing the model
m2 = Model()


# Inputs to the model
x1    = torch.randn(1, 3, 64, 64)
__output__  = m2(x1)
 
