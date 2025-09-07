
class Model(torch.nn.Module):
    def __init__(self, min_value=10**-64 , max_value = 2)
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3,8,1,stride=1,padding=1)
 
    def forward(self, x):
        v1 = self.convT(x)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x  = torch.randn(1, 3, 64, 64)
__output__   = m(x)
 
