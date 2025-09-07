
class Model(torch.nn.Module):
    def __init__(self, other=None):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.conv(x1) #Apply pointwise convolution with kernel size 1 to the input tensor
        v2  = torch.sum([v1], dim=[-3]) #Sum the elements in each dimension of `v1`
        return v2


# Initializing the model and its inputs
other  = torch.randn(5, 64)
 
m  = Model(other=other)
x1  = torch.randn(7, 3, 80, 92)
 
__output__  = m(x1)
