
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.1):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        mask = (v1 > 0).to(torch.float32)
        v3 = torch.where(mask, v1, -v1 * negative_slope) # Apply the where function to select elements from t1 or t3 based on the mask t2
        return v3

# Initializing the model
negative_slope  = 0.1 
m  = Model(negative_slope=negative_slope)


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
__output__   = m(x1)