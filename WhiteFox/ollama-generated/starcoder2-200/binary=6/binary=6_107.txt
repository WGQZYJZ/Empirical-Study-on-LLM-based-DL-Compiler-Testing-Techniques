
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1 = self.linear(x1)
        v2 = 70 - v1 
        return v2
 
 # Initializing the model
 m = Model()

 # Inputs to the model
 other = torch.randn(3,) 
 x1 = torch.randn(64, 8, 32, 32)
 