
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3
        v3  = torch.clamp(v2, min=0) # Clamps the output of the addition operation to a minimum of 0
        v4  = torch.clamp(v3, max=6) # Clamps the output of the clamp operation to a maximum of 6
        v5  = v1 * v4 
        v6  = v5 / 6 # Divides the output of the multiplication operation by 6
        return v6


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1,8,62,62)
__output__  = m(x1)

