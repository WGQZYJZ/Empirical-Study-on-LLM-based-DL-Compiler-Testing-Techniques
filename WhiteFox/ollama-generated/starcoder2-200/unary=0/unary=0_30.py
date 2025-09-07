
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1   = self.conv(x1)
        v2_0 = v1 * 0.5
        v2_1 = v2_0 + 0
        v3   = (v2_1 ** 3) * 0.044715 
        v4   = v1 + v3
        v5   = torch.tanh(v4 - 0) # Change 0 to 1 or some constant
        v6_0 = v5 * 0.7978845608028654  # Change 0.7978845608028654 to 1, 1 + sqrt(3), -1 etc...
        v6_1 = v6_0 * 1
        v6   = torch.add(v6_1, v1) # Change v6_1 to [0] or [torch.ones(v6)] or 1 or 2
        v7   = v2_0 * v6
        return v7


# Initializing the model