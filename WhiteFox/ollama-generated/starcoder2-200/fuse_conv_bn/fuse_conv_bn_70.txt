
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
         y  = torch.nn.functional.conv3d(x1)
         return (y, )

 # Initializing the model
m = Model()
 
 # Inputs to the model
x1  = torch.randn(256, 8, 30, 40, 50) 
 # Outputs of the model
  