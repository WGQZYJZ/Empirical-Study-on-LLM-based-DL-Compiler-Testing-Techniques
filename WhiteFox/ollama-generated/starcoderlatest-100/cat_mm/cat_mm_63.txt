
class Model(torch.nn.Module):
    def __init__(self, num_channel1, num_channel2):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, kernel_size=4)
        self.conv2 = torch.nn.Conv2d(8, 64, kernel_size=4)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        v2 = self.conv2(v1)
        v3 = torch.mm(v1, v2)
        v4 = torch.cat([v1, v1, v1], dim=1)
        return v4


# Initializing the model
m = Model()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
