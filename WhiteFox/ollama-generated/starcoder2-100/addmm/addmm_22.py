
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.MM()
 
    def forward(self, x1, inp=None):
        v1  = self.mm(x1) 
        if inp is not None:
            v2 = v1 + inp 
        else:
             v2 = v1
        return v2
 
# Initializing the model
m = Model()

 # Inputs to the model
x1, x2  = torch.randn(300), torch.randn(400)
 
 __output__  = m(x1, inp=x2)
