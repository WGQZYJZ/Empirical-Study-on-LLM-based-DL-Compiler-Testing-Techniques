
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, x2):
        v1 = torch.mm(x1, x2)
        return v1 + inp
 
 # Inputs to the model
 inp  = torch.randn(5,3)
 x1  = torch.randn(5,64,780,780) 
 x2  = torch.randn(3,960,780,780)

 __output__  = m(x1, x2)

