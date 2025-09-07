
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.25718963790405405):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        mask_v1  = v1 > 0
        v2  = v1 * negative_slope
        result  = torch.where(mask_v1, v1, v2)
        return result

# Initializing the model
negative_slope = 0.25718963790405405
m = Model(negative_slope=negative_slope)

 # Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
  