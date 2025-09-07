
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = v1 + other # Pass another tensor as a keyword argument to the addition operation in the convolution layer of the model
        return v2


# Initializing the model and providing input to the model
m  = Model(other=torch.randn(3, 8, 4, 4))
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

