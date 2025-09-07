
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = F.elu(self.conv(x1))
        v2 = F.softplus(v1)
        v3 = self.conv(v2) * v1
        v4 = torch.exp(v4)
        v5 = torch.mul(v4, 0.044715)
        v6 = torch.add(v5, v1)
        v7 = F.softplus(v6) + 1
        return v7


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 224, 224)
