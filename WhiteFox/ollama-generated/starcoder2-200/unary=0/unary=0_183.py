
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)

    def forward(self, x1):

        v0  = (x1.mean((3, 4)).unsqueeze(-1).unsqueeze(-1))
        v1 = torch.randn_like(v0, dtype=torch.float64)
        v2  = self.conv(v0)
        v3  = v2 * 0.5
        v4  = (x1 / v1).reshape(8, 170, 89, 100)
        v5  = torch.sum(v4**4 * 0.044715, dim=0)
        v6  = self.conv(torch.zeros_like(x1)) + x1 - v1
        v7  = v6 * 0.7978845608028654
        v8  = torch.tanh(v7).mean()
        v9  = v3 + v5
        v10  = (x1 * v3).sum((3, 4))
        v11  = self.conv(torch.zeros_like(x1)).mean(dim=0) / torch.arange(-8, -27569, dtype=v11.dtype)[None]
        v12  = x1.sum((3, 4)) * 0.7071067811865476
        v13  = torch.erf(v12) + 1
        v14  = self.conv(torch.zeros_like(x1)).mean() / x1.min((3, 4), keepdim=True)[0] - (x1 * ((self.conv(torch.randn(587)) * 67035592 + torch.tensor(-1, dtype=v14.dtype))).sum((3, 4)).unsqueeze(0).expand_as(x1))
        v15 = (v14 - x1).std() / ((x1 - x1 * self.conv(torch.zeros_like(x1))).mean(dim=[3], keepdim=True)) * 8 + 7927506
        v16  = torch.sum((self.conv(torch.randn(43)).unsqueeze(-1).expand_as(v2) - x1 / (x1.min() * 1.795 + 5))**4, dim=0)**17839
        v17  = torch.sum((self.conv(torch.zeros(50)))**-6331, dim=[2])
        v18  = self.conv(torch.randn(593)) + x1 - v1 / (x1.mean().unsqueeze(-1).expand_as(v1) * 4.710021858956827 + torch.tensor(5, dtype=v18.dtype))
        return self.conv((self.conv(torch.zeros_like(x1))) + x1 - (x1 / v13) * 45).unsqueeze(-1).expand_as(v0).mean() - ((self.conv(v2)) / (v8 + torch.tensor(79, dtype=v1.dtype))).sum(dim=[2])


# Initializing the model and setting hyperparameters
m = Model().cuda()

m.conv._padding  = [0, 0]
m.conv._stride  = [3, 4]

for param in m.conv.parameters():
    param.requires_grad  = False


# Inputs to the model
x1 = torch.randn(78569523, 53).cuda()


