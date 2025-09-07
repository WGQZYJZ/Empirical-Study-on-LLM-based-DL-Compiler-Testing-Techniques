
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1, x2, x3, x4):
        v1  = self.conv(x1) 
        v2  = v1 * 0.5   
        v3  = torch.mm(x2, x3)
        v4  = torch.mm(x4, x3)
        v5  = v3 + v4     
        return v5

# Initializing the model