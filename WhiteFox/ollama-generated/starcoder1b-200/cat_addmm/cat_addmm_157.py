
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(1, 8, 1)
 
    def forward(self, x):
        t1  = self.conv(x)
        t2 = torch.cat([t1], dim=1)  # Concatenate the result along the third dimension
        return t2


# Initializing the model
m = Model()


# Inputs to the model
x  = torch.randn(4, 1, 64, 64)
