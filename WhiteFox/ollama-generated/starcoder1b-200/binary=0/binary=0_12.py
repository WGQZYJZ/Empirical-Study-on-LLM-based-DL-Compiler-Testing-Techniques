
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other  = other
 
    def forward(self, x1, **kwargs):
        return self.conv(x1) + kwargs['other']


# Initializing the model
m = Model(torch.randn(20))


