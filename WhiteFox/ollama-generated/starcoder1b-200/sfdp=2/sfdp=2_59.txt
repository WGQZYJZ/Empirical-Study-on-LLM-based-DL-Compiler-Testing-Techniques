
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        v2 = torch.mul(v1, 0.5)
        v3 = torch.mul(v1, 0.7071067811865476)
        v4 = torch.exp(v3)
        v5 = torch.mul(v4, v2)
        v6 = torch.mul(x2, v5)
        return v6


# Inputs to the model
inputs = {
    'query': torch.randn(1, 3, 8, 8),
    'key': torch.randn(1, 8, 64, 64),
    'value': torch.randn(1, 3, 256, 1)
}
