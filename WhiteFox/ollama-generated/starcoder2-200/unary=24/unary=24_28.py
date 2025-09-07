

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        mask  = v1 > 0 
        v4  = -v1 * 5.0
        v7  = torch.where(mask, v1, v4) # Replace the negative values in v1 with 25.0
        return v7

# Initializing the model
m = Model()
__output__  = m(x1)


