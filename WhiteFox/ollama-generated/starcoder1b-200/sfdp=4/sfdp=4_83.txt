
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 * 0.5).unsqueeze(1) # batch size:1, channels: 3, kernel size 1, stride:1, padding: 1
        v3 = (v1 * 0.7071067811865476).unsqueeze(1) # batch size:1, channels: 3, kernel size 1, stride:1, padding: 1
        v4 = torch.erf(v3).unsqueeze(1) # batch size:1, channels: 1, kernel size 1, stride:1, padding: 1
        v5 = v4 + 1
        v6 = (v2 * v5).transpose(-2, -1) # batch size:1, channels: 3, kernel size 1, stride:1, padding: 1
        return v6


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
