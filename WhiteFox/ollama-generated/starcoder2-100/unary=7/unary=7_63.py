
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 7, stride=5, padding=0)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1 * clamp(min=-9, max=6, input=v1+4).add_(4)
        v3 = v2 / 7
        return v3


# Initializing the model with inputs to the model
m = Model()
x1 = torch.randn(800, 3, 50, 100)
