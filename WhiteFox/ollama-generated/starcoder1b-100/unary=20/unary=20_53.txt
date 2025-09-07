
class UpsampleModel(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        v = self.conv(x)
        return torch.sigmoid(v)


# Initializing the model
m = UpsampleModel()


# Inputs to the model
x = torch.randn(2, 3, 64, 64)
