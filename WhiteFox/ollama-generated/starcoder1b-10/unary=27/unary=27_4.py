
class Model(torch.nn.Module):
    def __init__(self, min_value=0, max_value=1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, min_value=0, max_value=1):
        v1 = self.conv(x1)
        v2 = v1 * (max_value - min_value) + min_value
        return v2


# Initializing the model
m = Model(min_value=-30, max_value=50)


