
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.3):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(8, 3, 1)
        self.negative_slope = negative_slope
 
    def forward(self, x1):
        v1 = self.convT(x1)
        v2 = v1 > 0
        v3 = v1 * self.negative_slope 
        v4 = torch.where(v2, v1, v3) # Where mask is True: return element in v1 else if False: return element from v3
        return v4

# Initializing the model with initial negative slope of 0.3
model = Model(negative_slope=0.3)

