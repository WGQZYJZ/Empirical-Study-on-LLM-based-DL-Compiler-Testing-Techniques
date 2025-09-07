
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3 # Add constant of 3 to the output of transpose conv
        v3  = torch.clamp(v2, min=0, max=6)# Clamp the output of the add operation
        v4  = v3 * 5 # Multiply the output of clamp by 5
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(2, 8, 60, 9)
__output__  = m(x1)