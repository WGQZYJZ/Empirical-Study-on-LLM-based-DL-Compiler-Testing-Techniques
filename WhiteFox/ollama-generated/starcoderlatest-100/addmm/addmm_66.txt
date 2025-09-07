
class Model(torch.nn.Module):
    def __init__(self, inp_tensor=None):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1, inp='inp'):
        v1 = self.conv(x1)
        v2 = torch.mm(v1, v1) + inp
        return v2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
inp_tensor = torch.randn(1, 8) # The shape of the input tensor for this model is [1, 8]
