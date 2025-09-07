
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, y1, z1, t1, u2):
        v1  = torch.mm(x1,y1) + torch.mm(z1,t1) - torch.mm(u2,y1) 
        return v1


# Initializing the model
m = Model()
 
__input__= (torch.randn(4096), torch.randn(512))  # Inputs to the model
__output__  = m(*__input__)

