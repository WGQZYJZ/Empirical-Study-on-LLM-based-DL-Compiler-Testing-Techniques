
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = torch.zeros(x1.shape[0], 4) + 0.5
        v3 = torch.cat([v2] * 8, dim=1)
        v1 = torch.randn(3, 3)
        v7 = F.conv2d(v1, v3, bias=None, stride=[2, 2], padding=(4, 0), dilation=2, groups=5)
        v9 = v7 + x1
        v8 = torch.relu(v9)
        return v8

# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(3, 64, 64)
__output__  = m(x1)


