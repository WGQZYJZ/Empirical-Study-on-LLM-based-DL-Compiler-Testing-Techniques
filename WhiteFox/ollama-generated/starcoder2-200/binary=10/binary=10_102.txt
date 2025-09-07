
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = self.conv(x1) + other
        return v2

 # Initializing the model
 m  = Model()
 
 # Inputs to the model
 other = torch.randn(32)
 x1   = torch.randn(1, 3, 64, 64) 
 