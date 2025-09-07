
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, size):
        v1 = torch.cat([x1, x1[:, size:]], dim=1)
        return v1


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
size = int(x1.size()[2]) * int(x1.size()[3])
