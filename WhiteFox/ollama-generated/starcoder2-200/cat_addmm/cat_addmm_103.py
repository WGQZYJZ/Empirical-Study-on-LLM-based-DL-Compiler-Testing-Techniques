
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
         t = torch.addmm(x1[0], torch.randn(8), 3*torch.ones((4)))
         return torch.cat([t], dim=2)

 # Initializing the model
m = Model()
 
 
 # Inputs to the model
x1 = (torch.rand(5, 9))
 
 # Calling the model and getting the output
output = m(x1)
 
 
 
 