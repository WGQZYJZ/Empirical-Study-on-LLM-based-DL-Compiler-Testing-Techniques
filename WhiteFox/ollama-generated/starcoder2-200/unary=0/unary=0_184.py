
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 * 0.5
        v3  = (v1**2).sqrt()
        v4  = ((v3)**3) * 0.044715 
        v5  = v1 + v4
        v6  = ((v5)*0.7978845608028654).tanh()
        v7  = v6 + 1
        v8  = (v2*v7)
        return v8

# Initializing the model
m  = Model()

 # Inputs to the model
 x1  = torch.randn(1,3,64,64)
 
 __output__  = m(x1)