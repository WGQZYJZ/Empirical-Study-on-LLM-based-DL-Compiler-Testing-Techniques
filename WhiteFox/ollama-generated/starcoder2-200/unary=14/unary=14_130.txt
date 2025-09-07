
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1x1 = torch.nn.Conv2d(3, 8, kernel_size=1)
        self.sigmoid = torch.nn.Sigmoid()
 
    def forward(self, x1):
        v1 = self.conv1x1(x1)
        v2 = self.sigmoid(v1)
        v3 = v1 * v2
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1 = torch.randn(8, 3, 40, 50)
