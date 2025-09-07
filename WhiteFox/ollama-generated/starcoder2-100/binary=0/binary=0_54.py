
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other
        return v2

# Initializing the model with an arbitrary tensor to pass as a keyword argument for the addition operation in the forward function of the class
other  = torch.randn(32,8,64,64)
 
# Initializing the model using that arbitrary tensor to pass as the keyword argument in the forward function definition of the class
m = Model(other=other)


# Inputs to the model