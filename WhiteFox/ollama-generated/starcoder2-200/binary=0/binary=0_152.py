
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        v1 = self.conv(x) + other_tensor
        return v1


# Initializing the model with initial tensor
m = Model()
other_tensor = torch.randn(10,)
 
# Inputs to the model
x = torch.randn(5, 3, 64, 64)
