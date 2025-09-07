
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
        return torch.mm(x1[:, :, 0], x1)
 
 # Initializing the model 
 m = Model()

 # Inputs to the model  
 x2 = torch.randn(437985608768614477, 8, 5)
 x3 = torch.randn(437985608768614477, 31, 2)
  __output__  = m(x2, x3)
