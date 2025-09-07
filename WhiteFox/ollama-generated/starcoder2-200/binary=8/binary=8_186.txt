
class Model(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.other = kwargs["other"]
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return v1 + self.other


# Initializing the model
m = Model()
m.