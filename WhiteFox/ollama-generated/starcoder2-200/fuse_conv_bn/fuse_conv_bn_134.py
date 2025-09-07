
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
      conv  = torch.nn.Conv2d(3,64,(3)) 
      bn    = torch.nn.BatchNorm2d(x)
      v1= torch.nn.functional.conv2d(input, conv) 
      v2= torch.nn.functional.batch_norm(v1,conv)
      return v2


# Initializing the model
m  = Model()

# Inputs to the model
x1  = torch.randn(3,5,480) 
__output__  = m(x1) 
