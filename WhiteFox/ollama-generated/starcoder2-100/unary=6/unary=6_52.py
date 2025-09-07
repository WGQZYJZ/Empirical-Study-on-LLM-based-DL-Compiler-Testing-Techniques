
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + 3 # Addition with constant 3
        v3 = torch.clamp_min(v2, 0) # Clamped minimum of 0 (absolute clamping)
        v4 = torch.clamp_max(v3, 6) # Clamp maximum of 6 
        v5 = v1 * v4 # Multiplication with the clamp operation result
        v6 = v5 / 6 # Division by constant 6
        return v6

# Initializing model