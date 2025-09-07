
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 3, stride=1, padding=1)
        self.conv2 = torch.nn.Conv2d(8, 16, 3, stride=1, padding=1)
 
    def forward(self, x):
        v1  = self.conv1(x)
        v2  = self.conv2(v1)
        t1 = torch.addmm(v2, v2.T, v2) # t1 is the result of performing a matrix multiplication and adding v2 to itself
        t2 = torch.cat([t1], dim=0) # t2 is the result of concatenating v2 along 0-th dimension with itself as element of the concatenation
        return t2


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(8, 3, 64, 64)
