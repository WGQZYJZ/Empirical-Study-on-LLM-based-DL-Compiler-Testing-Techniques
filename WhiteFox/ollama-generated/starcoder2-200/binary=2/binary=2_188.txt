
class Model(torch.nn.Module):
    def __init__(self,  other = torch.tensor([1]),  ):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other = other
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - self.other 
        return v2


# Initializing the model with `other` set to a tensor of shape `[3]` and all elements set to 1:
m = Model(torch.tensor([1, 0, 4]))


# Inputs to the model. 'x1' here is the input from previous model: 
x2  = torch.randn(1, 3, 64, 64)

__output__  = m(x2)

