
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
        self.sigmoid = torch.nn.Sigmoid()
 
    def forward(self, x1):
        v1 = self.conv_transpose(x1)
        v2 = self.sigmoid(v1)
        v3 = v1 * v2
        return v3


# Initializing the model
m2 = Model2()

 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
