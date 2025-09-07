
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = self.conv2d(x1)
        v3 = torch.sum(v2, 0) 
        return v3
