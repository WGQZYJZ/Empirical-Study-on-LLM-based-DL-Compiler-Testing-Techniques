
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x0):
         v1  = self.conv(x0)
         return v1


# Initializing the model
m = Model()

 # Inputs to the model
x1  = torch.randn(1, 4, 64, 64)
 
