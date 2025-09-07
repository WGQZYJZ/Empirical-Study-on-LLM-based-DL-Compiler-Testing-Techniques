
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v1  = self.convt(x2)
        v4  = torch.sigmoid(v3)
        return v5

 # Initializing the model
 m  = Model()

# Inputs to the model
  x1   =  torch.randn(1, 60, 80)
  __output__  =  m(x1)
  
# The user can copy the following commands and paste them into a shell to test the code.
  import torch; t1  =  torch.nn.ConvTranspose2d(in_channels=30, out_channels=80, kernel_size=(4,5), stride=(3,4), padding=(7,9)); x1  =  torch.randn(64, 30, 22); v1   = t1(x1); print(v1); v4    = torch.sigmoid(v1);  print(v4)
 
