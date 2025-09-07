
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other # "other" tensor is passed as a keyword argument to the addition operation
 
        return v2


# Initializing the model
m  = Model()


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
other = torch.tensor([0.5]) # The "other" tensor is a vector of size 8 whose values are all 0.5
 
__output__  = m(x1)

