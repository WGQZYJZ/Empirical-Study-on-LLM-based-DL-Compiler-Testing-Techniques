
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(3, 8)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, min_value=0.0) # minimum of (v1 + v5)/2 is not zero
        v3 = torch.clamp_max(v2, max_value=1.0)  # maximum of (v1 + v5)/2 - minimum of (v1 + v5)/2 is 1
        return v6


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
