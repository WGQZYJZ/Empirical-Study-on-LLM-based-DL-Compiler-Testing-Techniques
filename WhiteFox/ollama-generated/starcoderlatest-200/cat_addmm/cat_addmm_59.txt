
class Model(torch.nn.Module):
    def __init__(self, d_in, d_out):
        super().__init__()
        self.conv = torch.nn.Conv2d(d_in, d_out, 1)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.addmm(v1, torch.eye(4).float(), torch.ones_like(v1))
        return v2


# Inputs to the model
x1 = torch.randn(100, 3, 64, 64)
