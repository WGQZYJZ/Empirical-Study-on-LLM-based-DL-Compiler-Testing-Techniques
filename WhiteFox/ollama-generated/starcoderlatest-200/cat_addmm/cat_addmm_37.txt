
class Model(torch.nn.Module):
    def __init__(self, dim: int=2, stride: int=4):
        super().__init__()
        self.conv1 = torch.nn.Conv2d(3, 8, 1, stride=1)
        self.conv2 = torch.nn.Conv2d(8, 8, 5, stride=4, padding=0)
 
    def forward(self, x):
        v1 = self.conv1(x)
        v2 = self.conv2(v1)
        t1 = torch.addmm(v2, v2, v2)
        t2 = torch.cat([t1], dim=1) # Concatenate the result along dimension 1
        return t2


# Initializing the model
m = Model()

# Inputs to the model
x = torch.randn(1, 3, 64, 64)
