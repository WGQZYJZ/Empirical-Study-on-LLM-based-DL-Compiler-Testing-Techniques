
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1, padding=0)
 
    def forward(self, x1):
        v1 = self.conv1(x1)
        t1 = torch.addmm(v1, m, m)
        t2 = torch.cat([t1], dim) # Concatenate the result along a specified dimension
        return t2


# Initializing the model
m = Model()

# Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
