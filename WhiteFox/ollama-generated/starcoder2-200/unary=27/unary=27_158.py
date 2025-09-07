
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.clamp_min(v1, -50) # Set the minimum value to be a negative number
        v3 = torch.clamp_max(v2, 50) # Set the maximum value to be a positive number
        return v3


# Initializing and testing the model
m  = Model()
__output1__  = m(x1)


