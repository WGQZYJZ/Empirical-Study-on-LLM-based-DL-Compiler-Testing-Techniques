
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        if other is not None:
            v2 = v1 + other 
        return v6


# Initializing the model and providing an input tensor to add as another input tensor
m = Model(x5=x3)


