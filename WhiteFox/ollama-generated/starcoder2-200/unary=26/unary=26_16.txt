
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1) > 0 
        v2 = v1 * -0.5
        v3 = torch.where(v1, v1, v2)
        return v3

# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(1, 8, 64, 64)
__output__  = m(x1)

