

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
    
    def forward(self, x1):
        v1  = self.conv(x1) + torch.randn(1, 3, 64, 64)
        v2  = torch.relu(v1) 
        return v2

m  = Model()

__output__  = m(torch.rand(10, 3, 5))

