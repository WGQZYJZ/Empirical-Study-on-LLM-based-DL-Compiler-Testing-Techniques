
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1) 
        v2 = v1 + torch.randn(v1.shape[0], 3, v1.size(-2), v1.size(-1))
        v3 = v2 + torch.rand(v1.shape[0], 3, v1.size(-2), v1.size(-1))
        v4 = torch.clamp_max(torch.clamp_min(v3, -5.0), 5) 
        return v4

# Initializing the model with fixed arguments.
m = Model()

 # Inputs to the model 
 x1 = torch.randn(1, 3, 64, 64)
 
 # Fixed arguments used during the inference for clarity in the example. 
 min_value = -5.0
 max_value = 5.0
 
