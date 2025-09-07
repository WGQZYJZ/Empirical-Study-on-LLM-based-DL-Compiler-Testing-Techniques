
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, other): # "other" is passed as a keyword argument to the addition operation.
        v1  = self.conv(x1)
        v4  = v1 + other
        return v2

# Initializing the model
m = Model()

