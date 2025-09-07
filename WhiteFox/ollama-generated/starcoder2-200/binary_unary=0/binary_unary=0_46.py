
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = torch.randn(32)
        v2  = self.conv(x1) + v1[0]
        v4  = torch.relu(v2)
