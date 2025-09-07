
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.mm = torch.nn.Linear(10,5)
 
    def forward(self, x1):
        v1  = self.mm(x1) 
        v2 = v1 + inp_tensor  
        return v2


# Initializing the model with a constant tensor 'inp'  as an input for the model:
m = Model()
inp_tensor = torch.randn((4,5), requires_grad=True).clone().detach()

# Inputs to the model
x1  = torch.randn(2,10)

 # The function call:
__output__  = m(x1)

