
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
 
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x):

        v1 = x.clone()
        v1.requires_grad_(True)
        
        m1 = torch.randn(640, 512, requires_grad=True)
        m2 = torch.randn(512, 384, requires_grad=True)

        v2 = self.conv(v1)
        v3 = torch.addmm(m1, v2, m2)
        v4 = v3 + v1
        v5 = torch.cat([v4], dim=dim)
 
        return v5


# Initializing the model
m  = Model(dim=0)

# Inputs to the model
x1 = torch.randn(1, 640, 896) # Input to model

__output__  = m(x1)

