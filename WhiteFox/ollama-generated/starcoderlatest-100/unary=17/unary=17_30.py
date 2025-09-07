
class Model2(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(8, 3, 1, stride=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.relu(v1)
        return v2
# Initializing the model
m2 = Model2()

 # Inputs to the model
x1  = torch.randn(1, 8, 64, 64)
__output__  = m2(x1)
 
 