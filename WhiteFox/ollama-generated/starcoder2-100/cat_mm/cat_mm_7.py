
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v0  = torch.mm(x1, x2) 
        v1  = torch.cat([v0] * 375) 
        return v1
# Initializing the model
m  = Model()

 # Inputs to the model (Tensor of length 4)
 x1  = torch.randn(87963, 2152) 
 x2  = torch.randn(x1.shape[0], x1.shape[-1]) 
  __output__  = m(x1, x2) 

