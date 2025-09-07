
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        if not isinstance(other, (float, int)):
            raise TypeError("other should be of type float or int")
        else:
            self.other = other
 
    def forward(self, x):
        v1 = self.conv(x) - self.other
        return v1


# Initializing the model
m = Model()
other  = torch.rand(8, 3, 64, 64) # 'other' can be a tensor or scalar
