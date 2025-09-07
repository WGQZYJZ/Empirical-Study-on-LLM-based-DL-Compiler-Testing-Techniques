
class Model(torch.nn.Module):
    def __init__(self, dim=1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + torch.addmm(v1, torch.eye(64), torch.eye(64))
        v3 = torch.cat([v2], dim) 
        return v3

# Initializing the model and providing it with input dimension of 1 for concatenation along dimension 1
m = Model(dim=1)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
