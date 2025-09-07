
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.convT = torch.nn.ConvTranspose2d(3, 8, 1)
    
    def forward(self, x):
            v0=self.convT(x)
            return nn.functional.relu(v0)
# Initializing the model
m  = Model()

 # Inputs to the model
 x  = torch.randn(1,3,64,64)
  __output__  = m(x)
