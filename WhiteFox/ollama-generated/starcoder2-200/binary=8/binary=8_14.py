
class Model(torch.nn.Module):
    def __init__(self, **kwargs):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + kwargs["other"] 
        return v2


# Initializing the model with custom tensor for "other" argument
m = Model(other = torch.zeros((8, 3)))

# Inputs to the model without specifying a value of "other" keyword arguments in the call. The default value for this argument is zeros tensor of shape (8, 3).
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

