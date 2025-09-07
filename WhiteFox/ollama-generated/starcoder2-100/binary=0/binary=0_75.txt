
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.other = other
 
    def forward(self, x):
        v1  = self.conv(x)
        v2  = v1 + self.other
        return v2


# Initializing the model with keyword arguments