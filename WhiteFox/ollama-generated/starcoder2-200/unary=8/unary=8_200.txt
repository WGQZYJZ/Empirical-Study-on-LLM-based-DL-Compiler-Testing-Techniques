
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x):
        v1  = self.conv(x)
        v2  = v1 + 3 
        v3  = torch.clamp(v2, min=0, max=6) # clamp operation
        v4  = v3 / 6                        # division operation
        return v4

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)


__output__  = m(x1)

