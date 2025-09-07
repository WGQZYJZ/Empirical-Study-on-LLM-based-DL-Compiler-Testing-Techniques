
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, kernel_size=1, stride=1, padding=0)
        self.t_conv1 = torch.nn.ConvTranspose2d(8, 32, kernel_size=4, stride=4, padding=0) 
        self.t_conv2 = torch.nn.ConvTranspose2d(32, 64, kernel_size=4, stride=4, padding=1) 
 
    def forward(self, x):
        t1 = self.conv1(x)
        v2 = torch.sigmoid(t1)
        t3 = t1 * v2
        return t3


# Initializing the model
m = Model2()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
