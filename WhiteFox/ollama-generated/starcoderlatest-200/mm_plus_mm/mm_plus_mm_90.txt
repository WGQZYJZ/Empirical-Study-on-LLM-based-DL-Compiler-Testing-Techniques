
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
        self.conv2 = torch.nn.Conv2d(8, 4, 1, stride=1, padding=0)
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        v3 = torch.mm(v1, v2) # Addition of the two matrix multiplications performed in previous layer
        return v3


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
