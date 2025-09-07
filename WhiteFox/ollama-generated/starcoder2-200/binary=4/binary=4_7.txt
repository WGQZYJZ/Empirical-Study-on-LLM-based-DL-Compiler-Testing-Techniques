
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Linear(320*8 + 495 * 1 + 674 * 1, 5)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1  +  torch.randn_like(v1)
        return v2
