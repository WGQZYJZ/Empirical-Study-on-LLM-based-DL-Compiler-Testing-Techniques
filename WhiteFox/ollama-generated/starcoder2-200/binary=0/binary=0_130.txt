
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3,8, 1)
 
    def forward(self, x1, other=None): 
        v1  = self.conv(x1)
        v2 = v1 + other # ADDITION OPERATION
        return v2

# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(1,3,64,64)
other = 0.5 * torch.ones_like(v1)
