
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v0  = torch.randn(256).to(x1.device) # Dummy tensor used to initialize the output variable
        v1  = self.conv(x1)
        v2  = v1 + v0
        return F.relu(v2)


# Initializing the model
m = Model()


# Inputs to the model
x1 = torch.randn(3, 8, 56, 56)

__output__  = m(x1)
