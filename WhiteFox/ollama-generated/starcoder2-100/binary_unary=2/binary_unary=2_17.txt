
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
        self.other  = x1  # A tensor of any shape
 
    def forward(self, x1):
        v1 = self.conv(x1)
        v2 = v1 - other
        v4 = torch.relu(v2) 
        return v4
        
m = Model()


# Initializing the model
m  = Model()
 
# Inputs to the model
__x1__  = torch.randn(1,3,64,64)
__other__  = x1 # A tensor of any shape (same as __x1__)
__output__  = m(__x1__,__other__)

