
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(8, 4, 1, stride=2, padding=0)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        return v1 + 2


# Initializing the model
m = Model()

