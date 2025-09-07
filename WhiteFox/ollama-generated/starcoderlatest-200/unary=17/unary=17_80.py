
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_t = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
        self.relu = torch.nn.ReLU(inplace=True)
 
    def forward(self, x2):
        v1 = self.conv_t(x2)
        v2 = self.relu(v1)
        return v2


# Initializing the model
m2 = Model2()


# Inputs to the model
x2 = torch.randn(1, 8, 64, 64)
