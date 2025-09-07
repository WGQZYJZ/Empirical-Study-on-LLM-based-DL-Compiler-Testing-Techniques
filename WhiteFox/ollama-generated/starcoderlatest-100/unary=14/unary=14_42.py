
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(8, 3, 1, stride=2, padding=0)
 
    def forward(self, x2):
        v1 = self.conv_transpose(x2)
        v2 = nn.Sigmoid()(v1)
        v3 = v1 * v2
        return v3


# Initializing the model
m2 = Model2()

# Inputs to the model
x2 = torch.randn(1, 8, 64, 64)
__output__  = m2(x2)


