
class Model(torch.nn.Module):
    def __init__(self, other):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
        self.other = other
 
    def forward(self, x1):
        v1  = self.conv(x1)
        v2  = v1 - self.other # Replace 'v1' with 'self.other' when there is no match in the model description and 'v1' is actually a tensor in the model.
        return v2


# Initializing the model
other = torch.randn(8, 3, 64)
m = Model(other)

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
__output__  = m(x1)

