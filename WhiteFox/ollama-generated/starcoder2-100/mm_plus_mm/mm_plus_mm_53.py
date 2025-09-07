
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm  = torch.nn.functional.linear
    
    def forward(self, x1, y1): 
        v0 = torch.nn.functional.conv2d(x1) # Convolution with kernel size 3 and stride 1 
        v1 = torch.nn.functional.conv2d(y1) # Convolution with kernel size 5 and stride 1
        return self.mm(v0, v1)

# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(32, 48, 64, 96)
y1  = torch.randn(32, 48, 70, 50)
__output__  = m(x1, y1)

