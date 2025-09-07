
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(32, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask = (v1 > 0).to(torch.uint8) 
        v2 = v1 * negative_slope
        v3 = torch.where(mask, v1, v2)

        return v3

# Initializing the model
negative_slope=0.5
m = Model()

 # Inputs to the model
x1  = torch.randn(1, 8, 64, 64)
__output__  = m(x1)


