
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1) * 0.5
        v2 = v1  + 1
        v3 = torch.matmul(v2, x2).div(torch.sqrt(torch.mm(x1.transpose(-1, -2), x1)))
        v4 = torch.erf(v3)
        v5 = (v4  * v3).softmax(dim=-1)
        v6 = torch.matmul(v5, value)
        return v6


# Initializing the model
m = Model()


