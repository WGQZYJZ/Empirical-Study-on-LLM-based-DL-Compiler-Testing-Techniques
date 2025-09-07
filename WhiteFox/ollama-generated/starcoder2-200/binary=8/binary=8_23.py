
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1, y1=None): # The "other" tensor is passed as a keyword argument to the addition operation
        v1 = self.conv(x1)
        if isinstance(y1, torch.Tensor):
            v2  = v1 + other
        else:
            v2 = v1
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1,3,64,64) # The first tensor is a randomly generated input tensor
y1  = m(x1)                   # No tensor passed as keyword argument "other"
y2  = m(x1, y1)               # A tensor was passed as the second keyword argument

