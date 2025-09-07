
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(8, 3, 1)
 
    def forward(self, x1):
        v1 = self.convT(x1)
        v2 = torch.clamp_min(v1, min_value=0.5 * -torch.ones(v1).max()) # [1]
        v3 = torch.clamp_max(v2, max_value=0.7071067811865475 + 0.99*torch.ones(v2)) # [2]
        return v3


# Initializing the model
m = Model()
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
