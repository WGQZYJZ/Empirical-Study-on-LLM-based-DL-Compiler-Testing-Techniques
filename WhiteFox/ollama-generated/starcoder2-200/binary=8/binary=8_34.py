
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3, 8, 1)
        self.other = other
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 + self.other
        return v2


# Initializing the model with a dummy keyword argument and a dummy tensor (containing random numbers) as its value for the keyword argument
other_dummy = torch.randn(5, 3, 64, 64)
 
m  = Model(other=other_dummy)


