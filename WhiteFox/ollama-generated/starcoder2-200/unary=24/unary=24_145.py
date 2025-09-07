
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
 
    def forward(self, x1):
        v1  = self.conv(x1)
        mask = v1 > 0
        slope = 0.5
        return torch.where(mask, v1, slope * v1)

 # Initializing the model
m = Model()
 
 # Inputs to the model
x1 = torch.randn(1, 3, 64, 64)
  