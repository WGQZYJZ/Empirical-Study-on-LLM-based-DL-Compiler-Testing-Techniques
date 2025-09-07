
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, other_tensor=None):
        v1 = self.conv(x1)
        if not other_tensor is None:
            v2 = v1 + other_tensor
        else:
            v2 = v1  # Set the default value of "other_tensor" to be v1 
        return v2
