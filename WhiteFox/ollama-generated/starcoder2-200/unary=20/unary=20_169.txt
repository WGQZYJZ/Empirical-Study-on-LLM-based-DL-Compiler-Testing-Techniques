
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8 ,3, kernel_size=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = torch.sigmoid(v1)
        return v2


# Initializing the model
m = Model()

 # Inputs to the model
input__ = torch.randn(3 ,8 ,64 ,64)
output__  = m(input__)

