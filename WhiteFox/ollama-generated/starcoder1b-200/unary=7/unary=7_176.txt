
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 3, stride=2, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 5, stride=4, padding=2)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = v1  * clamp(min=0, max=6, l1  + 3) / 6
        v3 = v2 * clamp(min=0, max=6, l2 / 6)
        return v3


# Initializing the model
m = Model()


