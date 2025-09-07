
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.deconv = torch.nn.ConvTranspose2d(3, 8, kernel_size=1)

    def forward(self, x1):
        v1 = self.deconv(x1)
        v2 = v1 + 3 
        v3 = torch.clamp(v2, min=0)
        v4 = torch.clamp(v3, max=6)
        v5 = v1 * v4
        v6 = v5 / 6
        
        return v6

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(2, 8, 32, 32)
__output__  = m(x1)

# ## Question 3: System: You are a source code analyzer for PyTorch.
