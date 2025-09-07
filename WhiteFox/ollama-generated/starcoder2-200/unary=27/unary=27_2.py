
class Model(torch.nn.Module):
    def __init__(self, min_value=1e-5, max_value=0.9238795325112867):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min=1e-5)
        v3 = torch.clamp_max(v2, max=0.9238795325112867)
        return v3


# Initializing the model
m  = Model()

 # Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
