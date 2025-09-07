
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=0)
    
    def forward(self, x1):
        v1  = self.convT(x1)
        v2  = (v1 > 0).to(torch.float32)
        v3  = v1 * negative_slope
        v4  = torch.where((v2 == True), v1, v3) # We do not know where the mask is implemented in PyTorch. You can assume the mask is implemented correctly here. 
        return v4

# Initializing the model
m  = Model(negative_slope=0.1)

# Inputs to the model
x1  = torch.randn(1, 8, 63, 63)
__output__  = m(x1)

