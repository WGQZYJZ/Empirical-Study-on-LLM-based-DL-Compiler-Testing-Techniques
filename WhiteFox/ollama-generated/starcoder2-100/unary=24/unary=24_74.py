
class Model(torch.nn.Module):
    def __init__(self, negative_slope=0.5):
        super().__init__()
        self.conv  = torch.nn.Conv2d(3,8,1)
        self.negative_slope  = negative_slope
 
    def forward(self, x1):
       v1  = self.conv(x1)
       mask  = v1 > 0 
       v4  = self.negative_slope * v1
       v5  = torch.where(mask, v1, v4)
      return v5
 
m  = Model()


