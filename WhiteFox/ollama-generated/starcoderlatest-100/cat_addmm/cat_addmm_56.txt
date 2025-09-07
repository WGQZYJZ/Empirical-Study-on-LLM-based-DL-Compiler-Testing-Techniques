
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.dim = dim
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.addmm(v1, v1, v1) # Multiply each of the elements in tensor by its element itself and sum them together 
        v3 = torch.cat([v2], dim=self.dim)  # Concatenate along specified dimension
        return v3

# Initializing the model
m = Model(dim=2)
x1 = torch.randn(1, 3, 64, 64)
