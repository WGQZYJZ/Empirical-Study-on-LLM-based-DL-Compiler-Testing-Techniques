
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other
        return v2


# Initializing the model and passing "other" tensor as a keyword argument to the addition operation. 
m = Model()
__output__, other_tensor  = m(x1)

