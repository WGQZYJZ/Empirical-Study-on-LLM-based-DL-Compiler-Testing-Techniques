
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.randn(32, 8) * -9e-4
        v1 = torch.sigmoid(v0 + 35.)
        v1 = v1 / 6
        return v1

m = Model()

