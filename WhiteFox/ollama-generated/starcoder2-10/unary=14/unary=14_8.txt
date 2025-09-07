
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.ConvTranspose2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = torch.sigmoid(v1)
        v4  = v1 * v2 # Multiply the output of the transposed convolution by the output of the sigmoid function
        return v3

# Initializing the model
m = Model()

# Inputs to the model
x1  = torch.randn(1, 8, 60, 50)
__output__  = m(x1)

