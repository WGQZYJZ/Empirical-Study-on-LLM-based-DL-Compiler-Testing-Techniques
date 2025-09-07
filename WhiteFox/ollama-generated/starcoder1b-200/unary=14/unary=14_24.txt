
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.glu   = torch.nn.GLU()
 
    def forward(self, x1):
        v1 = self.conv_1(x1)
        v2 = self.glu(v1) * torch.sigmoid(v1)
        return v2


# Initializing the model
m = Model()

