
class Model(torch.nn.Module):
    def __init__(self, conv1, other=None):
        super().__init__()
        if other is None:
            self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        else:
            self.conv = conv1
 
        # Store the "other" tensor in order to be able to use it for adding later
        self._other_tensor = other
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + self._other_tensor
        return v2


# Initializing the model with "other" tensor passed to forward method.
m = Model(conv=torch.nn.Conv2d(3, 8, 1, stride=1, padding=1), other=x1)
