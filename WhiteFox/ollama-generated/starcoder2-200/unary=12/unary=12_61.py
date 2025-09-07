
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = self.conv(x1)
        v3  = torch.sigmoid(v2) # Apply sigmoid function to the output of the convolution
        v4  = v2 * v3
        return v4


# Initializing the model
m = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)

__output__  = m(x1)