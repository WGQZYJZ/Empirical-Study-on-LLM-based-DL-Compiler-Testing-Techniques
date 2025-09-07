
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m = Model()
other  =  torch.zeros((1,8,64,64)) # A tensor that is added to the output of the convolution


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64) # An input tensor that is passed to the convolution layer in the forward method of the model above
__output__   = m(x1)
