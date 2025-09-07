
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1, stride=1, padding=1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + other_tensor
        v3 = torch.relu(v2)
        return v3


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(1, 3, 64, 64)
other_tensor  = torch.randn(1, 8, 50, 50)


# Initializing the model
m2= Model()

# Inputs to the model
x2  = torch.randn(1, 3, 70, 64)
other_tensor   = torch.randn(1, 8, 50, 50)

