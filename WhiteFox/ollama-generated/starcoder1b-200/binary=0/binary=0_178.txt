
class Model(torch.nn.Module):
    def __init__(self, other_tensor=1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, **kwargs):
        v1 = self.conv(x1)
        v2 = v1 + kwargs["other"]
        return v2


# Initializing the model
m = Model()
other_tensor = torch.randn(3, 3, 64, 64)
