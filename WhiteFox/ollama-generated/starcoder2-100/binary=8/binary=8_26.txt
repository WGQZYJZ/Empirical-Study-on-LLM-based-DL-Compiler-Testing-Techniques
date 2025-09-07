

class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = v1 + x # Add the input tensor to another tensor
        return v2


# Initializing the model
m = Model()
x1 = torch.randn(1, 3, 64, 64)
x  = torch.randn(1, 8, 60, 60)
__output__  = m(x1, x=x)

