
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = torch.matmul(x1, x1.transpose(-2, -1)) 
        v2  = v1 / 0.5  
        return v2
