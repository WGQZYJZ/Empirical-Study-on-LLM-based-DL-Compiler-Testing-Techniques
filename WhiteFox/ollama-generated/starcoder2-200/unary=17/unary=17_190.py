
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1)
 
    def forward(self, x2):
        v1 = self.conv(x2)
        v2 = F.relu(v1) # This line is missing
        return v2


# Initializing the model
m2  = Model2()


# Inputs to the model
x2  = torch.randn(4,3,50,70)
__output2__ = m2(x2)
