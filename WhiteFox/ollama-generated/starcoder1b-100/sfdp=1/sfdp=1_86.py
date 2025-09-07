
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.matmul(v1, 0.5).mul(0.7071067811865476)
        v3 = v1 * 0.5
        v4 = v1  + 1
        v5 = torch.erf(v3)
        v6 = v2 * v5
        return v6


# Initializing the model
m = Model()


