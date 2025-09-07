
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.5):
        super().__init__()
 
        self.convT  = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.convT(x1)
        v2 = (v1 > 0).float() 
        v3 = v1 * negative_slope 
        v4 = torch.where((v2 == True), v1, v3)
        return v4


# Initializing the model
m = Model(negative_slope=0.5)
# Inputs to the model
x  = torch.randn(1, 8, 64, 64)
