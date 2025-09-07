
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x):
        v1 = self.conv(x)
        v2 = v1 - other # subtract 'other' from the output of the convolution
        return v2

# Initializing model
m  = Model()

