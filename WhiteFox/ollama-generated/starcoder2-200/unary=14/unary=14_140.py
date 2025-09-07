
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, 1, stride=1, padding=1)
 
    def forward(self, x):
        v0  = self.conv(x)
        v1  = torch.sigmoid(v0) 
        return v1 * v0

# Initializing the model
m  = Model()
 
# Input to the model
x1  = torch.randn(1, 8, 64, 64)
__output__  = m(x1)

