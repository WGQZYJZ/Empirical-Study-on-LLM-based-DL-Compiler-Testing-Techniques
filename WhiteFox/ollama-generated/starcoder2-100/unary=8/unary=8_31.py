
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT  = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v0  = 3
        v1  = self.convT(x1) + v0 
        v2  = torch.clamp(v1, min=0)
        v3  = torch.clamp(v2, max=6)
        v4  = v1 * v3 # 38
        return v4 / 6

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 7, 50)

# Outputs from the model for inputs x1 
output = m(x1)

