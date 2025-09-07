
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 + torch.rand_like(v1, dtype=torch.float) # Add torch.rand_like() to the output of the convolution with "torch.rand_like(x, 50)" being the keyword argument
        return v2

# Initializing model
m = Model()

