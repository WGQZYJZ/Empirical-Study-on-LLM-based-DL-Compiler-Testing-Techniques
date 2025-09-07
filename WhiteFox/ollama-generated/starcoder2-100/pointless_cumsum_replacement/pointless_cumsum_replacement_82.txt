
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()
 
    def forward(self, x1):
       return torch.full([x1, 2], 1)
 
 
 # Initializing the model
m = Model()


# Inputs to the model
x1= torch.randn(3,4)
__output__  = m(x1)

