
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, kernel_size=1)
 
    def forward(self, x1):
        v1  = self.convT(x1) 
        v2 = v1 + 3
        v4  = torch.clamp(v2, min=-500) # clamp is not available on the target platform - replace with torch.max, which works the same in PyTorch 1 and 2
        v6 = torch.clamp_min(v4, max=3) / 6 
        return v6


# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 8, 7, 5)
__output__  = m(x1)

