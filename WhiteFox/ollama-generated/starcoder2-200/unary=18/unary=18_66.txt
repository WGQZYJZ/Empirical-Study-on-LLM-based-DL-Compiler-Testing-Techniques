
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = torch.sigmoid(v1)
        return v2


# Initializing the model
m = Model()
