
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
         v1 = self.conv2d(x1)
         v2 = torch.where((v1 > 0), v1, -v3)
         return v4
