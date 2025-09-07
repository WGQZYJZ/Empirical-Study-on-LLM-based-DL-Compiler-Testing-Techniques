
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv_transpose = torch.nn.ConvTranspose2d(3, 8, 1, stride=1)
 
    def forward(self, x1):
        v1  = self.conv_transpose(x1) # Applying the transposed convolution to input tensor
        v2  = torch.relu(v1) 
        return v2

# Initializing model
m = Model()

# Inputs to the model
x1 = torch.randn(4, 3, 64, 64)
__output__  = m(x1)

