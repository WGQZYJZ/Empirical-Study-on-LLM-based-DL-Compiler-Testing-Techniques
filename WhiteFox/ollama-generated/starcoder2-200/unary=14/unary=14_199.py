
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = torch.sigmoid(v1)
        v3 = v1 * v2 # The output of the convolution is multiplied by the output of the sigmoid function
        return v3

# Initializing the model
m  = Model()
# Input to the model
x1 = torch.randn(1, 3, 64, 64)
 
# Output from the model
__output__  = m(x1)

