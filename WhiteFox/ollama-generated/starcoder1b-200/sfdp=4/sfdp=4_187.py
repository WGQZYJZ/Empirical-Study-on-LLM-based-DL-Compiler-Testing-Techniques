
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = v1 * 0.5
        v3 = v1 * 0.7071067811865476
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = (x2 @ v5.unsqueeze(-2)) / math.sqrt(v5.size(-1))
        return v6


# Inputs to the model
input_tensor = torch.randn(1, 3, 64, 64)
query     = torch.randn(10, 8, 7, 7)
key       = torch.randn(8, 8, 7, 7)
