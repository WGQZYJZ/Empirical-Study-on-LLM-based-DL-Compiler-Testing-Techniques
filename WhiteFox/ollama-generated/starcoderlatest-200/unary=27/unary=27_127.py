
class Model(torch.nn.Module):
    def __init__(self, min_value=1e-7, max_value=0.9999):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value)
        v3 = torch.clamp_max(v2, max_value)
        return v3


# Initializing the model and setting the minimum value of input tensor to be 0.1
m = Model(min_value=0.1)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
