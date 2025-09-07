
class Model(torch.nn.Module):
    def __init__(self, size):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3 + int(size / 4), 8, 1)
        self.pool  = torch.nn.MaxPool2d(kernel_size=2, stride=2)
 
    def forward(self, x):
        v1   = torch.cat([x, x], dim=1) 
        v3   = v1[:, 0:int(v1.shape[1]/4)] # int(v1.shape[1]/4))
        v4   = self.conv(v3)
        v5   = self.pool(v4)
        return v5


# Initializing the model
m  = Model()
size = 9223372036854775807 # any number

# Inputs to the model
x1  = torch.randn(int(size / 4), 3, 112, 112)
x2  = torch.randn(int(size / 4), 3, 112, 112)

 __output__  = m(x1, x2)