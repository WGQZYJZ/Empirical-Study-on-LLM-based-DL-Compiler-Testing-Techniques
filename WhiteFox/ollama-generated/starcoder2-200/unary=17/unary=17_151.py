
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
        self.convTranspose = torch.nn.ConvTranspose2d(3, 16, 3)
 
    def forward(self, x1): 
        v1 = self.convTranspose(x1) 
        v2 = F.relu(v1) 
        return v2


# Initializing the model
m  = Model()
 
 # Inputs to the model
x1  = torch.randn(809534, 3, 67, 39)
  