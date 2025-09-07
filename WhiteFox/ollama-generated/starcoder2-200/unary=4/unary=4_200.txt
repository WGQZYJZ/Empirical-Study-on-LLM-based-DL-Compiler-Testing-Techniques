
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.linear = torch.nn.Linear(3 * 64 * 64, 3072)
    
    def forward(self, x): 
        v1 = self.conv(x)
        v2 = self.linear(v1.flatten())
        return v2

m  = Model()

x1 = torch.randn(1, 3 * 64 * 64).view(-1, 3, 64, 64)
__output__  = m(x1)