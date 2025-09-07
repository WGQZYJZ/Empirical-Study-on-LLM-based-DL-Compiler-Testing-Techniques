
class Model(torch.nn.Module):
    def __init__(self, ...):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(...)
        self.conv2 = torch.nn.Conv2d(...)

    def forward(self, x1):
        v1  = self.conv1(x1)
        v2  = self.conv2(v1)
        return v2


# Initializing the model
m = Model(...)

# Inputs to the model
x1 = ...
