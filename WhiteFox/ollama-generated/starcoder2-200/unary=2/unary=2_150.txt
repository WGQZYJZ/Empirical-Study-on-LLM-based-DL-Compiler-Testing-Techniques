
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convt = torch.nn.ConvTranspose2d(3, 8, kernel_size=1)
 
    def forward(self, x1):
        v1  = self.convt(x1) 
        v2  = v1 * 0.5          # <--
        v4   = (v1 ** 3) * .044715  # <--
        v3  = v1 + v4
        v6   = v3 * .7978845608028654  # <--
        v5   = torch.tanh(v6) + 1  
        v7  = v2 * v5
        return v7

# Initializing the model
m = Model()

