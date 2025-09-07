
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convt  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.convt(x1)
        v2  = v1 * 0.5
        v3  = v1 * 0.7071067811865476
        v4  = torch.erf(v3)
        v5  = v4 + 1
        v6  = v2 * v5 
        return v6

# Initializing the model with different initialization parameters (for example, to solve possible deadlock)
m  = Model()

 # Inputs to the model
x1 = torch.randn(3, 8, 4096, 4096)
