
class Model(torch.nn.Module):
    def __init__(self, other1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other1  = other1
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + self.other1
        return v2

# Initializing the model with other tensor
m  = Model(other1=torch.randn(3, 8, 64, 64))

