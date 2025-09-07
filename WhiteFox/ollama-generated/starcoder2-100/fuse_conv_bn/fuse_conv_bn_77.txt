
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = torch.nn.Conv1d(3, 50, 9)

    def forward(self, x1):
      y = conv(x1).permute(0,2,1) 
      return bn(y),

# Initializing the model
m = Model()

 # Inputs to the model 
 x1 = torch.randn(1,3,587)
__output__  = m(x1)
