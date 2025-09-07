
class Model(torch.nn.Module):
    def __init__(self, other=0):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other
        return v2

# Initializing the model with a non-default argument for 'other' parameter
m = Model(other=4.)

