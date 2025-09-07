

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = v1 * 0.5
        v3  = v1 **  2
        v4  = v1 ** 3
        v6  = (v3 * 0.044715).sqrt() * tanh(v4 + v1 + 0.7978845608028654) 
        v7  = v6 + torch.abs(torch.randn_like(t))
        v8  = 0.3703703703703704 * t + -0.19344910189682954
        return v8

# Initializing the model
m = Model()
 
# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
