
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 2, stride=2, padding=0)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
query  = torch.randn(16, 3, 1, 1)
key    = torch.randn(16, 8, 4, 4)
value   = torch.randn(16, 16, 1, 1)
