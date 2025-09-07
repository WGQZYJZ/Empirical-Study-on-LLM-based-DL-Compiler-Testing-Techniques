
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
         self.conv = torch.nn.Conv2d(3, 8, 1)
        return v6
 
m  = Model()
 

Inputs to the model
x1  = torch.randn(1, 3, 64, 64)

