
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + other  # <-- Other is a keyword argument here
        return v2


# Initializing the model and passing in an argument to the addition operation
m = Model()
 
other_tensor  = torch.randn(3,8,64,64)
__output__   = m(x1, other=other_tensor) # <-- Now we are passing this tensor as a keyword argument to the addition operation

