
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 3)
        self.conv2 = torch.nn.Conv2d(8, 8, 3)
 
    def forward(self, x1, x2):
        v1  = self.conv1(x1)
        v2  = self.conv2(v1)
        v3  = v1 * v2
        return v3


# Initializing the model
m = Model()


