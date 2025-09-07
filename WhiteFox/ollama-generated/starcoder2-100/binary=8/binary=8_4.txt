
class Model(torch.nn.Module):
    def __init__(self, v0):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)

    def forward(self, x1, **kwargs):
        v1 = self.conv(x1)
        return v1 + kwargs['v0']


# Initializing the model with "other" tensor 
v0 = torch.zeros((24)) # Please generate a tensor with shape of (6, 8). If you need, you can also specify the shape in __init__.
m = Model(v0) 


# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)

 # Call the model with the keyword argument "other".
