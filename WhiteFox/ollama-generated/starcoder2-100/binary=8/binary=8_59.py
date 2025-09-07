
class Model(torch.nn.Module):
    def __init__(self, inputTensorSize):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + x1 # x1: the 0-th argument of add, 0-th positional argument of the 4th positional argument of add
        return v2


# Initializing the model