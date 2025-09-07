
class Model(torch.nn.Module):
    def __init__(self, split_size: int = 6):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 3, stride=2, padding=(split_size//2))
        self.conv2 = torch.nn.Conv2d(8, 8, 1, stride=2, padding=0)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        return v2


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
