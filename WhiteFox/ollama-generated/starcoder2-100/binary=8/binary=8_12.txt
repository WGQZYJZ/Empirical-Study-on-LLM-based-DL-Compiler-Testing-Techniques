
class Model(torch.nn.Module):
    def __init__(self, a = torch.randn(10)):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
        self.a = a
        
    def forward(self, x1):
        v1 = self.conv(x1)
        v4 = v1 + self.a
        return v4

# Initializing the model