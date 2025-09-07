
class Model(torch.nn.Module):
    def __init__(self, other1):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1  = self.conv(x1) + other1 
        return v1


# Initializing the model with keyword argument
m  = Model(other1=torch.zeros(3)) 

# Inputs to the model (keyword arguments)
x1 = torch.randn(1, 3, 64, 64),
other1  = x1 - x1

__output__  = m(**kwargs)

