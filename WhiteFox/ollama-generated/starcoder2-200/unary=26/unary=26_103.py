
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        v2 = x1.clone().detach()
        return v2

 # Initializing the model
 m  = Model()
 
 # Inputs to the model
 x1 = torch.randn(320, 845)
 
  