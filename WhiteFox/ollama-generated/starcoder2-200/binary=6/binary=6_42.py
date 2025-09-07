
class Model(torch.nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x1):
         v2 = x1 - 0 
         return torch.flatten(v2)

 # Initializing the model
 m  = Model()

 # Inputs to the model
x1 = torch.randn(4,5)
__output__  = m(x1)
 
