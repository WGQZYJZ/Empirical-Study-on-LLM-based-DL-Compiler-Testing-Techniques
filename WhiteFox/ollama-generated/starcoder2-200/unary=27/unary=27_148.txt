
class Model(torch.nn.Module):
    def __init__(self, min_value=0.3, max_value=27.84519692490049)
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x):
         v1  = self.conv(x)
         v2  = torch.clamp_min(v1, min_value)
         v3  = torch.clamp_max(v2, max_value)
         return v3

# Initializing the model with custom clamping values
m = Model(0.5, 47.863917541503906)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

