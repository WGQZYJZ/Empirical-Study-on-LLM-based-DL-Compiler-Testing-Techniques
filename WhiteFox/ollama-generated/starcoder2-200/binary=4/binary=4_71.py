
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v0 = torch.randn((x1)).to(device)
        v1  = torch.linear(v0) 
        return v1

 # Initializing the model
m  = Model()
 
 # Inputs to the model
  x1  = torch.rand(1234, 5678)
 