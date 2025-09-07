
class Model(torch.nn.Module):
    def __init__(self, other=0):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
        self.other = other
 
    def forward(self, x1):
        v1 = self.conv(x1) + self.other
        return v1


# Initializing the model with the specified keyword argument.
m  = Model(other=0.5)

 # Inputs to the model