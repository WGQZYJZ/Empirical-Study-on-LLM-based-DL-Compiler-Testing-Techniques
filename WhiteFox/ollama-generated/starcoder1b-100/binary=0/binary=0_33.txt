
class Model(torch.nn.Module):
    def __init__(self, x1=None, other=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other = other
 
    def forward(self, x1):
        return self.conv(x1)+self.other


# Inputs to the model
m = Model()
