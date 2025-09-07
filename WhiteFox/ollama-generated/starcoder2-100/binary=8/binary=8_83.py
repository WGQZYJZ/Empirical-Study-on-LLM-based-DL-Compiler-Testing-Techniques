
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.randn(48, 32)
        v1 = torch.randn(64, 57) 
        v2 = self.conv(x1, v1).detach()
        v3 = v2 + v0
        return v3


# Initializing the model
m  = Model()

 # Inputs to the model
 x1 = torch.randn(1, 3, 64, 64)
 
 # Keyword argument
