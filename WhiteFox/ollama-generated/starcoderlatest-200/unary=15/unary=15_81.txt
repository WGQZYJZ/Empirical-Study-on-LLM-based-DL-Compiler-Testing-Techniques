
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.nn.ReLU()(v1) # This line should be added to introduce non-linearity after each convolution operation
        return v2


# Initializing the model
m2 = Model()

# Inputs to the model
x2 = torch.randn(1, 3, 64, 64)
__output2__ = m2(x2)


