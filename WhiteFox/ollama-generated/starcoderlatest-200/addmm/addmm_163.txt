
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, x2):
        v1 = self.conv(x1)
        inp = torch.randn(64, 1) # Add the result of the matrix multiplication to another tensor 'inp'
        v2 = torch.matmul(v1, inp)
        return v2
# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
x2 = torch.randn(64, 1)
