
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.linear  = torch.nn.Linear(8, 32)
        self.leakyReLU  = torch.nn.LeakyReLU()
 
    def forward(self, x1):
        v1  = self.linear(x1)
        v2  = (v1 > 0).float()
        v3  = v1 * negative_slope
        v4  = torch.where(v2, v1, v3)
        return v4

# Initializing the model
m  = Model()
__output__  = m(torch.randn(1,8))

