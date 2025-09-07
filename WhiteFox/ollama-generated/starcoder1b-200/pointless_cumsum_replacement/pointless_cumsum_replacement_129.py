
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        return self.conv(x)


# Initializing the model
m = Model()
x = torch.randn(1, 3, 64, 64)
