
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.ConvTranspose2d(8, 3, 1)
    
    def forward(self, x1):
        v1  = self.conv(x1) 
        v2  = v1 + 3 # Addition operation
        v3  = torch.clamp(v2, min=0) # Min-max clamping
        v4  = torch.clamp(v3, max=6)# Min-max clamping
        v5  = v1 * v4 # Multiplication Operation
        v6  = v5 / 6 # Division operation
        return v6

# Initializing the model
m = Model()

# Inputs to the model
x2 = torch.randn(1,8,300,300)
 
