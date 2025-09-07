
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        v1 = self.conv1(x) 
        return v1 - other
