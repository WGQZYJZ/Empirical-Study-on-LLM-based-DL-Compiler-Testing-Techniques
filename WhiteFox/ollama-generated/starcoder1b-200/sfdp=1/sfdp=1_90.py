
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1)
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        return v2


# Inputs to the model
query = torch.randn(1, 3, 64, 64)
key   = torch.randn(8, 4, 1024, 1024)
value = torch.randn(1, 16, 1024, 1024)
