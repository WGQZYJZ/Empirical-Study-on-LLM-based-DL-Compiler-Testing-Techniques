
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1, other):
        v1 = self.conv(x1)
        v2 = v1 + other
        return v2


# Initializing the model
m = Model()

# Inputs to the model (in this case only one tensor is passed as an argument during call of the model) 
x1 = torch.randn(1, 3, 64, 64)

__output__  = m(x1) # This should be equal to `m(x1)` in the previous version

