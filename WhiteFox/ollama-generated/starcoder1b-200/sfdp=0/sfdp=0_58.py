
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 * 0.5).unsqueeze(-2).unsqueeze(-1).unsqueeze(-1)  # Scale
        v3 = (v1 * 0.7071067811865476).unsqueeze(-2).unsqueeze(-1).unsqueeze(-1)
        v4 = torch.erf(v3)
        v5 = v4 + 1
        v6 = ((v2 * v5).sum(-1).view_as(x1)).view(1, -1)
        return v6


# Inputs to the model
input_tensor = torch.randn(1, 3, 64, 64)
