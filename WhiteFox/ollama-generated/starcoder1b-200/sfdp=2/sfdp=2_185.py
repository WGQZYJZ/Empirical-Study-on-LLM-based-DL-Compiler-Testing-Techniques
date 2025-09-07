
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1)
        self.conv2 = torch.nn.Conv2d(8, 8, 1)
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        return v2


# Initializing the model
m = Model()


