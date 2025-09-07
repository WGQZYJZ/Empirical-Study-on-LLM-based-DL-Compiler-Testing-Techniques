
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        t1 = torch.full([4], 1, dtype=torch.float64, layout='csr', device=torch.device('cuda'))
        t2 = t1 * 0.5
        t3 = t1 * 0.7071067811865476
        v2 = torch.erf(t3)
        t4 = v2 + 1
        t5 = t2 * t4
        return t5


# Initializing the model
m = Model()


