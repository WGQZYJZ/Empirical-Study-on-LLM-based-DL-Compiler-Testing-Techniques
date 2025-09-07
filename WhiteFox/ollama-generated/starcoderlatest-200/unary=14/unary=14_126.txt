
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transposed = torch.nn.ConvTranspose2d(16, 8, kernel_size=4, stride=2, padding=0)
 
    def forward(self, x1):
        v1 = self.conv_transposed(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2
        return v3


# Initializing the model
m = Model2()

# Inputs to the model
x1 = torch.randn(2, 8, 64, 64)
