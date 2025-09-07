
class Model(torch.nn.Module):
    def __init__(self, conv2d=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
        if (not conv2d is None) and isinstance(conv2d, str):
            exec('self.conv' + conv2d + ' = conv2d')

    def forward(self, x1):
        v1 = self.conv(x1)
        if (not self.conv2d is None):  # Added 12-07-2020
            v2 = v1 + self.conv2d(v1).detach()
        else:
            v2 = v1

        return v2

# Initializing the model with keyword argument conv2d=' * 5'
m  = Model(conv2d=None)


# Inputs to the model that will be passed in to Model
x1  = torch.randn(1, 3, 64, 64)
__output__  = m(x1)
