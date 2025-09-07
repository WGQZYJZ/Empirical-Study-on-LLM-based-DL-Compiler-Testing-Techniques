
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + 3
        v3  = F.relu6(v2, inplace=True)
        v4  = F.hardtanh_(v3, min_val=0., max_val=6.) # F.hardtanh is deprecated from torch 1.9 onwards
        v5  = v1 * v4 
        v6  = v5 / 6
        return v6


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 8, 32, 32)
