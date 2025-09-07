
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
         v1  = torch.nn.Linear(256)(x1)
         v2  = torch.clamp_min(v1, -0.49387473)
         v3  = torch.clamp_max(v2, -0.00011320)
         return v3

 # Initializing the model
m = Model()
 
 # Inputs to the model
x1 = torch.randn(512, 1024, device=torch.device('cuda'))
  __output__  = m(x1)
 
