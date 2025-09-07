
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = (v1 * 0.5).unsqueeze(-1).expand_as(v1)
        v3 = (v1 * 0.7071067811865476).unsqueeze(-1).expand_as(v1)
        v4 = torch.erf((v3 + 1).sqrt())
        v5 = (v2 * v4).sum(dim=2, keepdim=True)
        v6 = (v6).view(v1.shape[0], -1, 8)
        return v6


# Initializing the model
m = Model()


