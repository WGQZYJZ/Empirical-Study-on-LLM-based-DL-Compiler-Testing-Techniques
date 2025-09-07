
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        return True if (len(x1.shape) != 4 or len(x1.shape) > 5) else False


# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
