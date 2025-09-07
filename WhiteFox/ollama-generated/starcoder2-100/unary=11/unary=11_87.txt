
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3
        v3  = torch.clamp_min(v2, 0) # Clamp the output of the addition operation at a minimum of `0`
        v4  = torch.clamp_max(v3, 6) # Clamp the output of the previous operation at a maximum of 6
        return v4 / 6

# Initializing the model
m1  = Model()
 
# Inputs to the model
x2  = torch.randn(8, 3, 100, 100) # Different from previous model output
__output__  = m1(x2)
