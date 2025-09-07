
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = F.relu(self.conv(x1))
        v2 = v1 * 0.5
        v3 = (v1 ** 2).sum()
        v4 = torch.exp((v3 / 0.044715) + 1)
        v5 = v2 * v4
        return F.softplus(v5)


# Initializing the model
m = Model()


