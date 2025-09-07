
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.2):
        super().__init__()
        self.conv1 = torch.nn.ConvTranspose2d(64, 32, 4, stride=2, padding=1)
        self.conv2 = torch.nn.ConvTranspose2d(32, 16, 4, stride=2, padding=1)
        self.conv3 = torch.nn.ConvTranspose2d(16, 8, 4, stride=2, padding=1)
        self.conv4 = torch.nn.ConvTranspose2d(8, 1, 4, stride=2, padding=1)
        self.negative_slope = negative_slope
 
    def forward(self, x):
        v1 = self.conv1(x)
        t1 = torch.where(v1 > 0, v1, self.negative_slope * v1)
        v2 = self.conv2(t1)
        t2 = torch.where(v2 > 0, v2, self.negative_slope * v2)
        v3 = self.conv3(t2)
        t3 = torch.where(v3 > 0, v3, self.negative_slope * v3)
        v4 = self.conv4(t3)
        t4 = torch.where(v4 > 0, v4, self.negative_slope * v4)
        return t4
 
# Initializing the model
m = Model()
 
# Inputs to the model
x = torch.randn(1, 64, 128, 128)
