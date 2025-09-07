
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv2d(3, 8, 1)
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other 
        return v2

# Initializing the model
m = Model()
 
# Inputs to the model 
other = torch.randn(64, 3, 50, 50) # A 4D input tensor that's different from x1 
x1   = torch.randn(1, 3, 64, 64)
