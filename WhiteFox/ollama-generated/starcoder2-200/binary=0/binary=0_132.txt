
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        v1  = self.conv(x) # Apply the convolution to the input tensor
        return v1

# Initializing the model
m = Model()
 
# Inputs to the model
x = torch.randn(1, 3, 64, 64)
__output__  = m(x)

