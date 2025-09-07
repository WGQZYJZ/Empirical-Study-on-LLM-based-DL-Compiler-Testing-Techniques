
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1) + 3 
        v2  = torch.clamp(v1, min=0)  
        v3  = torch.clamp(v2, max=6)   
        v4  = v1 * v3 
        v5  = v4 / 6
        return v5

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)

__output__  = m(x1)

# __solution__
m  = Model()

x1_fixed = 0.7 * x1 + 1e-2*torch.rand(1, 3, 64, 64).to('cpu')

output = m(x1_fixed)
