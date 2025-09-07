
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x1): 
        v1 = self.conv(x1)

        mask  = v1 > 0
        neg  = -torch.ones_like(v1)*negative_slope
        v3  = torch.where(mask, v1, v2)
        return v3

# Initializing the model with a negative slope of 0.5
m = Model(-0.5)

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
  