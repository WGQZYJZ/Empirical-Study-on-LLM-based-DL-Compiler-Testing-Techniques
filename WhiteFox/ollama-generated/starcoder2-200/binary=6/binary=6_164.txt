
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2  = v1 - other
        return v2
 
 # Initializing the model
 
m = Model()

 # Inputs to the model
 
 x1 = torch.randn(1000, 32)
 other = torch.rand(32)
 
 
