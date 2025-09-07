
class Model(torch.nn.Module):
    def __init__(self, ksize=1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, ksize)
 
    def forward(self, x1):
        v1 = self.conv(x1) + self._other_tensor
        return v1


# Initializing the model
m = Model()
m._other_tensor  = torch.randn(2, 3, 64, 64) # The tensor to add as a keyword argument
 
# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

