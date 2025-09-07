
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1, inp):
        v0 = torch.mm(x1, x2)
        v1  = v0 + inp
        return v1

 # Initializing the model
m  = Model()
 
# Inputs to the model 
 __input__   = torch.randn(8,4)
 __input_2__    = torch.randn(4,3)
 
 # Generating the input tensors for the model 
 x0  = torch.randn(16,5729)
 inp = torch.zeros(8,3)
 

 