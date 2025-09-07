
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear = torch.nn.Linear(32, 8)
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = (v1 > 0).float() * -0.5 + (v1 <= 0).float()
        v4 = v1 * v2
        return v4

m = Model()

x1  = torch.randn(64, 32)
__output__  = m(x1)

