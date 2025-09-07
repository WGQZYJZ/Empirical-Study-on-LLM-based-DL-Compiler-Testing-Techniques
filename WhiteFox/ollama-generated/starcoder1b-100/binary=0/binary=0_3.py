
class Model(torch.nn.Module):
    def __init__(self, x):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, other):
        v1 = self.conv(x1)
        v2 = v1 + other  # This operation is the same as adding a second argument to the addition operator.
        return v2


# Initializing the model
m = Model(x)


