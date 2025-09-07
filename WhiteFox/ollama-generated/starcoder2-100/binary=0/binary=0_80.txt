

class Model(torch.nn.Module):
    def __init__(self,  **kwargs):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v4 = 0 + kwargs['other']
        return v4


m = Model(**{'other': torch.tensor([2.,3])})
